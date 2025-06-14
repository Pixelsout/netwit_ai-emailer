from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os
import csv

router = APIRouter()

@router.get("/analytics/")
def get_email_stats():
    sent = failed = 0
    log_path = "logs/email_status.csv"

    if not os.path.exists(log_path):
        return JSONResponse(content={"sent": 0, "failed": 0, "opened": 0, "clicked": 0})

    with open(log_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "sent" in row["status"]:
                sent += 1
            elif "failed" in row["status"]:
                failed += 1

    return JSONResponse(content={
        "sent": sent,
        "failed": failed,
        "opened": 0,
        "clicked": 0
    })
