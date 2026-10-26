import streamlit as st

st.set_page_config(page_title="XenoMatch | Cases", layout="wide")

if 'strategic_decision_log' not in st.session_state:
    st.session_state.strategic_decision_log = []
if 'active_doctor_account' not in st.session_state:
    st.session_state.active_doctor_account = "Dr. Evelyn Vance"
if 'doctor_ledgers' not in st.session_state:
    st.session_state.doctor_ledgers = {
        "Dr. Evelyn Vance": {"urgency": 0, "utility": 0, "logs": []},
        "Dr. Marcus Chen": {"urgency": 0, "utility": 0, "logs": []},
        "Dr. Sarah Jenkins": {"urgency": 0, "utility": 0, "logs": []}
    }

CASE_BANK = [
    {
        "id": "4901",
        "name": "Marcus",
        "age": "34 Years",
        "condition": "End-Stage Kidney Disease",
        "sensitization": "Highly Sensitized (98% Antibody Matching Level)",
        "risk": "75% Preservation Cell Damage Risk",
        "dilemma": "The organ has been in cold storage for 11 hours, making tissue damage certain. Giving it to Marcus gives him a chance at life but risks early organ failure, wasting a modified graft. Bypassing him passes the organ to a low-risk patient."
    },
    {
        "id": "8812",
        "name": "Elena",
        "age": "19 Years",
        "condition": "Acute Liver Failure",
        "sensitization": "Moderate Sensitization (45% Antibody level)",
        "risk": "55% Preservation Cell Damage Risk",
        "dilemma": "Elena is critically unstable and has under 24 hours to live. Her antibody test suggests a partial match. Using this organ works as an immediate bridge to save her life, but if the organ fails, she cannot survive a second operation."
    },
    {
        "id": "1409",
        "name": "Robert",
        "age": "61 Years",
        "condition": "Severe Heart Disease",
        "sensitization": "Low Baseline Sensitization (12% Antibody level)",
        "risk": "85% Preservation Cell Damage Risk",
        "dilemma": "Robert has an excellent immune profile, but the donor organ suffered fluid damage during recovery. Giving it to Robert saves a patient who has waited years, but his blood vessel lining may reject the damaged tissue during surgery."
    }
]

if 'active_case_index' not in st.session_state:
    st.session_state.active_case_index = 0

st.markdown("""
    <style>
        @import url('https://googleapis.com');
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"], .stMarkdown, p, span, div, label {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        [data-testid="stHeader"], div[data-testid="StyledLinkIconContainer"] { display: none !important; }
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            padding: 32px !important;
        }
        .stMetric [data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace !important;
            color: #0F172A !important;
        }
    </style>
""", unsafe_allow_html=True)

active_user = st.session_state.active_doctor_account

st.markdown("<div style='font-size:1.8rem; font-weight:700; color:#0F172A; letter-spacing:-0.75px;'>Case Study Allocation Module</div>", unsafe_allow_html=True)
st.markdown(f"<div style='font-size:1rem; color:#0EA5E9; margin-bottom:24px; font-weight:600;'>Active User Account: {active_user}</div>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin-bottom: 24px;'>", unsafe_allow_html=True)

ctrl_col1, ctrl_col2 = st.columns([2.2, 0.8])
with ctrl_col2:
    if st.button("🔄 Load Next Patient Case File", use_container_width=True):
        st.session_state.active_case_index = (st.session_state.active_case_index + 1) % len(CASE_BANK)

current_case = CASE_BANK[st.session_state.active_case_index]

col_case_left, col_case_right = st.columns([1, 1.2], gap="large")

with col_case_left:
    with st.container(border=True):
        st.markdown(f"<h4 style='color:#DC2626; margin-top:0; font-weight:600;'>Patient Profile #{current_case['id']}</h4>", unsafe_allow_html=True)
        st.markdown(f"""
            <ul style='line-height: 2; padding-left: 20px; font-size: 0.95rem;'>
                <li><b>Patient Name:</b> {current_case['name']}</li>
                <li><b>Age:</b> {current_case['age']}</li>
                <li><b>Diagnosis:</b> {current_case['condition']}</li>
                <li><b>Antibody Matching:</b> {current_case['sensitization']}</li>
                <li><b>Tissue Damage Score:</b> {current_case['risk']}</li>
            </ul>
        """, unsafe_allow_html=True)

with col_case_right:
    with st.container(border=True):
        st.markdown("<h4 style='color:#0F172A; margin-top:0; font-weight:600;'>Allocation Dilemma</h4>", unsafe_allow_html=True)
        st.write(current_case['dilemma'])
        
        st.write("")
        btn_alpha, btn_beta = st.columns(2)
        with btn_alpha:
            if st.button("Transplant Immediately", use_container_width=True):
                st.session_state.doctor_ledgers[active_user]["urgency"] += 1
                st.session_state.doctor_ledgers[active_user]["logs"].append(f"Case #{current_case['id']} -> Transplanted (Urgency)")
                st.toast(f"Decision logged to {active_user}'s ledger", icon="⚖️")
        with btn_beta:
            if st.button("Hold Organ for Better Match", use_container_width=True):
                st.session_state.doctor_ledgers[active_user]["utility"] += 1
                st.session_state.doctor_ledgers[active_user]["logs"].append(f"Case #{current_case['id']} -> Held (Long-Term Success)")
                st.toast(f"Decision logged to {active_user}'s ledger", icon="📊")

st.write("")
st.markdown(f"<h3 style='color:#0EA5E9; margin-bottom:15px; font-weight:600; font-size:1.25rem;'>Saved Choice Records for {active_user}</h3>", unsafe_allow_html=True)

with st.container(border=True):
    user_data = st.session_state.doctor_ledgers[active_user]
    
    m_left, m_right = st.columns(2)
    with m_left:
        st.metric("Urgency Decisions", f"{user_data['urgency']}")
    with m_right:
        st.metric("Long-Term Success Decisions", f"{user_data['utility']}")
        
    if user_data["logs"]:
        st.write("---")
        st.markdown("<b>Audit Trail Log:</b>", unsafe_allow_html=True)
        for log in user_data["logs"]:
            st.text(f"📝 {log}")
