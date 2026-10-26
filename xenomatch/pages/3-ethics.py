import streamlit as st

st.set_page_config(
    page_title="XenoMatch | Crucible",
    layout="wide",
    page_icon="⚖️"
)

if 'ethics_score_log' not in st.session_state:
    st.session_state.ethics_score_log = []

st.markdown("<h2 style='color:#00D4B2; margin-bottom:0;'>⚖️ The Crucible: Moral Case Studies</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#9CA3AF; font-family:JetBrains Mono; margin-top:0;'>Comprehensive Ethical Decision-Support Registry</p>", unsafe_allow_html=True)
st.markdown("---")

case_id = st.selectbox("Select Active Case File From Registry", [
    "Case #4901: Patient Marcus (High-Urgency Cross-Match Override)",
    "Case #7822: Sophia (High-Viability Protocol)"
])

if "Marcus" in case_id:
    c1, c2 = st.columns([1, 1.2])
    with c1:
        with st.container(border=True):
            st.markdown("<h4 style='color:#EF4444; margin-top:0;'>📋 Patient Profile: Marcus</h4>", unsafe_allow_html=True)
            st.markdown(
                "<ul>"
                "<li><b>Age:</b> 34</li>"
                "<li><b>Clinical Status:</b> Critical, End-Stage Renal Disease</li>"
                "<li><b>Sensitization:</b> Highly sensitized, panel-reactive antibodies</li>"
                "<li><b>Calculated Baseline IRI Risk:</b> 75%</li>"
                "</ul>", unsafe_allow_html=True
            )
    with c2:
        with st.container(border=True):
            st.markdown("<h4 style='color:#FFF; margin-top:0;'>⚖️ The Dilemma</h4>", unsafe_allow_html=True)
            st.write(
                "Marcus is young but highly sensitized. The available porcine kidney has been on Static Cold Storage for 11 hours, "
                "meaning extreme reperfusion trauma is a mathematical certainty. If you proceed, the graft might fail within hours, "
                "wasting a highly engineered genomic asset. If you hold, Marcus will not survive the week, but the organ can go to a stable patient."
            )
            
            st.write("")
            b1, b2 = st.columns(2)
            with b1:
                if st.button("Allocate to Marcus", use_container_width=True):
                    st.session_state.ethics_score_log.append("Egalitarian")
                    st.error("🚨 **Verdict Logged:** You chose to save Marcus. Dr. Vance notes: *'We choose humanity over perfect statistics.'*")
            with b2:
                if st.button("Hold for Stability", use_container_width=True):
                    st.session_state.ethics_score_log.append("Utilitarian")
                    st.success("💎 **Verdict Logged:** You held the organ. Dr. Vance notes: *'A difficult calculus, but protecting the organ preserves long-term clinical utility.'*")

st.write("")
st.markdown("---")
st.markdown("<h3 style='color:#00D4B2; margin-bottom:10px;'>📊 Cumulative Institutional Ethics Profile</h3>", unsafe_allow_html=True)

with st.container(border=True):
    if st.session_state.ethics_score_log:
        egal_count = st.session_state.ethics_score_log.count("Egalitarian")
        util_count = st.session_state.ethics_score_log.count("Utilitarian")
        
        sc1, sc2 = st.columns(2)
        with sc1:
            st.metric("⚖️ Egalitarian Decisions", f"{egal_count}", delta="Prioritizing Immediate Need")
        with sc2:
            st.metric("📊 Utilitarian Decisions", f"{util_count}", delta="Prioritizing System Utility")
    else:
        st.info("No cases have been processed yet. Complete a case dilemma above to generate your live ethical tracking coordinates.")
