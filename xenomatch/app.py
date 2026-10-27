import streamlit as st

st.set_page_config(
    page_title="XenoMatch Systems",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aggressive Core Engine Font & Layout Override
st.markdown("""
    <style>
        @import url('https://googleapis.com');

        /* Force font directly into Streamlit's internal global variables */
        :root {
            --font-sans: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* Target text-bearing container layers explicitly */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"], 
        .stMarkdown, p, span, div, label, h1, h2, h3, h4, h5, h6, input, button, select, small {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
            color: #1E293B !important;
        }

        /* Background workspace coloring */
        [data-testid="stAppViewContainer"] {
            background-color: #F8FAFC !important;
        }

        /* Hide the top header bar and anchor elements entirely */
        header, [data-testid="stHeader"], [data-testid="stHeaderActionElements"], div[data-testid="StyledLinkIconContainer"] {
            visibility: hidden !important;
            display: none !important;
            height: 0 !important;
        }

        /* Prevent empty top padding gaps */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }

        /* Custom Header Banner */
        .brand-banner {
            background: linear-gradient(135deg, #0284C7 0%, #0EA5E9 100%);
            padding: 32px;
            border-radius: 12px;
            margin-bottom: 24px;
            box-shadow: 0 4px 15px rgba(14, 165, 233, 0.1);
            text-align: center;
        }

        .brand-title {
            font-size: 2.2rem;
            font-weight: 700;
            color: #FFFFFF !important;
            letter-spacing: -0.5px;
            margin: 0;
        }

        .brand-subtitle {
            font-size: 1rem;
            color: #E0F2FE !important;
            font-weight: 400;
            margin-top: 6px;
            margin-bottom: 0;
        }

        /* Remove default Streamlit vertical box layout frames */
        div[data-testid="stVVerticalBlockBorder"] {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
        }

        /* Custom Information Cards */
        .ui-card {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 28px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01);
            margin-bottom: 20px;
        }

        .card-heading {
            font-size: 1.25rem;
            font-weight: 600;
            color: #0F172A !important;
            margin-bottom: 12px;
            letter-spacing: -0.3px;
        }

        .card-description {
            font-size: 0.95rem;
            color: #475569 !important;
            line-height: 1.6;
        }

        .profile-row {
            display: flex;
            align-items: center;
            gap: 16px;
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 16px;
            margin-bottom: 12px;
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
        
        /* Clean Sidebar formatting */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }
        
        section[data-testid="stSidebar"] div {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
    </style>
""", unsafe_allow_html=True)

# Main Banner Layout Component
st.markdown("""
    <div class="brand-banner">
        <div class="brand-title">XenoMatch Systems</div>
        <div class="brand-subtitle">Computational Simulation Platform for Ischemia-Reperfusion Injury Kinetics</div>
    </div>
""", unsafe_allow_html=True)

# Render your custom hand-drawn logo centered right beneath the title banner
logo_col1, logo_col2, logo_col3 = st.columns([1, 0.8, 1])
with logo_col2:
    try:
        st.image("xenomatch/xenomatch_logo.png", use_container_width=True)
    except:
        try:
            st.image("xenomatch_logo.png", use_container_width=True)
        except:
            st.warning("Logo image file upload to repository in progress...")

st.write("")

# Symmetrical Proportional Columns
left_panel, right_panel = st.columns(2, gap="large")

with left_panel:
    with st.container(border=True):
        st.markdown("<div class='ui-card'><div class='card-heading'>Project Description</div>", unsafe_allow_html=True)
        st.write(
            "XenoMatch is a tool that evaluates how cell damage during organ preservation affects recipient "
            "compatibility. By analyzing clinical values like storage time and antibody levels, "
            "the system estimates graft success rates and walks users through ethical distribution choices."
        )
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("")
    with st.container(border=True):
        st.markdown("<div class='ui-card'><div class='card-heading'>User Account Login</div>", unsafe_allow_html=True)
        selected_doc = st.selectbox(
            "Select an investigator profile to log decisions:",
            ["Dr. Evelyn Vance", "Dr. Marcus Chen", "Dr. Sarah Jenkins"]
        )
        st.session_state.active_doctor_account = selected_doc
        st.success(f"Logged in as: {st.session_state.active_doctor_account}")
        st.markdown("</div>", unsafe_allow_html=True)

with right_panel:
    st.markdown("<div class='ui-card'><div class='card-heading'>Medical Review Board Profiles</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="profile-row">
            <div class="avatar-initial" style="background: linear-gradient(135deg, #0284C7, #0EA5E9);">EV</div>
            <div>
                <strong style="color: #0F172A; font-size: 0.95rem; display: block;">Dr. Evelyn Vance</strong>
                <span style="color: #64748B; font-size: 0.8rem; font-weight: 500;">Director of Transplantation Logistics</span>
            </div>
        </div>
        <div class="profile-row">
            <div class="avatar-initial" style="background: linear-gradient(135deg, #10B981, #059669);">MC</div>
            <div>
                <strong style="color: #0F172A; font-size: 0.95rem; display: block;">Dr. Marcus Chen</strong>
                <span style="color: #64748B; font-size: 0.8rem; font-weight: 500;">Lead Gene Editing Specialist</span>
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
