import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# IMAGENS REAIS / EDUCATIVAS
IMG_BLEFARO = "https://commons.wikimedia.org/wiki/Special:FilePath/Upper%20eyelid%20blepharoplasty%20incision.png"
IMG_PTOSE = "https://commons.wikimedia.org/wiki/Special:FilePath/Congenitalptosis.JPG"
IMG_VIAS = "https://commons.wikimedia.org/wiki/Special:FilePath/Tear%20system.svg"
IMG_MARCACAO = "https://commons.wikimedia.org/wiki/Special:FilePath/Eyelid%20surgery%20outline.jpg"
IMG_BLEFARO_INF = "https://commons.wikimedia.org/wiki/Special:FilePath/Lower%20Eyelid%20Blepharoplasty.jpg"

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fbf7ef 0%, #fffdf8 48%, #f4eadc 100%);
        color: #062f3a;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #062f3a 0%, #123f49 65%, #8a6a38 100%);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        color: #062f3a;
    }

    .brand-title {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 64px;
        letter-spacing: 9px;
        color: #062f3a;
        margin-bottom: 0;
    }

    .brand-subtitle {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 27px;
        color: #b1843f;
        font-style: italic;
        margin-top: -6px;
    }

    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 26px 0 40px 0;
    }

    .section-label {
        color: #b1843f;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 800;
        font-size: 13px;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #062f3a 0%, #b1843f 100%);
        color: white;
        border-radius: 999px;
        padding: 0.75rem 1.5rem;
        border: none;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background: #b1843f;
        color: white;
        border: none;
    }

    img {
        border-radius: 22px;
        border: 1px solid rgba(177, 132, 63, 0.35);
        box-shadow: 0 10px 25px rgba(90, 65, 30, 0.12);
    }

    .note {
        background: rgba(255, 255, 255, 0.78);
        border-left: 5px solid #b1843f;
        padding: 18px 22px;
        border-radius: 16px;
        margin-top: 18px;
        box-shadow: 0 8px 22px rgba(90, 65, 30, 0.08);
    }

    .footer {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        color: #8a6a38;
        font-size: 21px;
        font-style: italic;
        margin-top: 45px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("BLINK CLINIC")
pagina = st.sidebar.radio(
    "Menu",
    ["Início", "Serviços", "Galeria", "Sobre", "Contactos"]
)

st.markdown('<div class="brand-title">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="brand-subtitle">Oculoplástica · Pálpebras · Vias Lacrimais · Órbita</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

if pagina == "Início":
    col1, col2 = st.columns([1.15, 0.85])

    with col1:
        st.markdown('<div class="section-label">Clínica de Oculoplástica</div>', unsafe_allow_html=True)
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

        st.markdown(
            """
            <div class="note">
            Cuidado especializado em blefaroplastia, ptose palpebral,
            vias lacrimais, lesões palpebrais e estética periocular.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image(IMG_BLEFARO, caption="Marcação de blefaroplastia superior", use_container_width=True)

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.image(IMG_MARCACAO, caption="Marcação palpebral", use_container_width=True)
        st.subheader("Pálpebras")
        st.write("Blefaroplastia, ptose palpebral, entrópio, ectrópio e lesões palpebrais.")

    with c2:
        st.image(IMG_VIAS, caption="Sistema lacrimal", use_container_width=True)
        st.subheader("Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente e obstrução das vias lacrimais.")

    with c3:
        st.image(IMG_PTOSE, caption="Ptose palpebral", use_container_width=True)
        st.subheader("Ptose palpebral")
        st.write("Avaliação da queda da pálpebra superior e impacto funcional ou estético.")

elif pagina == "Serviços":
    st.markdown('<div class="section-label">Serviços médicos</div>', unsafe_allow_html=True)
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        st.image(IMG_BLEFARO, caption="Blefaroplastia superior", use_container_width=True)
        with st.container(border=True):
            st.subheader("Blefaroplastia")
            st.write(
                """
                Cirurgia das pálpebras superiores e/ou inferiores, com objetivo funcional,
                estético ou combinado.
                """
            )

        st.image(IMG_PTOSE, caption="Ptose palpebral", use_container_width=True)
        with st.container(border=True):
            st.subheader("Ptose palpebral")
            st.write("Avaliação e tratamento da queda da pálpebra superior.")

    with col2:
        st.image(IMG_VIAS, caption="Vias lacrimais", use_container_width=True)
        with st.container(border=True):
            st.subheader("Vias lacrimais")
            st.write("Avaliação de lacrimejo persistente e alterações da drenagem lacrimal.")

        st.image(IMG_BLEFARO_INF, caption="Blefaroplastia inferior", use_container_width=True)
        with st.container(border=True):
            st.subheader("Estética periocular")
            st.write("Abordagem médica da estética do olhar com naturalidade e segurança.")

elif pagina == "Galeria":
    st.markdown('<div class="section-label">Imagens clínicas e educativas</div>', unsafe_allow_html=True)
    st.header("Galeria")

    g1, g2, g3 = st.columns(3)

    with g1:
        st.image(IMG_BLEFARO, caption="Blefaroplastia superior", use_container_width=True)
        st.image(IMG_MARCACAO, caption="Marcação cirúrgica", use_container_width=True)

    with g2:
        st.image(IMG_PTOSE, caption="Ptose palpebral", use_container_width=True)
        st.image(IMG_BLEFARO_INF, caption="Blefaroplastia inferior", use_container_width=True)

    with g3:
        st.image(IMG_VIAS, caption="Sistema lacrimal", use_container_width=True)

elif pagina == "Sobre":
    col1, col2 = st.columns([0.9, 1.1])

    with col1:
        st.image(IMG_BLEFARO, caption="Blink Clinic · Oculoplástica", use_container_width=True)

    with col2:
        st.markdown('<div class="section-label">Sobre a clínica</div>', unsafe_allow_html=True)
        st.header("Cuidar do olhar com precisão e naturalidade")

        st.write(
            """
            A Blink Clinic nasce com uma visão clara: oferecer cuidados diferenciados
            em oculoplástica, integrando conhecimento oftalmológico, sensibilidade
            estética e atenção às necessidades individuais de cada paciente.
            """
        )

        st.write("• Avaliação individualizada")
        st.write("• Abordagem funcional e estética")
        st.write("• Resultados naturais e discretos")
        st.write("• Comunicação clara com o paciente")
        st.write("• Planeamento terapêutico personalizado")

elif pagina == "Contactos":
    st.markdown('<div class="section-label">Marcação</div>', unsafe_allow_html=True)
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
        st.image(IMG_MARCACAO, caption="Blink Clinic · Contactos", use_container_width=True)
        st.subheader("Blink Clinic")
        st.write("Oculoplástica")
        st.write("Pálpebras · Vias lacrimais · Órbita")
        st.write("Contacto: a definir")
        st.write("Localização: a definir")

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="footer">Blink Clinic · Oculoplástica · Saúde e estética do olhar</div>',
    unsafe_allow_html=True
)
