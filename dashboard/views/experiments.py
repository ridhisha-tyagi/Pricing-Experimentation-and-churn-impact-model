import streamlit as st
from utils.load_data import load_experiment_simulation
import streamlit.components.v1 as components


# -----------------------------
# 🧪 Experiment decision card
# -----------------------------
def experiment_card(row):

    if row["recommended_action"] == "Proceed to Live Test":
        bg = "#e7f3ec"
        border = "#2e7d32"
    elif row["recommended_action"] == "Limit / Monitor":
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
        border-radius:18px;
        margin-bottom:18px;
        font-family: Inter, sans-serif;
        color:#1f1f1f;
    ">
        <h3 style="margin-bottom:8px;">{row['segment_key']}</h3>

        <p><b>Decision:</b> {row['recommended_action']}</p>
        <p><b>Guardrail:</b> {row['guardrail_status']}</p>
        <p><b>Net Effect:</b> {row['net_effect_label']}</p>
    </div>
    """
    components.html(html, height=210)


# -----------------------------
# 🔹 Main render
# -----------------------------
def render():

    # -----------------------------
    # 🔙 Back to Home
    # -----------------------------
    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    # -----------------------------
    # 🔮 CENTERED TITLE
    # -----------------------------
    components.html("""
    <div style="
        text-align:center;
        font-size:44px;
        font-weight:900;
        margin:24px 0 36px 0;
        color:white;
    ">
        🧪 Pricing Experimentation
    </div>
    """, height=90)

    # -----------------------------
    # 📘 HOW TO READ (MATCHES MODEL)
    # -----------------------------
    components.html("""
    <div style="
        background:#f7f5ef;
        padding:34px;
        border-radius:22px;
        border-left:8px solid #b08968;
        font-size:18px;
        line-height:1.75;
        color:#1f1f1f;
        max-width:1100px;
        margin:0 auto 40px auto;
    ">

        <div style="font-size:22px; font-weight:800; margin-bottom:18px;">
            How to read this experimentation layer
        </div>

        <p>
            This page operationalizes insights from the
            <b>Pricing → Churn Impact Model</b>.
        </p>

        <p>
            Each card represents a <b>micro-experiment</b> scoped to a
            specific pricing segment.
        </p>

        <ul>
            <li><b>Baseline metrics</b> reflect current behavior</li>
            <li><b>Expected metrics</b> simulate expansion impact</li>
            <li><b>Guardrails</b> ensure churn risk stays controlled</li>
        </ul>

        <p style="margin-top:18px;"><b>Use this page to:</b></p>

        <ul>
            <li>🧪 design safe pricing experiments</li>
            <li>🚫 avoid high-risk rollout ideas</li>
            <li>📈 identify segments ready for expansion</li>
        </ul>

    </div>
    """, height=520)

    # -----------------------------
    # 📊 Load experiment data
    # -----------------------------
    exp_df = load_experiment_simulation()

    if exp_df.empty:
        st.warning("No experiment simulation data found.")
        return

    # -----------------------------
    # 🔍 Render experiments
    # -----------------------------
    for _, row in exp_df.iterrows():

        # Decision summary card
        experiment_card(row)

        # Expandable details
        with st.expander(f"🔍 View details — {row['segment_key']}"):

            c1, c2 = st.columns(2)

            with c1:
                st.markdown("### Baseline Metrics")
                st.metric("Subscribers", int(row["subs"]))
                st.metric("Churn Rate (%)", round(row["baseline_churn_rate"], 2))
                st.metric("Upgrade Rate (%)", round(row["baseline_upgrade_rate"], 2))
                st.metric("Downgrade Rate (%)", round(row["baseline_downgrade_rate"], 2))

            with c2:
                st.markdown("### Expected Impact")
                st.metric("Expected Churn (%)", round(row["expected_churn_rate"], 2))
                st.metric("Expected Upgrade (%)", round(row["expected_upgrade_rate"], 2))
                st.metric("Expected Downgrade (%)", round(row["expected_downgrade_rate"], 2))

            st.markdown(
                """
                **Interpretation**  
                This micro-experiment isolates a single pricing segment
                to evaluate expansion impact while respecting
                churn guardrails.
                """
            )
