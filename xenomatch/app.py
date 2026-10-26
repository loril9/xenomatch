import streamlit as st

st.set_page_config(
    page_title="XenoMatch | Core",
    layout="wide",
    page_icon="🧬"
)

# Premium Global Styles
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        * { font-family: 'Public Sans', sans-serif; }
        code, pre, .stMetric, [data-testid="stMetricValue"] { font-family: 'JetBrains Mono', monospace !important; }
        
        body { background-color: #0A0F1D; color: #E2E8F0; }
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #111827 !important;
            border: 1px solid #1F2937 !important;
            border-radius: 12px !important;
            padding: 24px !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }
        section[data-testid="stSidebar"] {
            background-color: #0A0F1D !important;
            border-right: 1px solid #1F2937;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 style='color:#00D4B2; font-weight:700; margin-bottom:0;'>🧬 XenoMatch OS v1.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#9CA3AF; font-size:1.1rem; margin-top:0; font-family:JetBrains Mono;'>Multi-Variant Computational Simulator for Porcine-to-Human Xenotransplantation Kinetics</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([1.8, 1.2])

with col1:
    with st.container(border=True):
        st.markdown("<h3 style='color:#E2E8F0; margin-top:0;'>🔬 Project Abstract & Strategic Objectives</h3>", unsafe_allow_html=True)
        st.write(
            "XenoMatch bridges the gap between mechanical translational medicine and clinical bioethics. "
            "By modeling **Ischemia-Reperfusion Injury (IRI) Severity Tiers** alongside hyper-acute rejection barriers, "
            "this application simulates high-stakes allocation triage under severe computational and moral constraints."
        )
        st.info(
            "⚡ **Operational Architecture Note:** Use the sidebar telemetry module to navigate between the "
            "Immunological Bio-Lab, the Dynamic Simulation Sandbox, and the Crucible Moral Evaluation Triage Framework."
        )

with col2:
    with st.container(border=True):
        st.markdown("<h3 style='color:#E2E8F0; margin-top:0;'>👤 Principal Investigator Profile</h3>", unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color:#1F2937; padding:15px; border-left:4px solid #00D4B2; border-radius:4px;'>"
            "<strong style='color:#FFF;'>Dr. Evelyn Vance</strong><br>"
            "<span style='font-size:0.85rem; color:#9CA3AF; font-family:JetBrains Mono;'>Director of Xenotransplantation & Ethical Logistics</span>"
            "</div>", 
            unsafe_allow_html=True
        )
        st.write("")
        st.write(
            "*\"Data dictates viability, but ethics dictates humanity. As we breach the species barrier, "
            "our algorithms must account for human fragility as much as biological compatibility.\"*"
        )
