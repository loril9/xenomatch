import streamlit as st

st.set_page_config(page_title="XenoMatch | Ethics", layout="wide")

if 'strategic_decision_log' not in st.session_state:
    st.session_state.strategic_decision_log = []

st.markdown("""
    <style>
        @import url('https://googleapis.com');
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"], .stMarkdown, p, span, div {
            background-color: #F8FAFC !important;
            font-family: 'Inter', sans-serif !important;
            color: #0F172A !important;
        }
        [data-testid="stHeaderActionElements"], div[data-testid="StyledLinkIconContainer"], h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
            display: none !important;
            pointer-events: none !important;
        }
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            padding: 32px !important;
        }
        .stMetric [data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace !important;
            font-weight: 500 !important;
            color: #0F172A !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div style='font-size:1.8rem; font-weight:700; color:#0F172A; letter-spacing:-0.75px;'>Ethical Dilemma Registries</div>", unsafe_allow_html=True)
st.markdown("<div style='font-size:1rem; color:#64748B; margin-bottom:24px;'>Case Scenario Assessment Framework</div>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin-bottom: 24px;'>", unsafe_allow_html=True)

st.selectbox("Active Registry File Target", ["Log Profile 4901: Medical Crossmatch Override Parameters"])

col_case_left, col_case_right = st.columns([1, 1.2], gap="large")
with col_case_left:
    with st.container(border=True):
        st.markdown("<h4 style='color:#DC2626; margin-top:0; font-weight:600;'>Patient Parameters: Candidate Alpha</h4>", unsafe_allow_html=True)
        st.markdown(
            "<ul style='line-height:1.8; color:#0F172A; padding-left:20px;'>"
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
st.markdown("<h3 style='color:#0EA5E9; margin-bottom:16px; font-weight:600; font-size:1.25rem;'>Aggregated Institutional Choice Vectors</h3>", unsafe_allow_html=True)

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
