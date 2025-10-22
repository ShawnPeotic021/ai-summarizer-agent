# app/core/summary_schema.py
from pydantic import BaseModel
from typing import List

class SummarySchema(BaseModel):
    customer_name: str
    product: str
    reason: str
    notes:List[str]
    summary: str
