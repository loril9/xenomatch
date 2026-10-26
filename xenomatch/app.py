import streamlit as st

st.set_page_config(
    page_title="XenoMatch | Core Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Core Design Engine Injection
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        /* Reset typography styles across Streamlit components */
        html, body, [data-testid="stMainView"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, div {
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Structural layout adjustments */
        .stApp {
            background-color: #0B0F19;
            color: #E2E8F0;
        }
        
        /* Seamless clinical container layout */
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #131C2E !important;
            border: 1px solid #1E293B !important;
            border-radius: 6px !important;
            padding: 30px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        
        /* Modern navigation bar layout styling */
        section[data-testid="stSidebar"] {
            background-color: #0B0F19 !important;
            border-right: 1px solid #1E293B;
        }
        
        /* Clean divider line rule overrides */
        hr {
            border-top: 1px solid #1E293B !important;
        }
    </style>
""", unsafe_allow_html=True)

# Main Application Hub Interface
st.markdown("<h1 style='color:#00D4B2; font-weight:700; margin-bottom:0; letter-spacing:-1.5px;'>XenoMatch OS</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#94A3B8; font-size:1.05rem; margin-top:5px; font-weight:400;'>Computational Modeling Platform for Porcine Transplantation Kinetics</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

layout_col_left, layout_col_right = st.columns([1.6, 1.4])

with layout_col_left:
    with st.container(border=True):
        st.markdown("<h3 style='color:#E2E8F0; margin-top:0; font-weight:600; font-size:1.4rem;'>Project Abstract</h3>", unsafe_allow_html=True)
        st.write(
            "XenoMatch models Ischemia-Reperfusion Injury severity tiers alongside hyper-acute rejection barriers. "
            "The platform evaluates high-stakes clinical allocation triage scenarios under strict computational and ethical constraints."
        )
        st.info(
            "System Navigation: Use the left telemetry sidebar menu to toggle between individual laboratory modules."
        )

with layout_col_right:
    with st.container(border=True):
        st.markdown("<h3 style='color:#E2E8F0; margin-top:0; font-weight:600; font-size:1.4rem;'>Clinical Direction</h3>", unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color:#1E293B; padding:16px; border-left:4px solid #00D4B2; border-radius:4px; margin-bottom:15px;'>"
            "<strong style='color:#FFF; font-weight:600;'>Dr. Evelyn Vance</strong><br>"
            "<span style='font-size:0.85rem; color:#94A3B8; font-family:JetBrains Mono;'>Xenotransplantation Director</span>"
            "</div>", 
            unsafe_allow_html=True
        )
        st.write(
            "\"Data dictates biological viability, but ethical frameworks guide asset management. "
            "As we clear immunological barriers, algorithms must balance clinical survival profiles with systemic allocation logic.\""
        )
