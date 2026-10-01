import re


def extract_evidence(source_text, source_title):
    """
    Extract potentially useful evidence from a webpage.
    """

    sentences = re.split(r'(?<=[.!?])\s+', source_text)

    evidence = []

    keywords = [
        "revenue",
        "sales",
        "market",
        "growth",
        "profit",
        "price",
        "vehicles",
        "electric",
        "battery",
        "company",
        "customers",
        "production"
    ]

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) < 40:
            continue

        sentence_lower = sentence.lower()

        if any(keyword in sentence_lower for keyword in keywords):

            evidence.append({
                "source": source_title,
                "claim": sentence[:500]
            })

        if len(evidence) >= 10:
            break

    return evidence