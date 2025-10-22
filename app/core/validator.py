#validator.py
import json, re

def validate_summary(raw_output: str):
    clean = re.sub(r"```(?:json)?|```", "", raw_output).strip()

    # Extract first JSON block if present
    match = re.search(r"\{.*\}", clean, re.DOTALL)
    if match:
        clean = match.group(0)

    # Try parsing JSON safely
    try:
        parsed = json.loads(clean)
        parsed["valid"] = True
    except json.JSONDecodeError:
        parsed = {"summary": raw_output, "valid": False}

    return parsed