def compare_companies(companies):
    """
    Compare information collected about multiple companies.
    """

    comparison = []

    for company in companies:
        comparison.append({
            "company": company.get("company", "Unknown"),
            "products": company.get("products", []),
            "strengths": company.get("strengths", []),
            "weaknesses": company.get("weaknesses", []),
            "pricing": company.get("pricing", "Unknown"),
            "market_position": company.get(
                "market_position",
                "Unknown"
            )
        })

    return comparison

