import streamlit as st

def inject_styles():
    st.markdown("""
    <style>
        body {
            background-color: #6f7f5f;
        }

        .main-title {
            font-size: 52px;
            font-weight: 800;
            text-align: center;
            color: #ffffff;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #f3f3f3;
            margin-bottom: 30px;
        }

        .nav-button button {
            background-color: #f6c1d1;
            color: #2b2b2b;
            border-radius: 14px;
            padding: 14px 26px;
            font-size: 16px;
            font-weight: 600;
            border: none;
        }

        .helper {
            text-align: center;
            font-size: 14px;
            color: #eaeaea;
            margin-bottom: 40px;
        }
    </style>
    """, unsafe_allow_html=True)
