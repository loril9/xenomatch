import streamlit as st

st.set_page_config(
    page_title="XenoMatch Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep Typography & Layout Alignment Matrix
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        /* Master font declaration */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"], .stMarkdown, p, span, div {
            background-color: #F8FAFC !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            color: #0F172A !important;
        }
        
        /* Wipes out header anchor link wrappers and structural action elements completely */
        [data-testid="stHeaderActionElements"], 
        div[data-testid="StyledLinkIconContainer"], 
        .css-10trblm, .css-7ym5gk, h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
            display: none !important;
            pointer-events: none !important;
        }
        
        /* Stripping down default Streamlit column wrapper padding */
        div[data-testid="stVVerticalBlockBorder"] {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
        }
        
        /* Premium custom clinical cards */
        .clinical-card {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 32px;
            box-shadow: 0 10px 15px -3px rgba(15, 23, 42, 0.03), 0 4px 6px -4px rgba(15, 23, 42, 0.02);
            margin-bottom: 24px;
        }
        
        .app-title {
            font-size: 2.6rem;
            font-weight: 700;
            color: #0F172A;
            letter-spacing: -1.5px;
            margin-bottom: 4px;
        }
        
        .app-subtitle {
            font-size: 1.05rem;
            color: #475569;
            font-weight: 400;
            margin-bottom: 24px;
        }
        
        .card-header {
            font-size: 1.35rem;
            font-weight: 600;
            color: #0F172A;
            margin-bottom: 14px;
            letter-spacing: -0.5px;
        }
        
        .card-body {
            font-size: 1rem;
            color: #334155;
            line-height: 1.6;
        }
        
        .profile-badge {
            background-color: #F1F5F9;
            border-left: 4px solid #0EA5E9;
            border-radius: 4px;
            padding: 16px;
            margin-bottom: 16px;
        }
        
        /* Sidebar styling overrides */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Layout Setup
st.markdown("<div class='app-title'>XenoMatch Systems</div>", unsafe_allow_html=True)
st.markdown("<div class='app-subtitle'>Predictive Computational Modeling for Porcine Transplantation Kinetics</div>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin-bottom: 32px;'>", unsafe_allow_html=True)

layout_col_left, layout_col_right = st.columns([1.5, 1.5], gap="large")

with layout_col_left:
    st.markdown("""
        <div class="clinical-card">
            <div class="card-header">Project Abstract</div>
            <div class="card-body">
                XenoMatch bridges mechanical translational medicine with predictive data parsing. 
                By evaluating multi-variant physiological constraints such as cold ischemia duration and recipient panel reactivity, 
                the system maps functional graft survival trajectories alongside ethical allocation paradigms.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.info("System Navigation: Toggle between application layers using the telemetry sidebar control panel.")

with layout_col_right:
    st.markdown("""
        <div class="clinical-card">
            <div class="card-header">Clinical Leadership</div>
            <div class="profile-badge">
                <strong style="color: #0F172A; font-size: 1.05rem; display: block; margin-bottom: 2px;">Dr. Evelyn Vance</strong>
                <span style="color: #64748B; font-size: 0.85rem; font-weight: 500;">Director of Translational Transplantation Logistics</span>
            </div>
            <div class="card-body" style="font-style: italic; color: #475569;">
                "Data structures ensure biological compatibility coordinates are optimized, but resource allocation 
                demands robust ethical guidelines. Algorithms must balance survival probabilities with equitable access."
            </div>
        </div>
    """, unsafe_allow_html=True)
