import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_evidence(question, evidence):
    """
    Analyze collected evidence using an LLM.
    """

    evidence_text = "\n\n".join(
        [
            f"Source: {item.get('source', 'Unknown')}\n"
            f"Claim: {item.get('claim', '')}"
            for item in evidence
        ]
    )

    prompt = f"""
You are an AI Business Research Analyst.

Business research question:
{question}

Evidence collected from external sources:
{evidence_text}

Analyze the evidence carefully.

Return the analysis using exactly these sections:

VERIFIED FACTS:
- Facts directly supported by the evidence.

CONFLICTING INFORMATION:
- Claims where sources disagree or information is inconsistent.

INFERENCES:
- Reasonable conclusions based on the available evidence.
- Clearly mark these as inferences.

UNKNOWN INFORMATION:
- Important information that cannot be established from the evidence.

KEY FINDINGS:
- The most important findings for a business decision.

IMPORTANT:
Do not invent facts.
Do not treat assumptions as facts.
If evidence is insufficient, say so.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text