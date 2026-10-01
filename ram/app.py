import streamlit as st
from workflow import run_research


# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="ResearchOS",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==============================
# CUSTOM CSS
# ==============================

st.markdown(
    """
    <style>

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #9ca3af;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 650;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .agent-card {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        background: rgba(128, 128, 128, 0.06);
        text-align: center;
        min-height: 100px;
    }

    .agent-name {
        font-weight: 600;
        margin-top: 8px;
    }

    .agent-status {
        color: #22c55e;
        font-size: 13px;
        margin-top: 5px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==============================
# SIDEBAR
# ==============================

with st.sidebar:

    st.title("🔎 ResearchOS")

    st.caption(
        "AI Business Research & "
        "Competitive Intelligence"
    )

    st.divider()

    st.subheader("Agent Pipeline")

    st.write("🧠 Research Planner")
    st.write("🔎 Source Discovery")
    st.write("📄 Source Extraction")
    st.write("📊 Evidence Analysis")
    st.write("⚠️ Contradiction Detection")
    st.write("🧩 Synthesis")
    st.write("📋 Executive Report")

    st.divider()

    st.caption("Hackathon Prototype")


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="main-title">🔎 ResearchOS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered business research and competitive intelligence'
    '</div>',
    unsafe_allow_html=True
)


# ==============================
# AGENT PIPELINE
# ==============================

agents = [
    ("🧠", "Research Planner"),
    ("🔎", "Source Discovery"),
    ("📄", "Extraction"),
    ("📊", "Evidence"),
    ("⚠️", "Verification"),
    ("🧩", "Synthesis"),
    ("📋", "Executive Report")
]

cols = st.columns(len(agents))

for col, (icon, name) in zip(cols, agents):

    with col:

        st.markdown(
            f'<div class="agent-card">'
            f'<div style="font-size:28px;">{icon}</div>'
            f'<div class="agent-name">{name}</div>'
            f'<div class="agent-status">● Ready</div>'
            f'</div>',
            unsafe_allow_html=True
        )


st.divider()


# ==============================
# RESEARCH INPUT
# ==============================

st.markdown(
    '<div class="section-title">'
    'Business Research Question'
    '</div>',
    unsafe_allow_html=True
)

question = st.text_area(
    "Research Question",
    placeholder=(
        "Example: How is Tesla performing "
        "compared with other electric vehicle companies?"
    ),
    height=130,
    label_visibility="collapsed"
)


start = st.button(
    "🚀  Start Research",
    use_container_width=True,
    type="primary"
)


# ==============================
# RUN RESEARCH
# ==============================

if start:

    if not question.strip():

        st.warning(
            "Please enter a business research question."
        )

    else:

        with st.spinner(
            "ResearchOS is researching and analyzing..."
        ):

            try:

                report = run_research(question)

                st.success(
                    "Research completed successfully!"
                )

                st.divider()


                # ==============================
                # METRICS
                # ==============================

                st.markdown(
                    '<div class="section-title">'
                    'Research Overview'
                    '</div>',
                    unsafe_allow_html=True
                )

                evidence_count = len(
                    report["verified_facts"]
                )

                conflict_count = len(
                    report["conflicting_information"]
                )

                unknown_count = len(
                    report["unknown_information"]
                )

                source_count = len(
                    report["sources"]
                )


                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "🔗 Sources",
                    source_count
                )

                col2.metric(
                    "📚 Evidence",
                    evidence_count
                )

                col3.metric(
                    "⚠️ Potential Conflicts",
                    conflict_count
                )

                col4.metric(
                    "❓ Unknown",
                    unknown_count
                )


                # ==============================
                # EXECUTIVE SUMMARY
                # ==============================

                st.markdown(
                    '<div class="section-title">'
                    '📋 Executive Summary'
                    '</div>',
                    unsafe_allow_html=True
                )

                for finding in report[
                    "executive_summary"
                ]:

                    st.write(
                        "•",
                        finding
                    )


                # ==============================
                # AI ANALYSIS
                # ==============================

                st.markdown(
                    '<div class="section-title">'
                    '🤖 AI Analysis'
                    '</div>',
                    unsafe_allow_html=True
                )

                ai_analysis = report.get(
                    "ai_analysis"
                )

                if ai_analysis:

                    st.markdown(
                        ai_analysis
                    )

                else:

                    st.info(
                        "AI reasoning is currently disabled. "
                        "The research pipeline is operating "
                        "using source discovery and evidence analysis."
                    )


                # ==============================
                # EVIDENCE
                # ==============================

                st.markdown(
                    '<div class="section-title">'
                    '📚 Evidence'
                    '</div>',
                    unsafe_allow_html=True
                )

                if evidence_count:

                    for index, item in enumerate(
                        report["verified_facts"],
                        start=1
                    ):

                        with st.expander(
                            f"Evidence {index}"
                        ):

                            st.write(
                                item.get(
                                    "claim",
                                    ""
                                )
                            )

                            st.caption(
                                "Source: "
                                + item.get(
                                    "source",
                                    "Unknown"
                                )
                            )

                else:

                    st.info(
                        "No evidence extracted."
                    )


                # ==============================
                # CONFLICTS
                # ==============================

                st.markdown(
                    '<div class="section-title">'
                    '⚠️ Potential Conflicts'
                    '</div>',
                    unsafe_allow_html=True
                )

                if conflict_count:

                    for conflict in report[
                        "conflicting_information"
                    ]:

                        st.warning(
                            f"Topic: "
                            f"{conflict['topic']}"
                        )

                        st.write(
                            "Sources: "
                            + ", ".join(
                                conflict["sources"]
                            )
                        )

                        st.caption(
                            "Status: "
                            + conflict["status"]
                        )

                else:

                    st.success(
                        "No potential conflicts detected."
                    )


                # ==============================
                # INFERENCES
                # ==============================

                st.markdown(
                    '<div class="section-title">'
                    '💡 Inferences'
                    '</div>',
                    unsafe_allow_html=True
                )

                if report["inferences"]:

                    for item in report[
                        "inferences"
                    ]:

                        st.write(
                            "•",
                            item
                        )

                else:

                    st.info(
                        "No inferences generated yet."
                    )


                # ==============================
                # UNKNOWN
                # ==============================

                st.markdown(
                    '<div class="section-title">'
                    '❓ Unknown Information'
                    '</div>',
                    unsafe_allow_html=True
                )

                for item in report[
                    "unknown_information"
                ]:

                    st.write(
                        "•",
                        item
                    )


                # ==============================
                # SOURCES
                # ==============================

                st.markdown(
                    '<div class="section-title">'
                    '🔗 Sources'
                    '</div>',
                    unsafe_allow_html=True
                )

                for source in report[
                    "sources"
                ]:

                    with st.expander(
                        source["title"]
                    ):

                        st.write(
                            source["url"]
                        )

                        st.write(
                            source["text"][:1000]
                        )


            except Exception as error:

                st.error(
                    f"Something went wrong: {error}"
                )