import streamlit as st

st.set_page_config(page_title="XenoMatch | Ethics Module", layout="wide")

if 'strategic_decision_log' not in st.session_state:
    st.session_state.strategic_decision_log = []

st.markdown("""
    <style>
        html, body, [data-testid="stMainView"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, div {
            font-family: 'Inter', sans-serif !important;
        }
        .stApp { background-color: #0B0F19; color: #E2E8F0; }
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #131C2E !important;
            border: 1px solid #1E293B !important;
            border-radius: 6px !important;
            padding: 30px !important;
        }
        .stMetric [data-testid="stMetricValue"] { font-family: 'JetBrains Mono', monospace !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#00D4B2; margin-bottom:0; font-weight:700; letter-spacing:-1px;'>Ethical Dilemma Registries</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#94A3B8; margin-top:5px;'>Case Scenario Assessment & Matrix Tracking</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

selected_case_profile = st.selectbox("Registry Case Logs File Select", [
    "Log Profile 4901: Medical Crossmatch Override Parameters"
])

case_layout_left, case_layout_right = st.columns([1, 1.2])
with case_layout_left:
    with st.container(border=True):
        st.markdown("<h4 style='color:#EF4444; margin-top:0; font-weight:600;'>Patient Parameters: Candidate Alpha</h4>", unsafe_allow_html=True)
        st.markdown(
            "<ul>"
            "<li><b>Age Demographics:</b> 34</li>"
            "<li><b>Clinical State:</b> End-Stage Organ Degradation</li>"
            "<li><b>Immunological Profile:</b> Highly sensitized reactivity</li>"
            "<li><b>Computed Structural Injury Risk:</b> 75%</li>"
            "</ul>", unsafe_allow_html=True
        )
with case_layout_right:
    with st.container(border=True):
        st.markdown("<h4 style='color:#FFF; margin-top:0; font-weight:600;'>Allocation Paradox</h4>", unsafe_allow_html=True)
        st.write(
            "The candidate presents with highly sensitized profiles. The tissue has been held for 11 hours under cold ischemia conditions, "
            "making significant tissue injury mathematically verified. Allocation to this candidate attempts immediate preservation of life "
            "but assumes an elevated risk of functional asset failure within a narrow post-operative window."
        )
        
        st.write("")
        execution_left_btn, execution_right_btn = st.columns(2)
        with execution_left_btn:
            if st.button("Route Asset to Alpha", use_container_width=True):
                st.session_state.strategic_decision_log.append("Urgency")
        with execution_right_btn:
            if st.button("Retain Asset for Optimization", use_container_width=True):
                st.session_state.strategic_decision_log.append("Longevity")

st.write("")
st.markdown("<h3 style='color:#00D4B2; margin-bottom:15px; font-weight:600; font-size:1.3rem;'>Aggregated Institutional Choice Vectors</h3>", unsafe_allow_html=True)

with st.container(border=True):
    if st.session_state.strategic_decision_log:
        urgency_metric_count = st.session_state.strategic_decision_log.count("Urgency")
        longevity_metric_count = st.session_state.strategic_decision_log.count("Longevity")
        
        metric_col_left, metric_col_right = st.columns(2)
        with metric_col_left:
            st.metric("Urgency Profile Selection Metrics", f"{urgency_metric_count}", delta="Egalitarian Vector Weights")
        with metric_col_right:
            st.metric("Utility Profile Selection Metrics", f"{longevity_metric_count}", delta="Utilitarian Vector Weights")
    else:
        st.info("Registry empty. Evaluate the scenario above to initialize decision metrics processing loops.")
