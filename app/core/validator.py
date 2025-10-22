#validator.py
from langchain_core.output_parsers import PydanticOutputParser
from app.core.summary_schema import SummarySchema

#initialize the parser
parser = PydanticOutputParser(pydantic_object = SummarySchema)

def validate_summary(raw_output: str):
    try:
        verified_output = parser.parse(raw_output).model_dump()
        return {"summary": verified_output, "valid": True}
    except Exception as e:
        print("⚠️ Schema parsing failed:", e)
        return {"summary": raw_output, "valid": False}