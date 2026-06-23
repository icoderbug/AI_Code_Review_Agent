import os
import sqlite3
import streamlit as st
import pandas as pd
import plotly.express as px

from agents.code_review_agent import review_code
from agents.risk_agent import calculate_risk_score
from agents.quality_agent import calculate_quality_score
from agents.optimization_agent import get_optimization_suggestions
from agents.language_agent import detect_language



from database import (
    initialize_database,
    save_review,
    fetch_reviews
)

from pdf_generator import generate_pdf

from ui_components import (
    apply_custom_theme,
    render_sidebar,
    render_header
)


# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="AI Code Review Agent",
    page_icon="🤖",
    layout="wide"
)

apply_custom_theme()
render_sidebar()
render_header()

initialize_database()


# ----------------------------
# HEADER
# ----------------------------

st.title("🤖 AI Code Review Agent")
st.markdown(
    """
Upload a Python file and receive:

 AI Review  
 Risk Score  
 Quality Score  
 Optimization Suggestions  
 PDF Report  
 Review History
"""
)

# ----------------------------
# FILE UPLOAD
# ----------------------------

uploaded_file = st.file_uploader(
    "Upload Source Code",
    type=["py", "java", "cpp", "c", "js", "rb"]
)

if uploaded_file:

    code = uploaded_file.read().decode("utf-8")
    detected_language = detect_language(
        uploaded_file.name
    )

    st.subheader("Uploaded Code")

    st.code(
        code,
        language=uploaded_file.name.split(".")[-1].lower()
    )

    if st.button("Review Code"):

        with st.spinner("Analyzing Code..."):

            # ----------------------------
            # AGENT 1
            # CODE REVIEW AGENT
            # ----------------------------

            review_result = review_code(
                code,
                detected_language
            )

            # ----------------------------
            # AGENT 2
            # RISK AGENT
            # ----------------------------

            risk_score = calculate_risk_score(
                review_result
            )

            # ----------------------------
            # AGENT 3
            # QUALITY AGENT
            # ----------------------------

            quality_score = calculate_quality_score(
                review_result
            )

            # ----------------------------
            # AGENT 4
            # OPTIMIZATION AGENT
            # ----------------------------

            suggestions = get_optimization_suggestions(
                code
            )

        # ----------------------------
        # DASHBOARD
        # ----------------------------

        st.subheader("📊 Scores")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Risk Score",
                f"{risk_score}/100"
            )

        with col2:
            st.metric(
                "Quality Score",
                f"{quality_score}/100"
            )

        # ----------------------------
        # CHART
        # ----------------------------

        chart_df = pd.DataFrame({
            "Metric": ["Risk Score", "Quality Score"],
            "Score": [risk_score, quality_score]
            })
        fig = px.area(
        chart_df,
        x="Metric",
        y="Score",
        title="Code Analysis Scores")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ----------------------------
        # REVIEW
        # ----------------------------

        st.subheader("📝 AI Review")

        st.write(review_result)

        # ----------------------------
        # OPTIMIZATION
        # ----------------------------

        st.subheader("⚡ Optimization Suggestions")

        st.write(suggestions)

        # ----------------------------
        # SAVE TO SQLITE
        # ----------------------------

        save_review(
            filename=uploaded_file.name,
            risk_score=risk_score,
            quality_score=quality_score,
            review=review_result
        )

        # ----------------------------
        # PDF REPORT
        # ----------------------------

        pdf_path = generate_pdf(
            uploaded_file.name,
            risk_score,
            quality_score,
            review_result,
            suggestions
        )

        with open(pdf_path, "rb") as file:

            st.download_button(
                label="📥 Download PDF Report",
                data=file,
                file_name="AI_Code_Review_Report.pdf",
                mime="application/pdf"
            )

# ----------------------------
# REVIEW HISTORY
# ----------------------------

st.markdown("---")

st.subheader("📚 Review History")

history = fetch_reviews()

if len(history) > 0:

    df = pd.DataFrame(
        history,
        columns=[
            "ID",
            "File",
            "Risk",
            "Quality",
            "Review"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info("No reviews available yet.")

st.markdown("---")
st.caption(
    "Developed by Prateek Singh | AI Code Review Agent"
)