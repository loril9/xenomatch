import streamlit as st

st.set_page_config(page_title="XenoMatch | Laboratory Hub", layout="wide")

st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainView"] {
            background-color: #F8FAFC !important;
            color: #0F172A !important;
            font-family: 'Inter', sans-serif !important;
        }
        h1, h2, h3, h4, h5, h6, p, label, span, div { color: #0F172A !important; }
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

st.markdown("<h2 style='color:#0EA5E9; margin-bottom:0; font-weight:700; letter-spacing:-0.5px;'>Immunology & Ischemia Reference Lab</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748B; margin-top:6px;'>Pathophysiological Dynamics Registry</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

tab_kinetics, tab_barriers, tab_therapeutics = st.tabs([
    "Ischemia-Reperfusion Kinetics", 
    "Interspecies Rejection Profiles", 
    "Therapeutic Interventions"
])

with tab_kinetics:
    with st.container(border=True):
        st.markdown("<h4 style='color:#0F172A; font-weight:600;'>Ischemia-Reperfusion Injury Mechanism</h4>", unsafe_allow_html=True)
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
        st.markdown("<h4 style='color:#0F172A; font-weight:600;'>Immunological Surface Barriers</h4>", unsafe_allow_html=True)
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
        st.markdown("<h4 style='color:#0F172A; font-weight:600;'>Monoclonal Antibody Applications</h4>", unsafe_allow_html=True)
        st.write(
            "Targeted therapeutics complement genomic engineering. Complement pathway inhibitors downregulate terminal "
            "cellular assembly steps, mitigating acute mechanical cell lysis during immediate vascular unclamping operations."
        )

# Direct Web Image Render Engine (Fetches crisp clinical vectors)
st.write("")
with st.container(border=True):
    st.markdown("<h4 style='color:#0F172A; margin-top:0; font-weight:600; font-size:1.2rem;'>Histological Modeling Framework</h4>", unsafe_allow_html=True)
    st.image(
        "https://unsplash.com", 
        caption="Microscopic monitoring view of vascular endothelial cell matrices during oxygenation cycles.",
        use_container_width=True
    )
