import requests
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_company(html_content):
    API_KEY = os.getenv("TOGETHER_API_KEY")  # ✅ Correct key name
    if not API_KEY:
        return {"insight": "API key not found. Please check your .env file."}

    prompt = f"What does this business do based on the following HTML?\n\n{html_content[:3000]}"

    response = requests.post(
        "https://api.together.xyz/inference",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "meta-llama/Llama-3-8b-chat-hf",
            "prompt": prompt
        }
    )

    try:
        if response.status_code == 200:
            output = response.json().get("output", "No output returned.")
            return {"insight": output}
        else:
            return {"insight": f"Error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"insight": f"Exception occurred: {str(e)}"}
