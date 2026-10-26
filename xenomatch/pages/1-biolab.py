import streamlit as st

st.set_page_config(page_title="XenoMatch | Lab", layout="wide")

st.markdown("""
    <style>
        @import url('https://googleapis.com');
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"], .stMarkdown, p, span, div {
            background-color: #F8FAFC !important;
            font-family: 'Inter', sans-serif !important;
            color: #0F172A !important;
        }
        [data-testid="stHeaderActionElements"], div[data-testid="StyledLinkIconContainer"], h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
            display: none !important;
            pointer-events: none !important;
        }
        div[data-testid="stVVerticalBlockBorder"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            padding: 32px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02) !important;
        }
        .stTabs [data-baseweb="tab"] { color: #64748B !important; font-weight: 500 !important; }
        .stTabs [aria-selected="true"] { color: #0EA5E9 !important; border-bottom-color: #0EA5E9 !important; }
        .module-header { font-size: 1.8rem; font-weight: 700; color: #0F172A; letter-spacing: -0.75px; margin-bottom: 4px; }
        .module-subtitle { font-size: 1rem; color: #64748B; margin-bottom: 24px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='module-header'>Immunology & Ischemia Reference Lab</div>", unsafe_allow_html=True)
st.markdown("<div class='module-subtitle'>Pathophysiological Dynamics Registry</div>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin-bottom: 24px;'>", unsafe_allow_html=True)

tab_kinetics, tab_barriers, tab_therapeutics = st.tabs([
    "Ischemia-Reperfusion Kinetics", 
    "Interspecies Rejection Profiles", 
    "Therapeutic Interventions"
])

with tab_kinetics:
    with st.container(border=True):
        st.markdown("<h4 style='color:#0F172A; font-weight:600; margin-top:0;'>Ischemia-Reperfusion Injury Mechanism</h4>", unsafe_allow_html=True)
        st.write(
            "Organ harvesting initiates cold ischemia, arresting tissue oxygenation pathways and depleting cellular ATP pools. "
            "This metabolic shutdown leaves the vascular bed vulnerable to subsequent microvascular damage."
        )
        st.error(
            "Reperfusion Dynamics: Restoring cellular blood flow induces a massive influx of reactive oxygen species, "
            "leading to immediate endothelial fragmentation, microvascular thrombosis, and programmatic cell death."
        )

with tab_barriers:
    with st.container(border=True):
        st.markdown("<h4 style='color:#0F172A; font-weight:600; margin-top:0;'>Immunological Surface Barriers</h4>", unsafe_allow_html=True)
        st.write(
            "Human complement cascades instantly target porcine carbohydrate antigens on foreign vessel walls, "
            "triggering hyper-acute vascular destruction."
        )
        st.markdown(
            "<div style='margin-bottom:12px; color:#0F172A;'><b>Genomic Sugar Deletion:</b> Knocking out native pig glycosylation sites stabilizes the initial vascular barrier interface.</div>"
            "<div style='color:#0F172A;'><b>Complement Regulation:</b> Transgenic expression of human protective markers safeguards cellular matrices against patient immune tracking.</div>",
            unsafe_allow_html=True
        )

with tab_therapeutics:
    with st.container(border=True):
        st.markdown("<h4 style='color:#0F172A; font-weight:600; margin-top:0;'>Monoclonal Antibody Applications</h4>", unsafe_allow_html=True)
        st.write(
            "Targeted therapeutics complement genomic engineering. Complement pathway inhibitors downregulate terminal "
            "cellular assembly steps, mitigating acute mechanical cell lysis during immediate vascular unclamping operations."
        )

# Direct External Biomedical Asset Integration
st.write("")
with st.container(border=True):
    st.markdown("<h4 style='color:#0F172A; margin-top:0; font-weight:600; font-size:1.15rem; margin-bottom:16px;'>Histological Modeling Framework</h4>", unsafe_allow_html=True)
    st.image(
        "https://unsplash.com", 
        caption="Microscopic monitoring view of vascular endothelial cell matrices during oxygenation cycles.",
        use_container_width=True
    )
