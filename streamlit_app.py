import streamlit as st

st.set_page_config(
    page_title="Blink Clinic",
    page_icon="👁️",
    layout="wide"
)

st.title("👁️ Blink Clinic")
st.subheader("Oculoplástica")

st.success("A aplicação está a funcionar!")

foto = st.file_uploader(
    "Carregar fotografia",
    type=["png", "jpg", "jpeg"]
)

if foto:
    st.image(foto, use_container_width=True)
