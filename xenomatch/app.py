import streamlit as st

st.set_page_config(
    page_title="XenoMatch Systems",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aggressive Core Engine Font Override
st.markdown("""
    <style>
        @import url('https://googleapis.com');

        /* Force font directly into Streamlit's internal global variables */
        :root {
            --font-sans: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* Target every text-bearing container layer explicitly to kill Arial */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"], 
        .stMarkdown, p, span, div, label, h1, h2, h3, h4, h5, h6, input, button, select, small {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
            color: #1E293B !important;
        }

        /* Background workspace coloring */
        [data-testid="stAppViewContainer"] {
            background-color: #F8FAFC !important;
        }

        /* Hide the top header bar and rogue anchor elements entirely */
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
            padding: 36px;
            border-radius: 12px;
            margin-bottom: 28px;
            box-shadow: 0 4px 15px rgba(14, 165, 233, 0.1);
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
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01), 0 2px 4px -1px rgba(0, 0, 0, 0.01);
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

        .badge-panel {
            background-color: #F8FAFC;
            border-left: 4px solid #0EA5E9;
            border-radius: 4px;
            padding: 16px;
            margin-bottom: 16px;
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

# Symmetrical Proportional Columns
left_panel, right_panel = st.columns(2, gap="large")

with left_panel:
    st.markdown("""
        <div class="ui-card">
            <div class="card-heading">Project Abstract</div>
            <div class="card-description">
                XenoMatch bridges mechanical translational medicine with predictive data parsing. 
                By evaluating multi-variant physiological constraints such as cold ischemia duration and recipient panel reactivity, 
                the system maps functional graft survival trajectories alongside ethical allocation paradigms.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.info("System Navigation: Toggle between operational layers using the sidebar controls.")

with right_panel:
    st.markdown("""
        <div class="ui-card">
            <div class="card-heading">Clinical Direction</div>
            <div class="badge-panel">
                <strong style="color: #0F172A; font-size: 1rem; display: block; margin-bottom: 2px;">Dr. Evelyn Vance</strong>
                <span style="color: #64748B; font-size: 0.85rem; font-weight: 500;">Director of Translational Transplantation Logistics</span>
            </div>
            <div class="card-description" style="font-style: italic;">
                "Data structures ensure biological compatibility coordinates are optimized, but resource allocation 
                demands robust ethical guidelines. Algorithms must balance survival probabilities with equitable access."
            </div>
        </div>
    """, unsafe_allow_html=True)
