import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


# -----------------------------
# 🔮 Pricing → Churn Impact Model
# -----------------------------
def render():


    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()
        
    # -----------------------------
    # 🎨 GLOBAL STYLES (SAFE)
    # -----------------------------
    st.markdown("""
    <style>
    .kpi-card {
        background:#ffffff;
        padding:28px;
        border-radius:22px;
        text-align:center;
        border:2px solid rgba(255,105,180,0.35);
        box-shadow:0 0 18px rgba(255,105,180,0.25);
        color:#1f1f1f;
    }

    .kpi-red {
        border-color:rgba(178,58,72,0.6);
        box-shadow:0 0 18px rgba(178,58,72,0.35);
    }

    .kpi-green {
        border-color:rgba(46,125,50,0.6);
        box-shadow:0 0 18px rgba(46,125,50,0.35);
    }

    .kpi-title {
        font-size:34px;
        font-weight:900;
    }

    .kpi-sub {
        font-size:15px;
        opacity:0.7;
        margin-top:8px;
    }

    .impact-card {
        background:#ffffff;
        padding:20px 24px;
        border-radius:18px;
        margin-bottom:14px;
        border-left:6px solid #ccc;
        color:#1f1f1f;
        font-size:16px;
    }
    </style>
    """, unsafe_allow_html=True)

    # -----------------------------
    # 🔮 CENTERED TITLE (FIXED)
    # -----------------------------
    components.html("""
    <div style="
        text-align:center;
        font-size:44px;
        font-weight:900;
        margin:24px 0 36px 0;
        color:white;
    ">
        🔮 Pricing → Churn Impact Model
    </div>
    """, height=90)

    # -----------------------------
    # 📘 HOW TO READ (NO MARKDOWN)
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
            How to read this model
        </div>

        <p><b>This is not a churn prediction model.</b></p>

        <p>
            It answers one question:
            <br>
            <b>“If we change pricing here, how much churn pressure do we add or remove?”</b>
        </p>

        <ul>
            <li><b>Positive %</b> → churn increases (risk)</li>
            <li><b>Negative %</b> → churn decreases (protective)</li>
            <li><b>Risk buckets</b> summarize severity so you don’t read coefficients</li>
        </ul>

        <p style="margin-top:18px;"><b>Use this page to:</b></p>

        <ul>
            <li>❌ block risky pricing ideas early</li>
            <li>✅ identify safe expansion zones</li>
            <li>🧪 design guardrail-aware experiments</li>
        </ul>

    </div>
    """, height=520)

    # -----------------------------
    # 📂 LOAD DATA
    # -----------------------------
    df = pd.read_csv("Data/processed/pricing_churn_impact.csv")
    df = df.sort_values("churn_delta_pct", ascending=False)

    top_risk = df.iloc[0]
    protective = df[df["risk_bucket"] == "Protective"]

    # -----------------------------
    # 🔢 KPI ROW
    # -----------------------------
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="kpi-card kpi-red">
            <div class="kpi-title">{top_risk['churn_delta_pct']}%</div>
            <div class="kpi-sub">Highest Churn Risk</div>
            <div style="margin-top:10px;">{top_risk['feature']}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi-card kpi-green">
            <div class="kpi-title">{len(protective)}</div>
            <div class="kpi-sub">Protective Pricing Signals</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">{len(df)}</div>
            <div class="kpi-sub">Pricing Factors Evaluated</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # -----------------------------
    # 📊 RISK BUCKETS
    # -----------------------------
    for bucket in ["High Risk", "Moderate Risk", "Neutral", "Protective"]:

        subset = df[df["risk_bucket"] == bucket]
        if subset.empty:
            continue

        if bucket == "High Risk":
            color = "#b23a48"
        elif bucket == "Moderate Risk":
            color = "#b08968"
        elif bucket == "Protective":
            color = "#2e7d32"
        else:
            color = "#6c757d"

        st.subheader(bucket)

        for _, row in subset.iterrows():
            st.markdown(f"""
            <div class="impact-card" style="border-left-color:{color};">
                <b>{row['feature']}</b><br>
                Churn impact: <b>{row['churn_delta_pct']}%</b>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # -----------------------------
    # 🧠 FINAL NOTE
    # -----------------------------
    st.markdown("""
    **What this means**

    This model does **not predict individual churn**.

    It quantifies **pricing-driven churn pressure** so teams can:
    - Kill bad ideas early  
    - Expand safely  
    - Design experiments with guardrails  

    This is a **strategy model**, not an ML.
    """)
