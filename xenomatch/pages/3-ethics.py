import streamlit as st

st.set_page_config(page_title="XenoMatch | Case Generator", layout="wide")

# Fallback profile variables if user bypasses landing setup
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
        "name": "Candidate Alpha (Marcus)",
        "age": "34 Years",
        "condition": "End-Stage Renal Disease (ESRD)",
        "sensitization": "Highly Sensitized (98% PRA Matrix)",
        "risk": "75% Base Calculated IRI Severity",
        "dilemma": "The organ asset has been in cold ischemia for 11 hours. Proceeding gives Marcus an immediate shot at life but carries a massive risk of hyper-acute cell wall failure within 48 hours, wasting a triple-knockout porcine graft. Bypassing him redirects the asset to a stable candidate."
    },
    {
        "id": "8812",
        "name": "Candidate Gamma (Elena)",
        "age": "19 Years",
        "condition": "Fulminant Hepatic Necrosis",
        "sensitization": "Moderate Sensitization (45% PRA)",
        "risk": "55% Base Calculated IRI Severity",
        "dilemma": "Elena is critically unstable and will lapse into a fatal coma within 24 hours. However, her genetic crossmatch shows cross-reactive antibody elevation. Utilizing this porcine asset functions as a high-risk bridge graft. If the graft fails, she cannot undergo a secondary surgery."
    },
    {
        "id": "1409",
        "name": "Candidate Delta (Robert)",
        "age": "61 Years",
        "condition": "Ischemic Cardiomyopathy",
        "sensitization": "Low Baseline Sensitization (12% PRA)",
        "risk": "85% Calculated Preservation Stress Index",
        "dilemma": "Robert has a highly favorable immune profile, but the donor pig organ suffered microvascular damage during collection. Allocating to Robert saves an elderly patient who has waited years, but his vascular bed may not survive the reperfusion phase, destroying the engineered organ."
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

# Top Bar Profile Tracker Display
active_user = st.session_state.active_doctor_account

st.markdown("<div style='font-size:1.8rem; font-weight:700; color:#0F172A; letter-spacing:-0.75px;'>The Crucible: Ethical Triage Simulator</div>", unsafe_allow_html=True)
st.markdown(f"<div style='font-size:1rem; color:#0EA5E9; margin-bottom:24px; font-weight:600;'>Logged Account Session: {active_user}</div>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin-bottom: 24px;'>", unsafe_allow_html=True)

ctrl_col1, ctrl_col2 = st.columns([2.2, 0.8])
with ctrl_col2:
    if st.button("🔄 Generate Next Registry Case", use_container_width=True):
        st.session_state.active_case_index = (st.session_state.active_case_index + 1) % len(CASE_BANK)

current_case = CASE_BANK[st.session_state.active_case_index]

col_case_left, col_case_right = st.columns([1, 1.2], gap="large")

with col_case_left:
    with st.container(border=True):
        st.markdown(f"<h4 style='color:#DC2626; margin-top:0; font-weight:600;'>Case File #{current_case['id']} Profile</h4>", unsafe_allow_html=True)
        st.markdown(f"""
            <ul style='line-height: 2; padding-left: 20px; font-size: 0.95rem;'>
                <li><b>Name Vector:</b> {current_case['name']}</li>
                <li><b>Age Demographics:</b> {current_case['age']}</li>
                <li><b>Pathology State:</b> {current_case['condition']}</li>
                <li><b>Sensitization Index:</b> {current_case['sensitization']}</li>
                <li><b>Calculated Risk Threat:</b> {current_case['risk']}</li>
            </ul>
        """, unsafe_allow_html=True)

with col_case_right:
    with st.container(border=True):
        st.markdown("<h4 style='color:#0F172A; margin-top:0; font-weight:600;'>Allocation Paradox</h4>", unsafe_allow_html=True)
        st.write(current_case['dilemma'])
        
        st.write("")
        btn_alpha, btn_beta = st.columns(2)
        with btn_alpha:
            if st.button("Route Asset to Candidate", use_container_width=True):
                # Update persistent state under active account
                st.session_state.doctor_ledgers[active_user]["urgency"] += 1
                st.session_state.doctor_ledgers[active_user]["logs"].append(f"Case #{current_case['id']} -> Allocated (Urgency)")
                st.toast(f"Decision logged to {active_user}'s ledger", icon="⚖️")
        with btn_beta:
            if st.button("Retain Asset for Optimization", use_container_width=True):
                # Update persistent state under active account
                st.session_state.doctor_ledgers[active_user]["utility"] += 1
                st.session_state.doctor_ledgers[active_user]["logs"].append(f"Case #{current_case['id']} -> Retained (Utility)")
                st.toast(f"Decision logged to {active_user}'s ledger", icon="📊")

st.write("")
st.markdown(f"<h3 style='color:#0EA5E9; margin-bottom:15px; font-weight:600; font-size:1.25rem;'>Aggregated Choice Ledger for {active_user}</h3>", unsafe_allow_html=True)

with st.container(border=True):
    user_data = st.session_state.doctor_ledgers[active_user]
    
    m_left, m_right = st.columns(2)
    with m_left:
        st.metric("Urgency Metrics (Egalitarian)", f"{user_data['urgency']}")
    with m_right:
        st.metric("Utility Metrics (Utilitarian)", f"{user_data['utility']}")
        
    if user_data["logs"]:
        st.write("---")
        st.markdown("<b>Audit Trail History Logs:</b>", unsafe_allow_html=True)
        for log in user_data["logs"]:
            st.text(f"📝 {log}")
