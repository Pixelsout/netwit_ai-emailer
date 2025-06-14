from fastapi import FastAPI, UploadFile, File, HTTPException, Path
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import pandas as pd
from io import StringIO
from backend.email_parser import parse_email
from backend.scraper import scrape_website
from backend.llm_integration import analyze_company
from backend.email_generator import generate_email_html
from backend.send_email import send_email
from backend.status_db import log_status
from backend.analytics import router as analytics_router  # ✅ NEW

import logging

app = FastAPI()
app.include_router(analytics_router)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup logging
if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(filename="logs/app.log", level=logging.INFO)

# Cache to store HTML previews
email_cache = {}

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <h2>✅ NetWit AI Email Automation is running!</h2>
    <p>Visit <a href="/docs" target="_blank">/docs</a> to upload emails and test the API.</p>
    """

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a valid CSV file.")

    try:
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))

        if "email" not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must contain 'email' column.")

        responses = []

        for email in df["email"]:
            try:
                name_data = parse_email(email)
                domain = name_data["domain"]
                full_name = name_data["full_name"]
                logging.info(f"Processing: {email}")

                html_content = scrape_website(domain)
                insights_data = analyze_company(html_content)
                insight = insights_data.get("insight", "No insight available.")

                email_body = generate_email_html(full_name, domain, insight)
                email_cache[email] = email_body  # Store HTML

                subject = f"Quick insights for {full_name} from NetWit AI"
                send_status = send_email(to_email=email, subject=subject, html_content=email_body)

                log_status(email, send_status)

                responses.append({
                    "email": email,
                    "status": send_status
                })

            except Exception as e:
                logging.error(f"Failed for {email}: {e}")
                responses.append({
                    "email": email,
                    "status": "failed",
                    "error": str(e)
                })

        return JSONResponse(content={"results": responses})

    except Exception as e:
        logging.error(f"Upload failed: {e}")
        raise HTTPException(status_code=500, detail="Error processing file.")

# Preview Route
@app.get("/preview/{email}")
def preview_email(email: str = Path(...)):
    return HTMLResponse(content=email_cache.get(email, "No preview available."))
