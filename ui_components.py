import streamlit as st


def apply_custom_theme():
    st.markdown("""
    <style>

    /* Main App Background */
    .stApp {
        background-color: #F8F4E9;
    }

    /* Main Content Text */
    .stMarkdown,
    .stText,
    p,
    label,
    div,
    span,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: black !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #EFE7D7;
    }

    /* Buttons */
    .stButton > button {
        background-color: black !important;
        color: white !important;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        height: 3em;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #222222 !important;
        color: white !important;
    }

    /* Download Button */
    .stDownloadButton > button {
        background-color: black !important;
        color: white !important;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }

    /* File Uploader */
    [data-testid="stFileUploader"] {
        background-color: white;
        border-radius: 12px;
        padding: 10px;
        border: 1px solid #d3d3d3;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #dcdcdc;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
    }

    /* DataFrame */
    .stDataFrame {
        background-color: white;
        border-radius: 10px;
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        color: black !important;
        font-weight: bold;
    }

    /* Code Blocks */
    pre {
        border-radius: 10px !important;
    }

    </style>
    """, unsafe_allow_html=True)


def render_sidebar():

    with st.sidebar:

        st.title("🤖 AI Code Review Agent")

        st.markdown("---")

        st.markdown("""
        ### Features

        ✅ Multi-Language Support

        ✅ AI Code Review

        ✅ Risk Analysis

        ✅ Quality Analysis

        ✅ Optimization Suggestions

        ✅ PDF Report

        ✅ SQLite Review History
        """)

        st.markdown("---")

        st.markdown("""
        ### Architecture

        Upload File

        ↓

        Language Agent

        ↓

        Review Agent

        ↓

        Risk Agent

        ↓

        Quality Agent

        ↓

        Optimization Agent

        ↓

        SQLite + PDF
        """)


def render_header():

    st.markdown("""
    # 🤖 AI Code Review Agent

    ### Analyze code quality using AI-powered multi-agent review

    Upload Python, Java, C++, JavaScript, Ruby, or C files and receive professional code review reports instantly.
    """)