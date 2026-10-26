import streamlit as st

st.set_page_config(
    page_title="XenoMatch | Bio Lab",
    layout="wide",
    page_icon="🔬"
)

st.markdown("<h2 style='color:#00D4B2; margin-bottom:0;'>🔬 Clinical Immunology & IRI Learning Lab</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#9CA3AF; font-family:JetBrains Mono; margin-top:0;'>Mastering Underlying Pathophysiological Mechanisms</p>", unsafe_allow_html=True)
st.markdown("---")

tab1, tab2, tab3 = st.tabs([
    "🩸 Ischemia-Reperfusion Injury (IRI)", 
    "🧬 Pig-to-Human Rejection Barriers", 
    "💊 Targeted Therapeutics"
])

with tab1:
    with st.container(border=True):
        st.markdown("<h4 style='color:#FFF;'>What is Ischemia-Reperfusion Injury?</h4>", unsafe_allow_html=True)
        st.write(
            "When a porcine organ is harvested, blood flow stops (**Ischemia**), starving cells of oxygen and depleting cellular ATP. "
            "This primes the vascular tissue for a secondary wave of destruction."
        )
        st.error(
            "⚠️ **The Paradox:** When blood is reconnected (**Reperfusion**), the sudden rush of oxygen triggers a massive burst "
            "of reactive oxygen species (ROS), causing severe endothelial tearing, capillary micro-vascular clotting, and rapid cellular apoptosis."
        )

with tab2:
    with st.container(border=True):
        st.markdown("<h4 style='color:#FFF;'>Overcoming the Immunological Barrier</h4>", unsafe_allow_html=True)
        st.write("Human blood contains pre-formed antibodies that immediately recognize alpha-gal sugars on standard pig blood vessels, triggering immediate organ destruction.")
        
        st.markdown(
            "<div style='margin-bottom:10px;'>🧬 <b style='color:#00D4B2;'>Triple-Knockout (TKO):</b> Genetically engineering the donor pig to remove these specific target sugars entirely prevents immediate hyper-acute hyper-destruction.</div>"
            "<div>🛡️ <b style='color:#00D4B2;'>Human Transgenes (CD46/CD55):</b> Inserting human complement regulatory proteins directly into the porcine genome acts as a structural cloaking device against the recipient's immune attack.</div>",
            unsafe_allow_html=True
        )

with tab3:
    with st.container(border=True):
        st.markdown("<h4 style='color:#FFF;'>Targeted Clinical Interventions</h4>", unsafe_allow_html=True)
        st.write(
            "Even with advanced transgenic genetics, targeted chemical intervention remains mandatory. Modern monoclonal antibodies "
            "like **Eculizumab** neutralize the C5 complement block, acting as an active chemical shield against mechanical "
            "cell damage during vascular unclamping."
        )
