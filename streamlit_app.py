import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fbf7ef 0%, #fffdf8 50%, #f3e8d8 100%);
        color: #062f3a;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #062f3a 0%, #123f49 70%, #8a6a38 100%);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        color: #062f3a;
    }
import streamlit as st

st.set_page_config(
    page_title="TESTE BLINK CLINIC",
    page_icon="👁️",
    layout="wide"
)

st.title("🚨 TESTE — CÓDIGO NOVO ATIVO")
st.write("Se estás a ver esta frase, o Streamlit já está a ler o código novo.")

foto = st.file_uploader(
    "Carrega aqui uma fotografia da clínica",
    type=["png", "jpg", "jpeg"]
)

if foto is not None:
    st.image(foto, caption="Fotografia carregada", use_container_width=True)
else:
    st.warning("Ainda não carregaste nenhuma fotografia.")
