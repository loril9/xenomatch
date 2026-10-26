import streamlit as st

st.set_page_config(page_title="XenoMatch | Simulator", layout="wide")

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
        .stSlider [data-testid="stWidgetLabel"], .stSelectbox label, .stRadio label {
            color: #0F172A !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
        }
        .metric-value {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 4.5rem;
            font-weight: 700;
            line-height: 1;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div style='font-size:1.8rem; font-weight:700; color:#0F172A; letter-spacing:-0.75px;'>Telemetry Simulation Matrix</div>", unsafe_allow_html=True)
st.markdown("<div style='font-size:1rem; color:#64748B; margin-bottom:24px;'>Computational Multi-Variant Allocation Grid</div>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin-bottom: 24px;'>", unsafe_allow_html=True)

col_inputs, col_telemetry = st.columns([1.3, 1.2], gap="large")

with col_inputs:
    st.markdown("<h5 style='color:#64748B; font-weight:600; letter-spacing:0.5px; margin-bottom:16px;'>CLINICAL MODEL VALUES</h5>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<div style='color:#0F172A; font-weight:600; margin-bottom:16px; font-size:1.1rem;'>Organ Preservation Variables</div>", unsafe_allow_html=True)
        cold_ischemia_hours = st.slider("Cold Ischemia Duration (Hours)", min_value=0, max_value=12, value=4)
        preservation_type = st.selectbox("Perfusion Delivery Modality", ["Static Cold Storage", "Hypothermic Machine Perfusion"])

    st.write("")
    with st.container(border=True):
        st.markdown("<div style='color:#0F172A; font-weight:600; margin-bottom:16px; font-size:1.1rem;'>Recipient Crossmatch Profile</div>", unsafe_allow_html=True)
        antibody_titer_level = st.selectbox("Circulating Anti-Pig Titer Load", ["Low Titer Baseline", "Medium Titer Elevation", "High Titer Saturation"])
        genetic_profile = st.radio("Porcine Donor Genomic Target State", ["Standard Knockout", "Advanced Combinatorial Transgenic"])

    st.write("")
    with st.container(border=True):
        st.markdown("<div style='color:#0F172A; font-weight:600; margin-bottom:16px; font-size:1.1rem;'>Adjunctive Protocol Management</div>", unsafe_allow_html=True)
        complement_inhibitor_active = st.checkbox("Deploy Targeted C5 Complement Blocking Protocol")

# Computational Engine
computed_injury_index = 10
if cold_ischemia_hours <= 4:
    computed_injury_index += (cold_ischemia_hours * 5)
else:
    computed_injury_index += (4 * 5) + ((cold_ischemia_hours - 4) * 10)

if preservation_type == "Static Cold Storage":
    computed_injury_index += 15
if antibody_titer_level == "Medium Titer Elevation":
    computed_injury_index += 15
elif antibody_titer_level == "High Titer Saturation":
    computed_injury_index += 30
if genetic_profile == "Advanced Combinatorial Transgenic":
    computed_injury_index -= 20
if complement_inhibitor_active:
    computed_injury_index -= 15

computed_injury_index = max(0, min(100, computed_injury_index))

with col_telemetry:
    st.markdown("<h5 style='color:#64748B; font-weight:600; letter-spacing:0.5px; margin-bottom:16px;'>REAL-TIME SIMULATION CORE</h5>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<span style='font-size:0.8rem; color:#64748B; font-weight:600; letter-spacing:0.5px;'>PROGNOSTIC VALUE INDEX</span>", unsafe_allow_html=True)
        
        if computed_injury_index >= 70:
            color_stat = "#DC2626"
            label_stat = "CRITICAL PATHOLOGY"
            desc_stat = "Critical Threat Profile: High risk of rapid structural degradation and rejection."
        elif 40 <= computed_injury_index < 70:
            color_stat = "#D97706"
            label_stat = "ELEVATED THREATS"
            desc_stat = "Moderate Threat Profile: Significant reperfusion trauma expected. Intense monitoring mandatory."
        else:
            color_stat = "#16A34A"
            label_stat = "OPTIMAL STABILITY"
            desc_stat = "Favorable baseline analytics calculated. Low ischemic cellular trauma profile."

        st.markdown(f"<div class='metric-value' style='color:{color_stat};'>{computed_injury_index}%</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#F8FAFC; padding:16px; border-left:4px solid {color_stat}; border-radius:6px; font-size:0.95rem; color:#0F172A;'><b>{label_stat}</b> — {desc_stat}</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("<h5 style='color:#64748B; font-weight:600; letter-spacing:0.5px; margin-bottom:16px;'>ALLOCATION STRATEGY PROTOCOL</h5>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f"Case Review Context: Target candidate match profile evaluated at **{computed_injury_index}%** calculated injury index.")
        st.markdown("• **Candidate Alpha:** In immediate systemic decline. Estimated stability survival window under 48 hours.")
        st.markdown("• **Candidate Beta:** Medically managed baseline candidate. Stable registry longevity tracking up to 12 months.")
        st.write("---")
        
        btn_left, btn_right = st.columns(2)
        with btn_left:
            triage_urgency = st.button("Prioritize Clinical Urgency", use_container_width=True)
        with btn_right:
            triage_longevity = st.button("Prioritize System Longevity", use_container_width=True)

        if triage_urgency:
            st.info("Strategy Registered: Urgent Medical Need Model (Egalitarian). Allocation is routed to maximize immediate survival parameters despite elevated risk tracking.")
        if triage_longevity:
            st.success("Strategy Registered: Long-term Asset Longevity Model (Utilitarian). Allocation matches stable profiling metrics to optimize global asset lifespan coordinates.")
