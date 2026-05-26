import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# ESTILO
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fbf7ef 0%, #fffdf8 50%, #f3e8d8 100%);
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

    div.stButton > button {
        background: #062f3a;
        color: white;
        border-radius: 999px;
        padding: 0.7rem 1.5rem;
        border: none;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background: #b1843f;
        color: white;
        border: none;
    }

    .titulo {
        text-align: center;
        font-family: Georgia, serif;
        font-size: 64px;
        letter-spacing: 8px;
        color: #062f3a;
        margin-bottom: 0;
    }

    .subtitulo {
        text-align: center;
        font-family: Georgia, serif;
        font-size: 28px;
        color: #b1843f;
        font-style: italic;
        margin-top: 0;
    }

    .linha {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 25px 0 40px 0;
    }

    .nota {
        background: rgba(255,255,255,0.75);
        border-left: 5px solid #b1843f;
        padding: 18px;
        border-radius: 14px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# MENU
st.sidebar.title("BLINK CLINIC")
pagina = st.sidebar.radio(
    "Menu",
    ["Início", "Serviços", "Sobre", "Contactos"]
)

# CABEÇALHO
st.markdown('<div class="titulo">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Oculoplástica · Saúde e estética do olhar</div>', unsafe_allow_html=True)
st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

# PÁGINA INÍCIO
if pagina == "Início":
    col1, col2 = st.columns([1.2, 0.8])

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
            A abordagem combina rigor médico, segurança clínica,
            naturalidade e atenção à harmonia do olhar.
            """
        )

        st.button("Marcar Consulta")

        st.markdown(
            """
            <div class="nota">
            Cuidado especializado em blefaroplastia, ptose palpebral,
            vias lacrimais, lesões palpebrais e estética periocular.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1511499767150-a48a237f0083",
            caption="Blink Clinic · Oculoplástica",
            use_container_width=True
        )

    st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.subheader("👁️ Pálpebras")
            st.write("Blefaroplastia, ptose palpebral, entrópio, ectrópio e lesões palpebrais.")

    with c2:
        with st.container(border=True):
            st.subheader("💧 Vias lacrimais")
            st.write("Avaliação de lacrimejo persistente e obstrução das vias lacrimais.")

    with c3:
        with st.container(border=True):
            st.subheader("✨ Estética periocular")
            st.write("Abordagem médica da estética do olhar com naturalidade e segurança.")

# PÁGINA SERVIÇOS
elif pagina == "Serviços":
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Blefaroplastia")
            st.write("Cirurgia das pálpebras superiores e/ou inferiores.")

        with st.container(border=True):
            st.subheader("Ptose palpebral")
            st.write("Tratamento da queda da pálpebra superior.")

        with st.container(border=True):
            st.subheader("Entrópio e ectrópio")
            st.write("Correção de alterações da posição das pálpebras.")

    with col2:
        with st.container(border=True):
            st.subheader("Vias lacrimais")
            st.write("Avaliação e tratamento de lacrimejo e obstruções lacrimais.")

        with st.container(border=True):
            st.subheader("Lesões palpebrais")
            st.write("Avaliação e eventual remoção de lesões nas pálpebras.")

        with st.container(border=True):
            st.subheader("Estética periocular")
            st.write("Tratamentos médicos focados na harmonia do olhar.")

# PÁGINA SOBRE
elif pagina == "Sobre":
    col1, col2 = st.columns([0.8, 1.2])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1559757175-0eb30cd8c063",
            use_container_width=True
        )

    with col2:
        st.header("Sobre a Blink Clinic")
        st.write(
            """
            A Blink Clinic é uma clínica dedicada à oculoplástica,
            uma área da oftalmologia focada nas pálpebras, vias lacrimais,
            órbita e região periocular.
            """
        )

        st.write("• Avaliação individualizada")
        st.write("• Rigor médico")
        st.write("• Resultados naturais")
        st.write("• Comunicação clara")
        st.write("• Acompanhamento personalizado")

# PÁGINA CONTACTOS
elif pagina == "Contactos":
    st.header("Marcar Consulta")

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

st.markdown('<div class="linha"></div>', unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#8a6a38; font-family:Georgia, serif; font-size:20px;'>Blink Clinic · Oculoplástica · Saúde e estética do olhar</p>",
    unsafe_allow_html=True
)
