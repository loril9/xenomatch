import streamlit as st

st.set_page_config(
    page_title="XenoMatch Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep Layout Restructuring Engine
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        /* Global Canvas Overrides */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"] {
            background-color: #F8FAFC !important;
            color: #0F172A !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Clean Up Form Headers and Structural Titles */
        h1, h2, h3, h4, h5, h6, p, label, span, div {
            font-family: 'Inter', sans-serif !important;
            color: #0F172A !important;
        }
        
        /* Premium Clinical Elevation Cards */
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            padding: 32px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
        }
        
        /* Clean Sidebar Navigation Formatting */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }
        
        /* Universal structural divider line rules */
        hr {
            border-top: 1px solid #E2E8F0 !important;
            margin: 24px 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Application Identity Header Row
st.markdown("<h1 style='color:#0EA5E9; font-weight:700; margin-bottom:0; letter-spacing:-1px;'>XenoMatch Systems</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748B; font-size:1.1rem; margin-top:6px; font-weight:400;'>Computational Simulator for Ischemia-Reperfusion Injury Kinetics in Xenotransplantation</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

col_left, col_right = st.columns([1.6, 1.4])

with col_left:
    with st.container(border=True):
        st.markdown("<h3 style='color:#0F172A; margin-top:0; font-weight:600; font-size:1.4rem;'>Project Abstract</h3>", unsafe_allow_html=True)
        st.write(
            "XenoMatch bridges mechanical translational medicine with predictive data parsing. "
            "By evaluating multi-variant physiological constraints such as cold ischemia duration and recipient panel reactivity, "
            "the system maps functional graft survival trajectories alongside ethical allocation paradigms."
        )
        st.info(
            "Operational Guidance: Use the sidebar navigation menu to switch between clinical data inputs, "
            "the processing matrix, and case registries."
        )

with col_right:
    with st.container(border=True):
        st.markdown("<h3 style='color:#0F172A; margin-top:0; font-weight:600; font-size:1.4rem;'>Clinical Direction</h3>", unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color:#F1F5F9; padding:20px; border-left:4px solid #0EA5E9; border-radius:6px; margin-bottom:20px;'>"
            "<strong style='color:#0F172A; font-weight:600; font-size:1.1rem;'>Dr. Evelyn Vance</strong><br>"
            "<span style='font-size:0.85rem; color:#64748B; font-weight:500; letter-spacing:0.5px;'>Director of Translational Transplantation Logistics</span>"
            "</div>", 
            unsafe_allow_html=True
        )
        st.write(
            "\"Data structures ensure biological compatibility coordinates are optimized, but resource allocation "
            "demands robust ethical guidelines. Algorithms must balance survival probabilities with equitable access.\""
        )
