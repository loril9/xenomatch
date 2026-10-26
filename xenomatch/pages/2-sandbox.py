import streamlit as st

st.set_page_config(
    page_title="XenoMatch | Simulator",
    layout="wide",
    page_icon="⚙️"
)

st.markdown("<h2 style='color:#00D4B2; margin-bottom:0;'>⚙️ Dynamic Telemetry Simulator Grid</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#9CA3AF; font-family:JetBrains Mono; margin-top:0;'>Real-time Ischemia & Bioethical Allocation Modeling</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([1.3, 1.2])

with col1:
    st.markdown("<h4 style='color:#9CA3AF; font-family:JetBrains Mono;'>PHASE 1: CLINICAL DATA INPUTS</h4>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<b style='color:#FFF;'>1. Ischemic Stress Parameters</b>", unsafe_allow_html=True)
        cit = st.slider("Cold Ischemia Time (CIT) in Hours", min_value=0, max_value=12, value=4, help="Duration organ is preserved without active blood circulation.")
        modality = st.selectbox("Preservation Environment Modality", ["Static Cold Storage (SCS)", "Hypothermic Machine Perfusion (HMP)"])

    st.write("")
    with st.container(border=True):
        st.markdown("<b style='color:#FFF;'>2. Immunological Rejection Barriers</b>", unsafe_allow_html=True)
        antibodies = st.selectbox("Pre-Existing Recipient Anti-Pig Antibody Titers", ["Low Titer Cross-Match", "Medium Titer Cross-Match", "High Titer Cross-Match"])
        genetics = st.radio("Porcine Donor Genomic Engineering Profile", ["Standard Triple-Knockout (TKO)", "Advanced Transgenic (TKO + hCD46/hCD55/hCD59)"])

    st.write("")
    with st.container(border=True):
        st.markdown("<b style='color:#FFF;'>3. Prophylactic Targeted Regimen</b>", unsafe_allow_html=True)
        eculizumab = st.checkbox("Administer Eculizumab (Targeted C5 Complement Inhibitor)")

# Computational Engine Calculation
iri_score = 10
if cit <= 4:
    iri_score += (cit * 5)
else:
    iri_score += (4 * 5) + ((cit - 4) * 10)

if modality == "Static Cold Storage (SCS)":
    iri_score += 15

if antibodies == "Medium Titer Cross-Match":
    iri_score += 15
elif antibodies == "High Titer Cross-Match":
    iri_score += 30

if genetics == "Advanced Transgenic (TKO + hCD46/hCD55/hCD59)":
    iri_score -= 20
if eculizumab:
    iri_score -= 15

iri_score = max(0, min(100, iri_score))

with col2:
    st.markdown("<h4 style='color:#9CA3AF; font-family:JetBrains Mono;'>PHASE 2: REAL-TIME SIMULATION TELEMETRY</h4>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<span style='font-size:0.9rem; color:#9CA3AF; font-family:JetBrains Mono;'>COMPUTED INDEX</span>", unsafe_allow_html=True)
        
        # Color coding status telemetry engine
        if iri_score >= 70:
            status_color = "#EF4444"
            status_text = "CRITICAL RISK PROFILE: High probability of acute microvascular damage and hyper-acute graft failure."
            badge = "❌ HIGH RISK"
        elif 40 <= iri_score < 70:
            status_color = "#F59E0B"
            status_text = "MODERATE RISK PROFILE: Reperfusion trauma expected. Requires hyper-vigilant post-operative management."
            badge = "⚠️ MODERATE RISK"
        else:
            status_color = "#10B981"
            status_text = "OPTIMAL RISK PROFILE: Minimal ischemic cellular damage calculated. Favorable graft prognosis."
            badge = "✅ OPTIMAL"

        st.markdown(f"<h1 style='color:{status_color}; font-size:4rem; margin:0; font-family:JetBrains Mono;'>{iri_score}%</h1>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#1F2937; padding:12px; border-left:4px solid {status_color}; border-radius:4px; font-size:0.9rem;'><b>{badge}</b> — {status_text}</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("<h4 style='color:#9CA3AF; font-family:JetBrains Mono;'>PHASE 3: BIOETHICAL ALLOCATION TRIAGE</h4>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f"**Case Evaluation:** The assigned transplant candidate presents a calculated **{iri_score}%** IRI risk index.")
        st.markdown("🔴 **Patient Status:** Critical condition. Facing imminent systemic failure; survival estimated under 48 hours on alternative therapies.")
        st.markdown("🟢 **Alternative Option:** A secondary candidate listed on the regional registry matches an optimal, low-risk immunoprofile but remains medically stable for up to 12 months.")
        st.write("---")
        st.markdown("💬 *As the presiding Institutional Review Board, allocate the organ:*")
        
        b1, b2 = st.columns(2)
        with b1:
            allocate = st.button("⚖️ Prioritize Urgent Justice", use_container_width=True, help="Egalitarian Framework: Allocate to the critical patient despite high calculated risk.")
        with b2:
            hold = st.button("📊 Prioritize Long-Term Utility", use_container_width=True, help="Utilitarian Framework: Reserve for the stable patient to maximize clinical asset life.")

        if allocate:
            st.toast("Egalitarian framework logged successfully.", icon="⚖️")
            st.info("**Moral Framework Logged: Egalitarian Model (Medical Urgency)**\n\nBy allocating to the critical patient, you prioritized immediate human survival. However, you accepted a steep statistical risk of graft loss due to severe baseline tissue trauma.")
        if hold:
            st.toast("Utilitarian framework logged successfully.", icon="📊")
            st.success("**Moral Framework Logged: Utilitarian Model (Resource Optimization)**\n\nBy routing the organ to the stable candidate, you maximized resource utility and longevity metrics. However, the high-urgency candidate has been bypassed due to clinical risk thresholds.")
