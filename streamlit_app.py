import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fbf7ef 0%, #fffdf8 50%, #f4eadc 100%);
        color: #062f3a;
    }

    [data-testid="stSidebar"] {
        background: #062f3a;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    h1, h2, h3 {
        font-family: Georgia, serif;
        color: #062f3a;
    }

    .titulo {
        text-align: center;
        font-family: Georgia, serif;
        font-size: 60px;
        letter-spacing: 8px;
        color: #062f3a;
        margin-bottom: 0px;
    }

    .subtitulo {
        text-align: center;
        font-family: Georgia, serif;
        font-size: 26px;
        color: #b1843f;
        font-style: italic;
        margin-top: 0px;
    }

    .linha {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 25px 0 40px 0;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #062f3a 0%, #b1843f 100%);
        color: white;
        border-radius: 999px;
        padding: 0.7rem 1.4rem;
        border: none;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background: #b1843f;
        color: white;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def desenho_olho(titulo):
    html = f"""
    <div style="
        background:#fffaf2;
        border:1px solid #d8b76d;
        border-radius:24px;
        padding:18px;
        box-shadow:0 8px 24px rgba(90,65,30,0.12);
        text-align:center;
        margin-bottom:18px;
    ">
        <svg width="100%" height="230" viewBox="0 0 600 300">
            <rect width="600" height="300" rx="24" fill="#fff7ed"/>
            <ellipse cx="300" cy="150" rx="185" ry="80" fill="#f2c6a5" opacity="0.45"/>
            <path d="M110 150 C180 75, 420 75, 490 150 C420 225, 180 225, 110 150 Z"
                  fill="white" stroke="#062f3a" stroke-width="6"/>
            <circle cx="300" cy="150" r="55" fill="#1f6f7a"/>
            <circle cx="300" cy="150" r="27" fill="#062f3a"/>
            <circle cx="282" cy="132" r="9" fill="white"/>
            <path d="M160 105 C220 58, 385 58, 440 105"
                  fill="none" stroke="#5c3a1e" stroke-width="14" stroke-linecap="round"/>
            <path d="M165 122 C230 95, 370 95, 435 122"
                  fill="none" stroke="#d8703b" stroke-width="6" stroke-dasharray="12 10"/>
            <path d="M165 205 C230 235, 370 235, 435 205"
                  fill="none" stroke="#d8703b" stroke-width="6" stroke-dasharray="12 10"/>
            <text x="300" y="280" text-anchor="middle"
                  font-family="Georgia" font-size="22" fill="#8a6a38">
                {titulo}
            </text>
        </svg>
    </div>
    """
    components.html(html, height=280)


def desenho_ptose():
    html = """
    <div style="
        background:#fffaf2;
        border:1px solid #d8b76d;
        border-radius:24px;
        padding:18px;
        box-shadow:0 8px 24px rgba(90,65,30,0.12);
        text-align:center;
        margin-bottom:18px;
    ">
        <svg width="100%" height="230" viewBox="0 0 600 300">
            <rect width="600" height="300" rx="24" fill="#fff7ed"/>
            <text x="150" y="35" text-anchor="middle" font-family="Georgia" font-size="24" fill="#062f3a">Antes</text>
            <text x="450" y="35" text-anchor="middle" font-family="Georgia" font-size="24" fill="#062f3a">Depois</text>

            <path d="M60 145 C105 95, 195 95, 240 145 C195 195, 105 195, 60 145 Z"
                  fill="white" stroke="#062f3a" stroke-width="5"/>
            <circle cx="150" cy="145" r="36" fill="#1f6f7a"/>
            <circle cx="150" cy="145" r="17" fill="#062f3a"/>
            <path d="M70 108 C110 80, 190 80, 230 108"
                  fill="none" stroke="#5c3a1e" stroke-width="13" stroke-linecap="round"/>
            <rect x="60" y="98" width="180" height="45" fill="#f2c6a5" opacity="0.75"/>
            <text x="150" y="245" text-anchor="middle" font-family="Georgia" font-size="20" fill="#8a6a38">Ptose</text>

            <path d="M360 145 C405 95, 495 95, 540 145 C495 195, 405 195, 360 145 Z"
                  fill="white" stroke="#062f3a" stroke-width="5"/>
            <circle cx="450" cy="145" r="36" fill="#1f6f7a"/>
            <circle cx="450" cy="145" r="17" fill="#062f3a"/>
            <circle cx="438" cy="132" r="7" fill="white"/>
            <path d="M370 100 C410 75, 490 75, 530 100"
                  fill="none" stroke="#5c3a1e" stroke-width="13" stroke-linecap="round"/>
            <text x="450" y="245" text-anchor="middle" font-family="Georgia" font-size="20" fill="#8a6a38">Correção</text>
        </svg>
    </div>
    """
    components.html(html, height=280)


# MENU
st.sidebar.title("BLINK CLINIC")
pagina = st.sidebar.radio(
    "Menu",
    ["Início", "Serviços", "Galeria", "Sobre", "Contactos"]
)

# CABEÇALHO
st.markdown('<div class="titulo">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Oculoplástica · Saúde e estética do olhar</div>', unsafe_allow_html=True)
st.markdown('<div class="linha"></div>', unsafe_allow_html=True)


if pagina == "Início":
    col1, col2 = st.columns([1.1, 0.9])

    with col1:
        st.title("Precisão médica para a saúde e estética do olhar")
        st.write(
            """
            A Blink Clinic dedica-se à avaliação e tratamento das alterações das pálpebras,
            vias lacrimais, órbita e região periocular.
            """
        )
        st.write(
            """
            Uma abordagem médica, segura e personalizada, com foco na função,
            naturalidade e harmonia do olhar.
            """
        )
        st.button("Marcar Consulta")

    with col2:
        desenho_olho("Blefaroplastia · Marcação palpebral")

    st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.subheader("👁️ Pálpebras")
            st.write("Blefaroplastia, ptose palpebral, entrópio, ectrópio e lesões palpebrais.")

    with c2:
        with st.container(border=True):
            st.subheader("💧 Vias lacrimais")
            st.write("Avaliação de lacrimejo persistente e alterações das vias lacrimais.")

    with c3:
        with st.container(border=True):
            st.subheader("✨ Estética periocular")
            st.write("Abordagem médica da estética do olhar com naturalidade e segurança.")


elif pagina == "Serviços":
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        desenho_olho("Blefaroplastia")
        with st.container(border=True):
            st.subheader("Blefaroplastia")
            st.write("Cirurgia das pálpebras superiores e/ou inferiores, com objetivo funcional ou estético.")

        desenho_ptose()
        with st.container(border=True):
            st.subheader("Ptose palpebral")
            st.write("Avaliação e tratamento da queda da pálpebra superior.")

    with col2:
        desenho_olho("Vias lacrimais")
        with st.container(border=True):
            st.subheader("Vias lacrimais")
            st.write("Avaliação de lacrimejo persistente e obstruções lacrimais.")

        desenho_olho("Lesões palpebrais")
        with st.container(border=True):
            st.subheader("Lesões palpebrais")
            st.write("Avaliação e eventual remoção de lesões localizadas nas pálpebras.")


elif pagina == "Galeria":
    st.header("Galeria ilustrativa")

    g1, g2 = st.columns(2)

    with g1:
        desenho_olho("Marcação cirúrgica")
        desenho_ptose()

    with g2:
        desenho_olho("Estética periocular")
        desenho_olho("Avaliação palpebral")


elif pagina == "Sobre":
    col1, col2 = st.columns([0.9, 1.1])

    with col1:
        desenho_olho("Blink Clinic")

    with col2:
        st.header("Sobre a Blink Clinic")
        st.write(
            """
            A Blink Clinic é dedicada à oculoplástica, uma área da oftalmologia
            focada nas pálpebras, vias lacrimais, órbita e região periocular.
            """
        )
        st.write("• Avaliação individualizada")
        st.write("• Rigor médico")
        st.write("• Resultados naturais")
        st.write("• Comunicação clara")
        st.write("• Acompanhamento personalizado")


elif pagina == "Contactos":
    st.header("Marcar Consulta")

    col1, col2 = st.columns([1, 1])

    with col1:
        with st.container(border=True):
            nome = st.text_input("Nome")
            contacto = st.text_input("Contacto")
            motivo = st.selectbox(
                "Motivo da consulta",
                [
                    "Consulta de Oculoplástica",
                    "Blefaroplastia",
                    "Ptose palpebral",
                    "Vias lacrimais",
                    "Lesão palpebral",
                    "Estética periocular",
                    "Outro"
                ]
            )
            mensagem = st.text_area("Mensagem")

            if st.button("Enviar pedido"):
                st.success("Pedido registado. Esta versão ainda não envia emails automaticamente.")

    with col2:
        desenho_olho("Oculoplástica")

st.markdown('<div class="linha"></div>', unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#8a6a38; font-family:Georgia, serif; font-size:20px;'>Blink Clinic · Oculoplástica · Saúde e estética do olhar</p>",
    unsafe_allow_html=True
)
