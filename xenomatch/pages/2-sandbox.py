import streamlit as st

st.set_page_config(page_title="XenoMatch | Simulator", layout="wide")

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
        /* Style input widgets natively */
        .stSlider [data-testid="stWidgetLabel"] { color: #FFF !important; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#00D4B2; margin-bottom:0; font-weight:700; letter-spacing:-1px;'>Telemetry Simulation Matrix</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#94A3B8; margin-top:5px;'>Computational Multi-Variant Allocation Grid</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

input_grid_col, display_grid_col = st.columns([1.3, 1.2])

with input_grid_col:
    st.markdown("<h5 style='color:#94A3B8; font-weight:600; letter-spacing:0.5px; margin-bottom:15px;'>CLINICAL MODEL VALUES</h5>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<div style='color:#FFF; font-weight:600; margin-bottom:15px;'>Organ Preservation Variables</div>", unsafe_allow_html=True)
        cold_ischemia_hours = st.slider("Cold Ischemia Duration (Hours)", min_value=0, max_value=12, value=4)
        preservation_type = st.selectbox("Perfusion Delivery Modality", ["Static Cold Storage", "Hypothermic Machine Perfusion"])

    st.write("")
    with st.container(border=True):
        st.markdown("<div style='color:#FFF; font-weight:600; margin-bottom:15px;'>Recipient Crossmatch Profile</div>", unsafe_allow_html=True)
        antibody_titer_level = st.selectbox("Circulating Anti-Pig Titer Load", ["Low Titer Baseline", "Medium Titer Elevation", "High Titer Saturation"])
        genetic_profile = st.radio("Porcine Donor Genomic Target State", ["Standard Knockout", "Advanced Combinatorial Transgenic"])

    st.write("")
    with st.container(border=True):
        st.markdown("<div style='color:#FFF; font-weight:600; margin-bottom:15px;'>Adjunctive Protocol Management</div>", unsafe_allow_html=True)
        complement_inhibitor_active = st.checkbox("Deploy Targeted C5 Complement Blocking Protocol")

# Algorithmic Compute Engine logic
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

with display_grid_col:
    st.markdown("<h5 style='color:#94A3B8; font-weight:600; letter-spacing:0.5px; margin-bottom:15px;'>REAL-TIME SIMULATION CORE</h5>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<span style='font-size:0.8rem; color:#94A3B8; font-weight:600; letter-spacing:0.5px;'>PROGNOSTIC VALUE INDEX</span>", unsafe_allow_html=True)
        
        if computed_injury_index >= 70:
            profile_ui_color = "#EF4444"
            profile_ui_desc = "Critical Threat Profile: High probability of structural cellular tearing and hyper-acute asset loss."
            profile_ui_label = "CRITICAL PATHOLOGY"
        elif 40 <= computed_injury_index < 70:
            profile_ui_color = "#F59E0B"
            profile_ui_desc = "Moderate Threat Profile: Significant reperfusion trauma projected. High-surveillance monitoring required."
            profile_ui_label = "ELEVATED RISKS"
        else:
            profile_ui_color = "#10B981"
            profile_ui_desc = "Optimal Threat Profile: Checked markers indicate low cellular injury. Favorable graft runway."
            profile_ui_label = "OPTIMAL STABILITY"

        st.markdown(f"<h1 style='color:{profile_ui_color}; font-size:4rem; margin:0; font-weight:700; font-family:\'JetBrains Mono\', monospace;'>{computed_injury_index}%</h1>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#1E293B; padding:14px; border-left:4px solid {profile_ui_color}; border-radius:4px; font-size:0.9rem; margin-top:12px;'><b>{profile_ui_label}</b> — {profile_ui_desc}</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("<h5 style='color:#94A3B8; font-weight:600; letter-spacing:0.5px; margin-bottom:15px;'>ALLOCATION STRATEGY COMPONENT</h5>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f"Case Review Context: Target candidate profiles with a matching computed index score of **{computed_injury_index}%**.")
        st.markdown("Candidate Alpha: Facing end-stage systemic shutdown; expected survivability window under 48 hours without immediate intervention.")
        st.markdown("Candidate Beta: Listed on the regional clinical baseline matching index; stable runway expected for 12 months.")
        st.write("---")
        
        triage_left_col, triage_right_col = st.columns(2)
        with triage_left_col:
            triage_action_urgent = st.button("Prioritize Clinical Urgency", use_container_width=True)
        with triage_right_col:
            triage_action_optimal = st.button("Prioritize System Longevity", use_container_width=True)

        if triage_action_urgent:
            st.info("Strategy Registered: Medical Urgency Framework (Egalitarian Model). The organ is prioritized for the critical candidate despite baseline risk values.")
        if triage_action_optimal:
            st.success("Strategy Registered: Expected Asset Lifespan Framework (Utilitarian Model). The organ is routed to maximize net graft functionality parameters.")
