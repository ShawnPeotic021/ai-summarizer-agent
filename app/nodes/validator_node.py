#add validator node
from app.core.validator import validate_summary

def validator_node(state):
    print("🟢 Running node: Validator_node")
    verified = validate_summary(state["summary"])
    return {
        "validated_summary": verified,
        "valid": verified.get("valid", False)  # ✅ surface 'valid' to top-level
    }



