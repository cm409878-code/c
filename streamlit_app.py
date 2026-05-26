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
        font-size: 60px;
        letter-spacing: 8px;
        color: #062f3a;
        margin-bottom: 0;
    }

    .brand-subtitle {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 26px;
        color: #b1843f;
        font-style: italic;
        margin-top: -5px;
    }

    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 25px 0 38px 0;
    }

    .section-label {
        color: #b1843f;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 800;
        font-size: 13px;
    }

    .note {
        background: rgba(255, 255, 255, 0.82);
        border-left: 5px solid #b1843f;
        padding: 18px 22px;
        border-radius: 16px;
        margin-top: 18px;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #062f3a 0%, #b1843f 100%);
        color: white;
        border-radius: 999px;
        padding: 0.75rem 1.5rem;
        border: none;
        font-weight: 700;
    }

    img {
        border-radius: 22px;
        border: 1px solid rgba(177, 132, 63, 0.35);
        box-shadow: 0 10px 25px rgba(90, 65, 30, 0.12);
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
st.sidebar.caption("Oculoplástica · Saúde e estética do olhar")

pagina = st.sidebar.radio(
    "Menu",
    ["Início", "Serviços", "Galeria", "Sobre", "Contactos"]
)

st.sidebar.divider()
st.sidebar.subheader("Carregar imagens")

img_oculoplastica = st.sidebar.file_uploader("Imagem principal / Oculoplástica", type=["png", "jpg", "jpeg"])
img_blefaro = st.sidebar.file_uploader("Imagem Blefaroplastia", type=["png", "jpg", "jpeg"])
img_vias = st.sidebar.file_uploader("Imagem Vias Lacrimais", type=["png", "jpg", "jpeg"])
img_ptose = st.sidebar.file_uploader("Imagem Ptose Palpebral", type=["png", "jpg", "jpeg"])
img_estetica = st.sidebar.file_uploader("Imagem Estética Periocular", type=["png", "jpg", "jpeg"])


def mostrar_imagem(imagem, legenda, emoji="👁️"):
    if imagem is not None:
        st.image(imagem, caption=legenda, use_container_width=True)
    else:
        with st.container(border=True):
            st.markdown(f"## {emoji}")
            st.caption(f"Carrega a imagem para: {legenda}")


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
        mostrar_imagem(img_oculoplastica, "Oculoplástica", "👁️")

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        mostrar_imagem(img_blefaro, "Blefaroplastia", "👁️")
        st.subheader("Blefaroplastia")
        st.write("Cirurgia das pálpebras superiores e/ou inferiores, com objetivo funcional, estético ou combinado.")

    with c2:
        mostrar_imagem(img_vias, "Vias lacrimais", "💧")
        st.subheader("Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente, obstruções e alterações do sistema lacrimal.")

    with c3:
        mostrar_imagem(img_ptose, "Ptose palpebral", "👁️")
        st.subheader("Ptose palpebral")
        st.write("Avaliação da queda da pálpebra superior e do impacto funcional ou estético.")


elif pagina == "Serviços":
    st.markdown('<div class="section-label">Serviços médicos</div>', unsafe_allow_html=True)
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            mostrar_imagem(img_blefaro, "Blefaroplastia", "👁️")
            st.subheader("Blefaroplastia")
            st.write("Tratamento cirúrgico do excesso de pele e/ou bolsas palpebrais.")

        with st.container(border=True):
            mostrar_imagem(img_ptose, "Ptose palpebral", "👁️")
            st.subheader("Ptose palpebral")
            st.write("Correção da queda da pálpebra superior.")

        with st.container(border=True):
            st.subheader("Entrópio e Ectrópio")
            st.write("Correção de alterações da posição das pálpebras.")

    with col2:
        with st.container(border=True):
            mostrar_imagem(img_vias, "Vias lacrimais", "💧")
            st.subheader("Vias lacrimais")
            st.write("Avaliação de lacrimejo persistente e obstruções lacrimais.")

        with st.container(border=True):
            mostrar_imagem(img_oculoplastica, "Lesões palpebrais", "👁️")
            st.subheader("Lesões palpebrais")
            st.write("Avaliação, diagnóstico e eventual remoção de lesões nas pálpebras.")

        with st.container(border=True):
            mostrar_imagem(img_estetica, "Estética periocular", "✨")
            st.subheader("Estética periocular")
            st.write("Abordagem médica da estética do olhar com naturalidade e segurança.")


elif pagina == "Galeria":
    st.markdown('<div class="section-label">Imagens clínicas e educativas</div>', unsafe_allow_html=True)
    st.header("Galeria de Oculoplástica")

    g1, g2, g3 = st.columns(3)

    with g1:
        mostrar_imagem(img_oculoplastica, "Oculoplástica", "👁️")
        mostrar_imagem(img_blefaro, "Blefaroplastia", "👁️")

    with g2:
        mostrar_imagem(img_vias, "Vias lacrimais", "💧")
        mostrar_imagem(img_ptose, "Ptose palpebral", "👁️")

    with g3:
        mostrar_imagem(img_estetica, "Estética periocular", "✨")


elif pagina == "Sobre":
    col1, col2 = st.columns([0.9, 1.1])

    with col1:
        mostrar_imagem(img_oculoplastica, "Blink Clinic · Oculoplástica", "👁️")

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
                    "Entrópio / Ectrópio",
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
        mostrar_imagem(img_estetica, "Blink Clinic · Contactos", "✨")
        with st.container(border=True):
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
