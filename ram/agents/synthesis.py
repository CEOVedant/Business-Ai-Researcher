def create_synthesis(research_data):
    """
    Organize all research into a structured
    executive decision brief.
    """

    return {
        "verified_facts": research_data.get(
            "verified_facts", []
        ),

        "conflicting_information": research_data.get(
            "conflicting_information", []
        ),

        "inferences": research_data.get(
            "inferences", []
        ),

        "unknown_information": research_data.get(
            "unknown_information", []
        ),

        "key_findings": research_data.get(
            "key_findings", []
        ),

        "sources": research_data.get(
            "sources", []
        )
    }
