def create_executive_report(synthesis):
    """
    Create a structured executive-level business report.
    """

    report = {
        "title": "AI Business Research & Competitive Intelligence Report",

        "executive_summary": synthesis.get(
            "key_findings", []
        ),

        "verified_facts": synthesis.get(
            "verified_facts", []
        ),

        "conflicting_information": synthesis.get(
            "conflicting_information", []
        ),

        "inferences": synthesis.get(
            "inferences", []
        ),

        "unknown_information": synthesis.get(
            "unknown_information", []
        ),

        "sources": synthesis.get(
            "sources", []
        )
    }

    return report
