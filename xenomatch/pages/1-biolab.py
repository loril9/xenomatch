import streamlit as st

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
        
        st.write("")
        # Renders your custom Ischemia Phase vs Reperfusion graphic asset flawlessly
        try:
            st.image("xenomatch/iri_graph.png", caption="Fig 1.1: Original BioRender modeling of cold storage ATP depletion vs reactive oxygen species cascades.", use_container_width=True)
        except:
            st.image("iri_graph.png", caption="Fig 1.1: Original BioRender modeling of cold storage ATP depletion vs reactive oxygen species cascades.", use_container_width=True)

with tab_barriers:
    with st.container(border=True):
        st.markdown("<h4 style='font-weight:600; margin-top:0;'>Immunological Surface Barriers</h4>", unsafe_allow_html=True)
        st.write("Human complement cascades instantly target porcine carbohydrate antigens on foreign vessel walls, triggering hyper-acute vascular destruction.")
        st.markdown("<div style='margin-bottom:12px;'><b>Genomic Sugar Deletion:</b> Knocking out native pig glycosylation sites stabilizes the initial vascular barrier interface.</div><div><b>Complement Regulation:</b> Transgenic expression of human protective markers safeguards cellular matrices against patient immune tracking.</div>", unsafe_allow_html=True)
        
        st.write("")
        # Renders your custom Nucleus mRNA genetic sequencing asset flawlessly
        try:
            st.image("xenomatch/genetic_diagram.png", caption="Fig 1.2: Original Student BioRender research mapping transcriptional cellular monoubiquitin pathways.", use_container_width=True)
        except:
            st.image("genetic_diagram.png", caption="Fig 1.2: Original Student BioRender research mapping transcriptional cellular monoubiquitin pathways.", use_container_width=True)

with tab_therapeutics:
    with st.container(border=True):
        st.markdown("<h4 style='font-weight:600; margin-top:0;'>Monoclonal Antibody Applications</h4>", unsafe_allow_html=True)
        st.write("Targeted therapeutics complement genomic engineering. Complement pathway inhibitors downregulate terminal cellular assembly steps, mitigating acute mechanical cell lysis during immediate vascular unclamping operations.")
