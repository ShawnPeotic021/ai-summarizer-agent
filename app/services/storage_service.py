import requests
import os
from app.schemas.summary_schema import SummarySchema

CRM_URL = os.getenv("CRM_API_URL")  # e.g. "https://crm.example.com/api/summaries"

def save_summary_to_crm(summary: SummarySchema):
    """Send structured summary to external CRM or DB API."""
    try:
        response = requests.post(CRM_URL, json = summary.model.dump())
        response.raise_for_status()
        print(f"✅ Saved summary for {summary.customer_name} to CRM.")
        return{"status": "success","crm_id":response.json().get("id")}
    except Exception as e:
        print(f"⚠️ Failed to save summary: {e}")
        return {"status": "error", "error": str(e)}
