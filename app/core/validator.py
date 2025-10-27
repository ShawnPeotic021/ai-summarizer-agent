#validator.py
import time
start = time.time()
print("Before")
from langchain_core.output_parsers import PydanticOutputParser
from app.schemas.summary_schema import SummarySchema

#initialize the parser
parser = PydanticOutputParser(pydantic_object = SummarySchema)
end = time.time()
print(f"after:{end -start: .5f} ")


def validate_summary(raw_output: str):
    try:
        verified_output = parser.parse(raw_output).model_dump()

        # optional runtime check for "notes" completeness
        if "notes" in verified_output and len(verified_output["notes"]) != 2:
            print("⚠️ Incomplete notes field detected — auto-fixing to 2 items.")
            verified_output["notes"] = (
                verified_output["notes"][:1] + ["missing final outcome"]
                if verified_output["notes"]
                else ["missing agent response", "missing final outcome"]
            )

        return {"summary": verified_output, "valid": True}
    except Exception as e:
        print("⚠️ Schema parsing failed:", e)
        return {"summary": raw_output, "valid": False}