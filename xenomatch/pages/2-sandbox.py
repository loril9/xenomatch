import streamlit as st

st.set_page_config(page_title="XenoMatch | Calculator", layout="wide")

st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"], .stMarkdown, p, span, div, label {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #1E293B !important;
        }
        h1, h2, h3, h4, h5, h6, p, label, span, div { color: #1E293B !important; }
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            padding: 32px !important;
        }
        .stSlider [data-testid="stWidgetLabel"], .stSelectbox label, .stRadio label {
            color: #1E293B !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div style='font-size:1.8rem; font-weight:700; color:#0F172A; letter-spacing:-0.75px;'>Organ Viability Calculator</div>", unsafe_allow_html=True)
st.markdown("<div style='font-size:1rem; color:#64748B; margin-bottom:24px;'>Adjust Case Values to Compute Estimated Tissue Damage</div>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin-bottom: 24px;'>", unsafe_allow_html=True)

col_inputs, col_telemetry = st.columns([1.3, 1.2], gap="large")

with col_inputs:
    st.markdown("<h5 style='color:#64748B; font-weight:600; letter-spacing:0.5px; margin-bottom:16px;'>PATIENT CASE VALUES</h5>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<div style='color:#0F172A; font-weight:600; margin-bottom:16px; font-size:1.1rem;'>Organ Storage Method</div>", unsafe_allow_html=True)
        cold_ischemia_hours = st.slider("Cold Storage Duration (Hours)", min_value=0, max_value=12, value=4)
        preservation_type = st.selectbox("Storage Fluid Delivery Type", ["Static Cold Storage", "Machine Fluid Perfusion"])

    st.write("")
    with st.container(border=True):
        st.markdown("<div style='color:#0F172A; font-weight:600; margin-bottom:16px; font-size:1.1rem;'>Recipient Antibody Crossmatch</div>", unsafe_allow_html=True)
        antibody_titer_level = st.selectbox("Patient Anti-Pig Antibody Levels", ["Low Baseline", "Elevated", "High Saturation"])
        genetic_profile = st.radio("Donor Pig Gene Editing Setup", ["Standard Knockout", "Advanced Multi-Gene Transgenic"])

    st.write("")
    with st.container(border=True):
        st.markdown("<div style='color:#0F172A; font-weight:600; margin-bottom:16px; font-size:1.1rem;'>Treatment Protocol</div>", unsafe_allow_html=True)
        complement_inhibitor_active = st.checkbox("Give Antibody Protective Drug (Eculizumab)")

# Engine Math
computed_injury_index = 10
if cold_ischemia_hours <= 4:
    computed_injury_index += (cold_ischemia_hours * 5)
else:
    computed_injury_index += (4 * 5) + ((cold_ischemia_hours - 4) * 10)

if preservation_type == "Static Cold Storage":
    computed_injury_index += 15
if antibody_titer_level == "Elevated":
    computed_injury_index += 15
elif antibody_titer_level == "High Saturation":
    computed_injury_index += 30
if genetic_profile == "Advanced Multi-Gene Transgenic":
    computed_injury_index -= 20
if complement_inhibitor_active:
    computed_injury_index -= 15

computed_injury_index = max(0, min(100, computed_injury_index))

with col_telemetry:
    st.markdown("<h5 style='color:#64748B; font-weight:600; letter-spacing:0.5px; margin-bottom:16px;'>SIMULATION LOG RESULTS</h5>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<span style='font-size:0.8rem; color:#64748B; font-weight:600; letter-spacing:0.5px;'>ESTIMATED TISSUE DAMAGE INDEX</span>", unsafe_allow_html=True)
        
        if computed_injury_index >= 70:
            color_stat = "#DC2626"
            label_stat = "HIGH RISK PROFILE"
            desc_stat = "High probability of severe cell tearing and early organ rejection."
        elif 40 <= computed_injury_index < 70:
            color_stat = "#D97706"
            label_stat = "MODERATE RISK PROFILE"
            desc_stat = "Tissue damage expected during surgery. Requires intense post-op care."
        else:
            color_stat = "#16A34A"
            label_stat = "OPTIMAL STABILITY PROFILE"
            desc_stat = "Low expected cell damage. Favorable organ matching outcomes."

        st.markdown(f"<h1 style='color:{color_stat}; font-size:4.5rem; margin:0; font-weight:700;'>{computed_injury_index}%</h1>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#F8FAFC; padding:16px; border-left:4px solid {color_stat}; border-radius:6px; font-size:0.95rem; margin-top:15px; color:#0F172A;'><b>{label_stat}</b> — {desc_stat}</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("<h5 style='color:#64748B; font-weight:600; letter-spacing:0.5px; margin-bottom:16px;'>ALLOCATION CASE STUDY</h5>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f"The current matching patient has an estimated tissue damage index of **{computed_injury_index}%**.")
        st.markdown("• **Patient A:** Critically unstable. Estimated survival is under 48 hours without a transplant.")
        st.markdown("• **Patient B:** Medically stable. Can safely remain on the waiting list for up to 12 months.")
        st.write("---")
        
        btn_left, btn_right = st.columns(2)
        with btn_left:
            triage_urgency = st.button("Allocate based on Medical Urgency", use_container_width=True)
        with btn_right:
            triage_longevity = st.button("Allocate based on Long-Term Success", use_container_width=True)

        if triage_urgency:
            st.info("Decision Saved: You gave the organ to the most critical patient first, choosing immediate need over tissue damage risk.")
        if triage_longevity:
            st.success("Decision Saved: You gave the organ to the stable patient to ensure the engineered organ lasts as long as possible.")
