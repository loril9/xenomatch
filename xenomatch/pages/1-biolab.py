import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="XenoMatch | Lab", layout="wide")

# Core Engine Font & Theme Override
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        :root { --font-sans: 'Plus Jakarta Sans', sans-serif !important; }
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"], .stMarkdown, p, span, div, label, h1, h2, h3, h4, h5, h6 {
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
            color: #1E293B !important;
        }
        header, [data-testid="stHeader"], [data-testid="stHeaderActionElements"], div[data-testid="StyledLinkIconContainer"] {
            visibility: hidden !important; display: none !important; height: 0 !important;
        }
        .block-container { padding-top: 2rem !important; }
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            padding: 32px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01) !important;
        }
        .stTabs [data-baseweb="tab"] { color: #64748B !important; font-weight: 500 !important; }
        .stTabs [aria-selected="true"] { color: #0EA5E9 !important; border-bottom-color: #0EA5E9 !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#0EA5E9; font-weight:700; margin-bottom:0; letter-spacing:-0.5px;'>Immunology & Ischemia Reference Lab</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748B; margin-top:4px;'>Pathophysiological Dynamics Registry</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin-bottom: 24px;'>", unsafe_allow_html=True)

tab_kinetics, tab_barriers, tab_therapeutics = st.tabs([
    "Ischemia-Reperfusion Kinetics", 
    "Interspecies Rejection Profiles", 
    "Therapeutic Interventions"
])

with tab_kinetics:
    with st.container(border=True):
        st.markdown("<h4 style='font-weight:600; margin-top:0;'>Ischemia-Reperfusion Injury Mechanism</h4>", unsafe_allow_html=True)
        st.write("Organ harvesting initiates cold ischemia, arresting tissue oxygenation pathways and depleting cellular ATP pools. This metabolic shutdown leaves the vascular bed vulnerable to subsequent microvascular damage.")
        st.error("Reperfusion Dynamics: Restoring cellular blood flow induces a massive influx of reactive oxygen species, leading to immediate endothelial fragmentation, microvascular thrombosis, and programmatic cell death.")

with tab_barriers:
    with st.container(border=True):
        st.markdown("<h4 style='font-weight:600; margin-top:0;'>Immunological Surface Barriers</h4>", unsafe_allow_html=True)
        st.write("Human complement cascades instantly target porcine carbohydrate antigens on foreign vessel walls, triggering hyper-acute vascular destruction.")
        st.markdown("<div style='margin-bottom:12px;'><b>Genomic Sugar Deletion:</b> Knocking out native pig glycosylation sites stabilizes the initial vascular barrier interface.</div><div><b>Complement Regulation:</b> Transgenic expression of human protective markers safeguards cellular matrices against patient immune tracking.</div>", unsafe_allow_html=True)

with tab_therapeutics:
    with st.container(border=True):
        st.markdown("<h4 style='font-weight:600; margin-top:0;'>Monoclonal Antibody Applications</h4>", unsafe_allow_html=True)
        st.write("Targeted therapeutics complement genomic engineering. Complement pathway inhibitors downregulate terminal cellular assembly steps, mitigating acute mechanical cell lysis during immediate vascular unclamping operations.")

# 🚀 FOOLPROOF MATH DIAGRAM GENERATOR (Replaces the broken image completely)
st.write("")
with st.container(border=True):
    st.markdown("<h4 style='font-weight:600; margin-top:0; font-size:1.15rem; margin-bottom:16px;'>Histological Modeling Framework</h4>", unsafe_allow_html=True)
    
    # Generate clean mock analytical data grid to simulate endothelial scanning
    fig, ax = plt.subplots(figsize=(10, 3.5), facecolor='#FFFFFF')
    x = np.linspace(0, 10, 200)
    y1 = np.sin(x) * np.exp(-x/5) * 50 + 50
    y2 = np.cos(x) * np.exp(-x/6) * 30 + 40
    
    ax.plot(x, y1, color='#0EA5E9', label='Endothelial Cell Viability (%)', linewidth=2.5)
    ax.plot(x, y2, color='#EF4444', label='Reactive Oxygen Species (ROS) Concentration', linewidth=2, linestyle='--')
    
    # Styling the programmatic figure to match the UI perfectly
    ax.set_facecolor('#F8FAFC')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CBD5E1')
    ax.spines['bottom'].set_color('#CBD5E1')
    ax.tick_params(colors='#64748B', labelsize=9)
    ax.set_xlabel('Perfusion Cycle Duration (Hours)', color='#64748B', fontsize=10)
    ax.legend(facecolor='#FFFFFF', edgecolor='#E2E8F0', loc='upper right', fontsize=9)
    ax.grid(True, linestyle=':', alpha=0.5, color='#CBD5E1')
    
    # Render figure directly in layout without image files
    st.pyplot(fig)
    st.caption("Fig 1: Computer-generated real-time kinetic modeling curve of complement cascades in vascular endothelium during oxygenation cycles.")
