import streamlit as st

st.set_page_config(
    page_title="XenoMatch Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize global tracking accounts
if 'active_doctor_account' not in st.session_state:
    st.session_state.active_doctor_account = "Dr. Evelyn Vance"
if 'doctor_ledgers' not in st.session_state:
    st.session_state.doctor_ledgers = {
        "Dr. Evelyn Vance": {"urgency": 0, "utility": 0, "logs": []},
        "Dr. Marcus Chen": {"urgency": 0, "utility": 0, "logs": []},
        "Dr. Sarah Jenkins": {"urgency": 0, "utility": 0, "logs": []}
    }

st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        :root {
            --font-sans: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"], 
        .stMarkdown, p, span, div, label, h1, h2, h3, h4, h5, h6, small {
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
            color: #1E293B !important;
        }
        
        [data-testid="stAppViewContainer"] {
            background-color: #F8FAFC !important;
        }
        
        header, [data-testid="stHeader"], [data-testid="stHeaderActionElements"], div[data-testid="StyledLinkIconContainer"] {
            visibility: hidden !important; display: none !important; height: 0 !important;
        }
        
        .block-container { padding-top: 2rem !important; padding-bottom: 2rem !important; }
        
        .brand-banner {
            background: linear-gradient(135deg, #0284C7 0%, #0EA5E9 100%);
            padding: 36px;
            border-radius: 12px;
            margin-bottom: 28px;
            box-shadow: 0 4px 15px rgba(14, 165, 233, 0.1);
        }
        
        .brand-title { font-size: 2.2rem; font-weight: 700; color: #FFFFFF !important; letter-spacing: -0.5px; margin: 0; }
        .brand-subtitle { font-size: 1rem; color: #E0F2FE !important; font-weight: 400; margin-top: 6px; margin-bottom: 0; }
        
        div[data-testid="stVVerticalBlockBorder"] {
            background: transparent !important; border: none !important; box-shadow: none !important; padding: 0 !important;
        }
        
        .ui-card {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 28px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01);
            margin-bottom: 20px;
        }
        
        .card-heading { font-size: 1.25rem; font-weight: 600; color: #0F172A !important; margin-bottom: 12px; }
        .card-description { font-size: 0.95rem; color: #475569 !important; line-height: 1.6; }
        
        /* Premium custom profile layouts */
        .profile-row {
            display: flex;
            align-items: center;
            gap: 16px;
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 16px;
            margin-bottom: 12px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.01);
        }
        
        .avatar-initial {
            width: 46px;
            height: 46px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 0.95rem;
            color: #FFFFFF !important;
            flex-shrink: 0;
        }
        
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="brand-banner">
        <div class="brand-title">XenoMatch</div>
        <div class="brand-subtitle">Computational Simulation Platform for Ischemia-Reperfusion Injury Kinetics</div>
    </div>
""", unsafe_allow_html=True)

left_panel, right_panel = st.columns(2, gap="large")

with left_panel:
    with st.container(border=True):
        st.markdown("<div class='ui-card'><div class='card-heading'>Project Abstract</div>", unsafe_allow_html=True)
        st.write(
            "XenoMatch bridges mechanical translational medicine with predictive data parsing. "
            "By evaluating multi-variant physiological constraints such as cold ischemia duration and recipient panel reactivity, "
            "the system maps functional graft survival trajectories alongside ethical allocation paradigms."
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.write("")
    with st.container(border=True):
        st.markdown("<div class='ui-card'><div class='card-heading'>🔐 Active Account Selection Console</div>", unsafe_allow_html=True)
        # Select active account user profile
        selected_doc = st.selectbox(
            "Log in as presiding Institutional Review Board investigator:",
            ["Dr. Evelyn Vance", "Dr. Marcus Chen", "Dr. Sarah Jenkins"]
        )
        st.session_state.active_doctor_account = selected_doc
        st.success(f"Active Account: {st.session_state.active_doctor_account} (Decisions will log to this profile ledger)")
        st.markdown("</div>", unsafe_allow_html=True)

with right_panel:
    st.markdown("<div class='ui-card'><div class='card-heading'>Institutional Review Board (IRB) Direction</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="profile-row">
            <div class="avatar-initial" style="background: linear-gradient(135deg, #0284C7, #0EA5E9);">EV</div>
            <div>
                <strong style="color: #0F172A; font-size: 0.95rem; display: block;">Dr. Evelyn Vance</strong>
                <span style="color: #64748B; font-size: 0.8rem; font-weight: 500;">Director of Translational Transplantation Logistics</span>
            </div>
        </div>
        <div class="profile-row">
            <div class="avatar-initial" style="background: linear-gradient(135deg, #10B981, #059669);">MC</div>
            <div>
                <strong style="color: #0F172A; font-size: 0.95rem; display: block;">Dr. Marcus Chen</strong>
                <span style="color: #64748B; font-size: 0.8rem; font-weight: 500;">Chief Interspecies Gene Editing Specialist</span>
            </div>
        </div>
        <div class="profile-row">
            <div class="avatar-initial" style="background: linear-gradient(135deg, #F59E0B, #D97706);">SJ</div>
            <div>
                <strong style="color: #0F172A; font-size: 0.95rem; display: block;">Dr. Sarah Jenkins</strong>
                <span style="color: #64748B; font-size: 0.8rem; font-weight: 500;">Head of Clinical Bioethics Council</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
