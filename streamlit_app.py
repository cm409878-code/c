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

    .titulo {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 66px;
        letter-spacing: 8px;
        color: #062f3a;
        margin-bottom: 0;
    }

    .frase {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 27px;
        color: #b1843f;
        font-style: italic;
        margin-top: 10px;
    }

    .subtitulo {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 18px;
        color: #6f5a34;
        letter-spacing: 2px;
    }

    .linha {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 25px 0 38px 0;
    }

    .gratis-box {
        background: linear-gradient(135deg, #062f3a, #0e4b58);
        color: white;
        border-radius: 22px;
        padding: 22px 26px;
        margin: 22px 0;
        border: 1px solid rgba(177,132,63,0.55);
        box-shadow: 0 16px 34px rgba(6,47,58,0.18);
    }

    .gratis-box h3 {
        color: #d8b76d;
        margin-top: 0;
    }

    img {
        border-radius: 24px !important;
        border: 1px solid rgba(177,132,63,0.35);
        box-shadow: 0 14px 34px rgba(90,65,30,0.13);
    }

    div.stButton > button {
        background: linear-gradient(135deg, #062f3a 0%, #b1843f 100%);
        color: white;
        border-radius: 999px;
        padding: 0.75rem 1.5rem;
        border: none;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# MENU
st.sidebar.title("BLINK CLINIC")
st.sidebar.caption("Fotografias da clínica")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "A Clínica",
        "Galeria",
        "Serviços",
        "Marcar Consulta",
        "Contactos"
    ]
)

st.sidebar.divider()

foto_principal = st.sidebar.file_uploader(
    "1. Carregar fotografia principal",
    type=["png", "jpg", "jpeg"]
)

foto_rececao = st.sidebar.file_uploader(
    "2. Carregar fotografia da receção",
    type=["png", "jpg", "jpeg"]
)

foto_sala = st.sidebar.file_uploader(
    "3. Carregar fotografia da sala de espera",
    type=["png", "jpg", "jpeg"]
)

foto_consultorio = st.sidebar.file_uploader(
    "4. Carregar fotografia do consultório",
    type=["png", "jpg", "jpeg"]
)

foto_extra = st.sidebar.file_uploader(
    "5. Carregar fotografia extra",
    type=["png", "jpg", "jpeg"]
)


def mostrar_foto(foto, legenda):
    if foto is not None:
        st.image(foto, caption=legenda, use_container_width=True)
    else:
        st.info(f"Carrega uma fotografia na barra lateral para aparecer aqui: {legenda}")


# CABEÇALHO
st.markdown('<div class="titulo">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="frase">A arte de cuidar do olhar com precisão, segurança e naturalidade.</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitulo">Oculoplástica · Pálpebras · Vias Lacrimais · Órbita</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="linha"></div>', unsafe_allow_html=True)


if pagina == "Início":
    col1, col2 = st.columns([1, 1])

    with col1:
        st.title("Precisão médica para a saúde e estética do olhar")
        st.write(
            """
            A Blink Clinic é especializada no diagnóstico e tratamento das alterações
            das pálpebras, vias lacrimais, órbita e região periocular.
            """
        )

        st.write(
            """
            Uma abordagem médica, segura e personalizada, com foco na função,
            naturalidade e harmonia do olhar.
            """
        )

        st.button("Marcar Avaliação Gratuita")

        st.markdown(
            """
            <div class="gratis-box">
                <h3>Primeira avaliação gratuita</h3>
                <p>
                    Marca a tua primeira avaliação para conheceres a abordagem mais adequada
                    para o teu caso, sem compromisso inicial.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        mostrar_foto(foto_principal, "Blink Clinic · Fotografia principal")

    st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

    st.header("Serviços principais")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("Blefaroplastia")
        st.write("Cirurgia das pálpebras superiores e/ou inferiores.")

    with c2:
        st.subheader("Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente e obstruções lacrimais.")

    with c3:
        st.subheader("Ptose palpebral")
        st.write("Avaliação da queda da pálpebra superior.")


elif pagina == "A Clínica":
    st.header("A Clínica")

    col1, col2 = st.columns(2)

    with col1:
        mostrar_foto(foto_rececao, "Receção Blink Clinic")

    with col2:
        st.subheader("Um espaço pensado para cuidar do olhar")
        st.write(
            """
            A Blink Clinic foi pensada para transmitir conforto, sofisticação e segurança.
            A estética do espaço reflete a filosofia da clínica: detalhe, precisão e naturalidade.
            """
        )
        st.write("• Ambiente premium e acolhedor")
        st.write("• Consulta personalizada")
        st.write("• Foco em resultados naturais")
        st.write("• Acompanhamento próximo")

    st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        mostrar_foto(foto_sala, "Sala de espera")

    with col4:
        mostrar_foto(foto_consultorio, "Consultório")


elif pagina == "Galeria":
    st.header("Galeria da Clínica")

    g1, g2 = st.columns(2)

    with g1:
        mostrar_foto(foto_principal, "Fotografia principal")
        mostrar_foto(foto_sala, "Sala de espera")

    with g2:
        mostrar_foto(foto_rececao, "Receção")
        mostrar_foto(foto_consultorio, "Consultório")

    mostrar_foto(foto_extra, "Fotografia extra")


elif pagina == "Serviços":
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Blefaroplastia")
        st.write("Tratamento cirúrgico do excesso de pele e/ou bolsas palpebrais.")

        st.subheader("Ptose palpebral")
        st.write("Correção da queda da pálpebra superior.")

        st.subheader("Entrópio e Ectrópio")
        st.write("Correção de alterações da posição das pálpebras.")

    with col2:
        st.subheader("Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente e alterações da drenagem lacrimal.")

        st.subheader("Estética periocular")
        st.write("Tratamentos focados na harmonia do olhar, respeitando anatomia e naturalidade.")

        st.subheader("Lesões palpebrais")
        st.write("Avaliação, diagnóstico e eventual remoção de lesões localizadas nas pálpebras.")


elif pagina == "Marcar Consulta":
    st.header("Marcar Avaliação Gratuita")

    st.markdown(
        """
        <div class="gratis-box">
            <h3>Primeira avaliação gratuita</h3>
            <p>
                Preenche o formulário para pedir a tua primeira avaliação.
                Esta etapa serve para perceber o motivo da consulta e orientar o próximo passo.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        nome = st.text_input("Nome")
        contacto = st.text_input("Contacto")
        motivo = st.selectbox(
            "Motivo da avaliação",
            [
                "Consulta de Oculoplástica",
                "Blefaroplastia",
                "Ptose palpebral",
                "Vias lacrimais",
                "Estética periocular",
                "Outro"
            ]
        )
        mensagem = st.text_area("Mensagem")

        if st.button("Enviar pedido de avaliação gratuita"):
            st.success("Pedido registado. Esta versão ainda não envia emails automaticamente.")

    with col2:
        mostrar_foto(foto_rececao, "Blink Clinic · Avaliação gratuita")


elif pagina == "Contactos":
    st.header("Contactos")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Blink Clinic")
        st.write("Oculoplástica")
        st.write("Pálpebras · Vias lacrimais · Órbita")
        st.write("Primeira avaliação: gratuita")
        st.write("Telefone: a definir")
        st.write("Email: a definir")
        st.write("Morada: a definir")

    with col2:
        mostrar_foto(foto_extra, "Blink Clinic")


st.markdown('<div class="linha"></div>', unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#8a6a38; font-family:Georgia, serif; font-size:20px;'>Blink Clinic · Oculoplástica · Saúde e estética do olhar</p>",
    unsafe_allow_html=True
)
