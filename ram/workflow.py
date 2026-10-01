import os

from agents.research_planner import create_research_plan
from agents.source_discovery import search_web
from agents.source_extraction import extract_source
from agents.evidence_extraction import extract_evidence
from agents.contradiction import detect_contradictions
from agents.synthesis import create_synthesis
from agents.executive_report import create_executive_report


# AI analysis is disabled by default
USE_AI_ANALYSIS = os.getenv(
    "USE_AI_ANALYSIS",
    "false"
).lower() == "true"


def run_research(question):

    print("\n🧠 Creating research plan...")
    research_plan = create_research_plan(question)

    print("🔎 Discovering sources...")
    sources = search_web(question)

    print(f"📚 Found {len(sources)} sources.")

    extracted_sources = []
    all_evidence = []

    for source in sources:

        try:

            text = extract_source(
                source["url"]
            )

            extracted_sources.append({
                "title": source["title"],
                "url": source["url"],
                "text": text[:5000]
            })

            evidence = extract_evidence(
                text,
                source["title"]
            )

            all_evidence.extend(evidence)

        except Exception as error:

            print(
                f"⚠️ Could not process "
                f"{source['url']}: {error}"
            )

    print(
        f"📄 Extracted "
        f"{len(extracted_sources)} sources."
    )

    print(
        f"📊 Found "
        f"{len(all_evidence)} evidence items."
    )

    print(
        "⚠️ Checking for potential contradictions..."
    )

    potential_conflicts = detect_contradictions(
        all_evidence
    )

    print(
        f"⚠️ Potential conflicts found: "
        f"{len(potential_conflicts)}"
    )

    # --------------------------------
    # AI ANALYSIS
    # --------------------------------

    ai_analysis = None

    if USE_AI_ANALYSIS:

        try:

            from agents.ai_analysis import analyze_evidence

            print("🤖 Running AI analysis...")

            ai_analysis = analyze_evidence(
                question,
                all_evidence
            )

            print("✅ AI analysis completed.")

        except Exception as error:

            print(
                f"⚠️ AI analysis unavailable: {error}"
            )

            ai_analysis = None

    else:

        print(
            "ℹ️ AI analysis disabled."
        )

    # --------------------------------
    # RESEARCH DATA
    # --------------------------------

    research_data = {

        "research_plan": research_plan,

        "sources": extracted_sources,

        "verified_facts": all_evidence,

        "conflicting_information":
            potential_conflicts,

        "inferences": [],

        "unknown_information": [
            "AI-based verification is not enabled."
        ],

        "key_findings": [

            f"Research question: {question}",

            f"Sources analyzed: "
            f"{len(extracted_sources)}",

            f"Evidence items extracted: "
            f"{len(all_evidence)}",

            f"Potential conflicts: "
            f"{len(potential_conflicts)}"
        ],

        "ai_analysis": ai_analysis
    }

    # --------------------------------
    # SYNTHESIS
    # --------------------------------

    print("🧠 Creating synthesis...")

    synthesis = create_synthesis(
        research_data
    )

    # --------------------------------
    # EXECUTIVE REPORT
    # --------------------------------

    print("📋 Creating executive report...")

    report = create_executive_report(
        synthesis
    )

    # Keep AI analysis in final report
    report["ai_analysis"] = ai_analysis

    return report