import streamlit as st

def apply_theme():
    st.markdown(
        """
        <style>
        /* Import premium font */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500&display=swap');

        /* Page background */
        .stApp {
            background-color: #6B7B5A;
        }

        /* Main title */
        .main-title {
            font-family: 'Playfair Display', serif;
            font-size: 56px;
            font-weight: 700;
            color: #FFFFFF;
            text-align: center;
            margin-bottom: 10px;
        }

        /* Subtitle */
        .subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            color: #F2F2F2;
            text-align: center;
            max-width: 720px;
            margin: 0 auto;
            line-height: 1.6;
        }

        /* Helper / how-to text */
        .helper {
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            color: #E6E6E6;
            text-align: center;
            max-width: 680px;
            margin: 18px auto 40px auto;
            line-height: 1.6;
        }

        /* Button container */
        .button-row {
            display: flex;
            justify-content: center;
            gap: 24px;
            margin-top: 30px;
        }

        /* Buttons */
        div.stButton > button {
            background-color: #F4C2D7;
            color: #3A3A3A;
            border-radius: 14px;
            padding: 16px 26px;
            font-size: 16px;
            font-weight: 600;
            border: none;
            min-width: 220px;
        }

        div.stButton > button:hover {
            background-color: #F7A8C7;
            transform: translateY(-1px);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
