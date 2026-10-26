import streamlit as st

st.set_page_config(page_title="XenoMatch | Case Registry", layout="wide")

if 'strategic_decision_log' not in st.session_state:
    st.session_state.strategic_decision_log = []

st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"] {
            background-color: #F8FAFC !important;
            color: #0F172A !important;
            font-family: 'Inter', sans-serif !important;
        }
        h1, h2, h3, h4, h5, h6, p, label, span, div { color: #0F172A !important; }
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            padding: 32px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#0EA5E9; margin-bottom:0; font-weight:700; letter-spacing:-0.5px;'>Ethical Dilemma Registries</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748B; margin-top:6px;'>Case Scenario Assessment Framework</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

st.selectbox("Active Registry File Target", ["Log Profile 4901: Medical Crossmatch Override Parameters"])

col_case_left, col_case_right = st.columns([1, 1.2])
with col_case_left:
    with st.container(border=True):
        st.markdown("<h4 style='color:#DC2626; margin-top:0; font-weight:600;'>Patient Parameters: Candidate Alpha</h4>", unsafe_allow_html=True)
        st.markdown(
            "<ul style='line-height:1.8; color:#0F172A;'>"
            "<li><b>Age Demographics:</b> 34 Years</li>"
            "<li><b>Clinical State:</b> End-Stage Organ Degradation</li>"
            "<li><b>Immunological Profile:</b> Highly sensitized reactivity matrix</li>"
            "<li><b>Computed Structural Injury Risk:</b> 75% Critical Threshold</li>"
            "</ul>", unsafe_allow_html=True
        )
with col_case_right:
    with st.container(border=True):
        st.markdown("<h4 style='color:#0F172A; margin-top:0; font-weight:600;'>Allocation Paradox</h4>", unsafe_allow_html=True)
        st.write(
            "The candidate presents with high sensitization. The organ profile tracker identifies an 11-hour cold ischemia duration, "
            "meaning significant baseline cell structural trauma is confirmed. Routing allocation to Alpha attempts to safeguard "
            "immediate survival but introduces a high statistical threat of early graft failure."
        )
        
        st.write("")
        btn_alpha, btn_beta = st.columns(2)
        with btn_alpha:
            if st.button("Route Asset to Alpha", use_container_width=True):
                st.session_state.strategic_decision_log.append("Urgency")
        with btn_beta:
            if st.button("Retain Asset for Optimization", use_container_width=True):
                st.session_state.strategic_decision_log.append("Longevity")

st.write("")
st.markdown("<h3 style='color:#0EA5E9; margin-bottom:15px; font-weight:600; font-size:1.3rem;'>Aggregated Institutional Choice Vectors</h3>", unsafe_allow_html=True)

with st.container(border=True):
    if st.session_state.strategic_decision_log:
        urg_c = st.session_state.strategic_decision_log.count("Urgency")
        lon_c = st.session_state.strategic_decision_log.count("Longevity")
        
        m_left, m_right = st.columns(2)
        with m_left:
            st.metric("Urgency Profile Selection Metrics", f"{urg_c}", delta="Egalitarian Weights")
        with m_right:
            st.metric("Utility Profile Selection Metrics", f"{lon_c}", delta="Utilitarian Weights")
    else:
        st.info("Registry clear. Execute allocation routing choices above to populate historical matrix coordinates.")
