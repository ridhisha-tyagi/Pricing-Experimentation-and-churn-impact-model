import streamlit as st
from utils.load_data import load_trial, load_billing, load_plan_seat


import streamlit.components.v1 as components

def decision_card(
    title,
    subs,
    churn,
    upgrade,
    age,
    confidence,
    performance,
    guardrail,
    action,
):
    if "High Stability" in performance:
        bg = "#e7f3ec"
        border = "#2e7d32"
    elif "Neutral" in performance:
        bg = "#f5efe6"
        border = "#b08968"
    else:
        bg = "#f7d7db"
        border = "#b23a48"

    html = f"""
    <div style="
        background:{bg};
        border-left:6px solid {border};
        padding:22px;
        border-radius:16px;
        font-family: Inter, sans-serif;
        color:#1f1f1f;
    ">
        <h2>{title}</h2>
        <p><b>Confidence:</b> {confidence} ({subs:,} subs)</p>

        <p>📉 <b>Avg Churn:</b> {churn:.2f}%</p>
        <p>📈 <b>Avg Upgrade:</b> {upgrade:.2f}%</p>
        <p>⏳ <b>Median Subscription Age:</b> {age} days</p>

        <hr style="margin:12px 0;">

        <p><b>Guardrail:</b> {guardrail}</p>
        <p><b>Action:</b> {action}</p>
    </div>
    """

    components.html(html, height=330)

#
# -----------------------------
# 🔹 Main render
# -----------------------------
def render():

    # -----------------------------
    # 🔙 Back to Home (ONLY THIS)
    # -----------------------------
    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown('<div class="main-title">Pricing System</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="helper">Click a branch to explore pricing impact.</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    if "branch" not in st.session_state:
        st.session_state.branch = None

    with col1:
        if st.button("Trial vs Non-Trial"):
            st.session_state.branch = "trial"

    with col2:
        if st.button("Billing Frequency"):
            st.session_state.branch = "billing"

    with col3:
        if st.button("Plan Structure"):
            st.session_state.branch = "plan"

    st.markdown("---")

    # =============================
    # TRIAL vs NON-TRIAL
    # =============================
    if st.session_state.branch == "trial":

        st.subheader("Trial vs Non-Trial")
        st.markdown(
            "**How to read:** Entry strategy comparison. "
            "Trial users reflect onboarding quality and early intent. "
            "Non-trial users reflect direct purchase confidence."
        )

        trial_df = load_trial()
        c1, c2 = st.columns(2)

        with c1:
            row = trial_df[trial_df["trial_group"] == "Trial"].iloc[0]
            decision_card(
                title="🧪 Trial Users",
                subs=row["subs"],
                churn=row["avg_churn_rate"],
                upgrade=row["avg_upgrade_rate"],
                age=row["median_subscription_age"],
                confidence=row["confidence_level"],
                performance=row["performance_label"],
                guardrail=row["guardrail_status"],
                action=row["recommended_action"],
            )

        with c2:
            row = trial_df[trial_df["trial_group"] == "Non-Trial"].iloc[0]
            decision_card(
                title="🚀 Direct Purchase",
                subs=row["subs"],
                churn=row["avg_churn_rate"],
                upgrade=row["avg_upgrade_rate"],
                age=row["median_subscription_age"],
                confidence=row["confidence_level"],
                performance=row["performance_label"],
                guardrail=row["guardrail_status"],
                action=row["recommended_action"],
            )

    # =============================
    # BILLING FREQUENCY
    # =============================
    elif st.session_state.branch == "billing":

        st.subheader("Billing Frequency")
        st.markdown(
            "**How to read:** Commitment depth comparison. "
            "Annual billing signals long-term value alignment. "
            "Monthly billing reflects flexibility and ongoing evaluation."
        )

        billing_df = load_billing()
        c1, c2 = st.columns(2)

        with c1:
            row = billing_df[billing_df["billing_group"] == "Annual"].iloc[0]
            decision_card(
                title="🗓 Annual Billing",
                subs=row["subs"],
                churn=row["avg_churn_rate"],
                upgrade=row["avg_upgrade_rate"],
                age=row["median_subscription_age"],
                confidence=row["confidence_level"],
                performance=row["performance_label"],
                guardrail=row["guardrail_status"],
                action=row["recommended_action"],
            )

        with c2:
            row = billing_df[billing_df["billing_group"] == "Monthly"].iloc[0]
            decision_card(
                title="📆 Monthly Billing",
                subs=row["subs"],
                churn=row["avg_churn_rate"],
                upgrade=row["avg_upgrade_rate"],
                age=row["median_subscription_age"],
                confidence=row["confidence_level"],
                performance=row["performance_label"],
                guardrail=row["guardrail_status"],
                action=row["recommended_action"],
            )

    # =============================
    # PLAN × SEAT  ✅ FIXED
    # =============================
    elif st.session_state.branch == "plan":

        st.subheader("Plan × Seat Structure")
        st.markdown(
            "**How to read:** Performance of pricing plans across customer sizes. "
            "Each card reflects value alignment at scale."
        )

        plan_df = load_plan_seat()

        selected_plan = st.selectbox(
            "Select plan",
            options=sorted(plan_df["plan_group"].unique())
        )

        filtered = plan_df[plan_df["plan_group"] == selected_plan]

        st.markdown("---")

        for _, row in filtered.iterrows():
            decision_card(
                title=f"{selected_plan} · {row['seat_bucket']} seats",
                subs=row["subs"],
                churn=row["avg_churn_rate"],
                upgrade=row["avg_upgrade_rate"],
                age=row["median_subscription_age"],
                confidence=row["confidence_level"],
                performance=row["performance_label"],
                guardrail=row["guardrail_status"],
                action=row["recommended_action"],
            )



