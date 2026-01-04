import streamlit as st

def render():

    st.markdown(
        '<div class="main-title">Pricing System Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
        Understand how pricing decisions shape churn, upgrades,
        and long-term customer stability.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="helper">
        Read this like a decision tree.
        Start broad, then drill down into behavioral splits to see
        where value breaks — and where it compounds.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Horizontal buttons using columns
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")

    with col1:
        if st.button("Explore Pricing System"):
            st.session_state.page = "pricing"

    with col2:
        if st.button("View Experiments"):
            st.session_state.page = "experiments"

    with col3:
        if st.button("Churn Impact Model"):
            st.session_state.page = "churn"
