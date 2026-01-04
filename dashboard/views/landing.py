import streamlit as st

def render():

    st.markdown('<div class="main-title">Pricing System Intelligence</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="subtitle">Decision-first analysis of pricing, churn, and expansion</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="helper">Read this like a decision tree. Start broad, then drill into pricing behavior.</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])

    with col2:
        if st.button("📊 Explore Pricing System"):
            st.session_state.page = "pricing"

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🧪 View Experiments"):
            st.session_state.page = "experiments"

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🧠 Churn Impact Model"):
            st.session_state.page = "model"
