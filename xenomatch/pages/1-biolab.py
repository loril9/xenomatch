import streamlit as st
import os

st.set_page_config(page_title="XenoMatch | Science Reference", layout="wide")

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
        }
        .stTabs [data-baseweb="tab"] { color: #64748B !important; font-weight: 500 !important; }
        .stTabs [aria-selected="true"] { color: #0EA5E9 !important; border-bottom-color: #0EA5E9 !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#0EA5E9; font-weight:700; margin-bottom:0; letter-spacing:-0.5px;'>Science Reference Library</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748B; margin-top:4px;'>Underlying Biological Mechanisms</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin-bottom: 24px;'>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "Preservation Cell Damage", 
    "Genetic Barriers", 
    "Drug Interventions"
])

def load_local_image(primary_name, fallback_name):
    possible_paths = [
        primary_name, fallback_name,
        os.path.join("xenomatch", primary_name), os.path.join("xenomatch", fallback_name),
        os.path.join("xenomatch", "xenomatch", primary_name), os.path.join("xenomatch", "xenomatch", fallback_name)
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

with tab1:
    with st.container(border=True):
        st.markdown("<h4 style='font-weight:600; margin-top:0;'>Ischemia-Reperfusion Injury</h4>", unsafe_allow_html=True)
        st.write("When an organ is harvested, blood flow stops. This starves the cells of oxygen and depletes their energy supplies during storage.")
        st.error("The Problem: Reconnecting blood flow causes a sudden rush of oxygen. This triggers cell swelling, tissue damage, and cell death.")
        
        st.write("")
        iri_path = load_local_image("iri_graph.png", "iri_graph.png")
        if iri_path:
            st.image(iri_path, caption="Fig 1.1: Organ cell changes during cold storage vs blood restoration.", use_container_width=True)

with tab2:
    with st.container(border=True):
        st.markdown("<h4 style='font-weight:600; margin-top:0;'>Pig-to-Human Rejection Filters</h4>", unsafe_allow_html=True)
        st.write("Human blood contains antibodies that immediately spot foreign sugars on pig blood vessels, leading to immediate organ failure.")
        st.markdown("<div style='margin-bottom:12px;'><b>Gene Knockouts:</b> Editing out specific pig genes helps hide the organ from human antibody tracking.</div><div><b>Protective Human Transgenes:</b> Adding human protective proteins helps block the patient's immune system from attacking the graft.</div>", unsafe_allow_html=True)
        
        st.write("")
        genetic_path = load_local_image("genetic_diagram.png", "genetic_graph.png")
        if genetic_path:
            st.image(genetic_path, caption="Fig 1.2: Student research showing cellular pathways used to modify the donor organ.", use_container_width=True)

with tab3:
    with st.container(border=True):
        st.markdown("<h4 style='font-weight:600; margin-top:0;'>Monoclonal Antibody Therapies</h4>", unsafe_allow_html=True)
        st.write("Alongside genetic edits, targeted drugs are necessary. Antibody medications block the patient's complement proteins from tearing apart the donor organ cells during surgery.")
        
        st.write("")
        therapeutics_path = load_local_image("therapeutic_diagram.png", "therapeutic_graph.png")
        if therapeutics_path:
            st.image(therapeutics_path, caption="Fig 1.3: How antibody medications protect the cell lining during blood re-entry.", use_container_width=True)
