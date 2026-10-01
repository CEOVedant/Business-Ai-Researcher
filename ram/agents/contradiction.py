def detect_contradictions(evidence):
    """
    Detect potential conflicts between evidence
    from different sources.

    This is a basic heuristic version.
    Final verification will be handled by the AI layer.
    """

    potential_conflicts = []

    keywords = [
        "revenue",
        "sales",
        "profit",
        "price",
        "market share",
        "growth",
        "production",
        "customers"
    ]

    for keyword in keywords:

        matching_items = []

        for item in evidence:

            claim = item.get("claim", "").lower()

            if keyword in claim:
                matching_items.append(item)

        # If multiple sources discuss the same metric,
        # flag it for later verification.
        if len(matching_items) > 1:

            sources = []

            for item in matching_items:
                source = item.get("source", "Unknown")

                if source not in sources:
                    sources.append(source)

            if len(sources) > 1:

                potential_conflicts.append({
                    "topic": keyword,
                    "sources": sources,
                    "status": "Needs Verification"
                })

    return potential_conflicts