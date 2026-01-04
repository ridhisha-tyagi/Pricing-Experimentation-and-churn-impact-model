import streamlit as st
from visuals.themes import apply_theme
from views import home, pricing_system, experiments, churn_model

st.set_page_config(
    page_title="Pricing System Intelligence",
    layout="wide"
)

apply_theme()

# -----------------------------
# Session-based routing
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

page = st.session_state.page


if page == "home":
    home.render()
elif page == "pricing":
    pricing_system.render()
elif page == "experiments":
    experiments.render()
elif page == "churn":
    churn_model.render()


