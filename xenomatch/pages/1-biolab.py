import streamlit as st

st.set_page_config(page_title="XenoMatch | Laboratory", layout="wide")

st.markdown("""
    <style>
        html, body, [data-testid="stMainView"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, label, div {
            font-family: 'Inter', sans-serif !important;
        }
        .stApp { background-color: #0B0F19; color: #E2E8F0; }
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #131C2E !important;
            border: 1px solid #1E293B !important;
            border-radius: 6px !important;
            padding: 30px !important;
        }
        /* Style navigation tabs for premium dashboard aesthetic */
        .stTabs [data-baseweb="tab"] {
            color: #94A3B8 !important;
            font-weight: 500 !important;
        }
        .stTabs [aria-selected="true"] {
            color: #00D4B2 !important;
            border-bottom-color: #00D4B2 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#00D4B2; margin-bottom:0; font-weight:700; letter-spacing:-1px;'>Immunology & Ischemia Learning Lab</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#94A3B8; margin-top:5px;'>Pathophysiological Dynamics Registry</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

primary_tabs = st.tabs([
    "Ischemia-Reperfusion Kinetics", 
    "Interspecies Rejection Profiles", 
    "Therapeutic Interventions"
])

with primary_tabs[0]:
    with st.container(border=True):
        st.markdown("<h4 style='color:#FFF; font-weight:600;'>Ischemia-Reperfusion Injury Mechanism</h4>", unsafe_allow_html=True)
        st.write(
            "Organ harvesting initiates cold ischemia, arresting tissue oxygenation pathways and depleting cellular ATP pools. "
            "This metabolic shutdown leaves the vascular bed vulnerable to subsequent microvascular injury."
        )
        st.error(
            "Reperfusion Dynamics: Restoring cellular blood flow induces a massive influx of reactive oxygen species, "
            "leading to immediate endothelial fragmentation, microvascular thrombosis, and programmatic cell death."
        )

with primary_tabs[1]:
    with st.container(border=True):
        st.markdown("<h4 style='color:#FFF; font-weight:600;'>Immunological Surface Barriers</h4>", unsafe_allow_html=True)
        st.write(
            "Human complement cascades instantly target porcine carbohydrate antigens on foreign vessel walls, "
            "triggering hyper-acute vascular destruction."
        )
        st.markdown(
            "<div style='margin-bottom:12px;'><b>Genomic Sugar Deletion:</b> Knocking out native pig glycosylation sites stabilizes the initial vascular barrier interface.</div>"
            "<div><b>Complement Regulation:</b> Transgenic expression of human protective markers safeguards cellular matrices against patient immune tracking.</div>",
            unsafe_allow_html=True
        )

with primary_tabs[2]:
    with st.container(border=True):
        st.markdown("<h4 style='color:#FFF; font-weight:600;'>Monoclonal Antibody Applications</h4>", unsafe_allow_html=True)
        st.write(
            "Targeted therapeutics complement genomic engineering. Complement pathway inhibitors downregulate terminal "
            "cellular assembly steps, mitigating acute mechanical cell lysis during immediate vascular unclamping operations."
        )
