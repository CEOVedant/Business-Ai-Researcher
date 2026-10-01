def verify_information(claim, source_text):
    """
    Basic verification layer.

    Returns the claim, available evidence,
    and a verification status.
    """

    if not claim:
        return {
            "claim": "",
            "evidence": "",
            "status": "Unknown"
        }

    if not source_text:
        return {
            "claim": claim,
            "evidence": "",
            "status": "Needs Verification"
        }

    # Basic evidence check
    if claim.lower() in source_text.lower():
        status = "Verified"
    else:
        status = "Needs Verification"

    return {
        "claim": claim,
        "evidence": source_text[:1000],
        "status": status
    }
