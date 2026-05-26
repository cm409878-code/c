import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# FOTOGRAFIAS / IMAGENS REAIS POR LINK
IMG_HERO = "https://commons.wikimedia.org/wiki/Special:FilePath/Eyelid%20surgery%20outline.jpg"
IMG_BLEFARO = "https://eyewiki.org/w/images/thumb/9/9f/Lower_blepharoplasty_pre_post.jpg/700px-Lower_blepharoplasty_pre_post.jpg"
IMG_PTOSE = "https://commons.wikimedia.org/wiki/Special:FilePath/Congenitalptosis.JPG"
IMG_PTOSE_ANTES_DEPOIS = "https://www.oculofacialsociety.org/wp-content/uploads/2020/06/ptosis-correction-before-after.jpg"
IMG_VIAS = "https://commons.wikimedia.org/wiki/Special:FilePath/Tear%20system.svg"
IMG_OCULOPLASTICA = "https://commons.wikimedia.org/wiki/Special:FilePath/Upper%20eyelid%20blepharoplasty%20incision.png"

st.markdown(
    """
    <style>
    .stApp {
        background: #f8f6f2;
        color: #132f3a;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #022c35 0%, #033845 55%, #0a1f27 100%);
        border-right: 1px solid rgba(212, 170, 84, 0.22);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .block-container {
        padding-top: 1.6rem;
        padding-left: 2.8rem;
        padding-right: 2.8rem;
        max-width: 1600px;
    }

    h1, h2, h3, h4 {
        font-family: Georgia, "Times New Roman", serif;
        color: #102c36;
    }

    .brand-title {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 78px;
        letter-spacing: 7px;
        color: #102c36;
        margin-bottom: 0.2rem;
        line-height: 1;
    }

    .brand-subtitle {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        color: #ba8d3c;
        font-size: 26px;
        letter-spacing: 2px;
        margin-bottom: 1rem;
    }

    .gold-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #c59b4d, transparent);
        margin: 14px 0 28px 0;
    }

    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #c59b4d, transparent);
        margin: 28px 0 18px 0;
    }

    .hero-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 58px;
        line-height: 1.08;
        color: #102c36;
        margin-bottom: 20px;
    }

    .hero-text {
        font-size: 20px;
        line-height: 1.65;
        color: #2c3f46;
        margin-bottom: 24px;
    }

    .section-heading {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 22px;
        letter-spacing: 1px;
        color: #b1873e;
        text-align: center;
        margin-bottom: 8px;
        margin-top: 4px;
    }

    .service-text {
        font-size: 16px;
        line-height: 1.55;
        color: #25363c;
        margin-top: 8px;
    }

    img {
        border-radius: 18px !important;
        border: 1px solid rgba(197, 155, 77, 0.28);
        box-shadow: 0 12px 28px rgba(90, 65, 30, 0.10);
    }

    div.stButton > button {
        background: #063a48;
        color: white;
        border: none;
        border-radius: 18px;
        padding: 0.7rem 1.4rem;
        font-size: 18px;
        font-weight: 600;
        font-family: Georgia, serif;
    }

    div.stButton > button:hover {
        background: #0b4b5d;
        color: white;
        border: none;
    }

    .footer-text {
        text-align: center;
        color: #b1873e;
        font-family: Georgia, serif;
        font-size: 18px;
        letter-spacing: 2px;
        margin-top: 30px;
        margin-bottom: 10px;
    }

    .sidebar-logo {
        text-align: center;
        padding-top: 10px;
        padding-bottom: 12px;
    }

    .sidebar-logo-mark {
        font-size: 38px;
        color: #d6aa54;
        margin-bottom: 4px;
    }

    .sidebar-logo-title {
        font-family: Georgia, serif;
        font-size: 28px;
        color: #f7f4ea;
        letter-spacing: 2px;
        margin-bottom: 2px;
    }

    .sidebar-logo-sub {
        font-size: 15px;
        color: #d6aa54;
        letter-spacing: 2px;
    }

    .sidebar-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #d6aa54, transparent);
        margin: 12px 0 22px 0;
    }

    .quote-box {
        margin-top: 30px;
        border-top: 1px solid rgba(197, 155, 77, 0.35);
        padding-top: 26px;
        text-align: center;
        color: #f5e8cb;
        font-family: Georgia, serif;
        font-size: 20px;
        line-height: 1.5;
        font-style: italic;
    }

    .small-note {
        color: #33454c;
        font-size: 15px;
        line-height: 1.55;
    }

    @media (max-width: 900px) {
        .brand-title {
            font-size: 46px;
            letter-spacing: 4px;
        }

        .brand-subtitle {
            font-size: 18px;
        }

        .hero-title {
            font-size: 36px;
        }

        .hero-text {
            font-size: 17px;
        }

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div class="sidebar-logo">
        <div class="sidebar-logo-mark">👁️</div>
        <div class="sidebar-logo-title">BLINK CLINIC</div>
        <div class="sidebar-logo-sub">OCULOPLÁSTICA</div>
    </div>
    <div class="sidebar-divider"></div>
    """,
    unsafe_allow_html=True
)

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Início",
        "Serviços",
        "Sobre a Oculoplástica",
        "Galeria",
        "Informação Clínica",
        "Marcar Consulta",
        "Contactos",
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown(
    """
    <div class="quote-box">
        “Cuidamos do olhar<br>
        com precisão, segurança<br>
        e naturalidade.”
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="brand-title">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="brand-subtitle">OCULOPLÁSTICA &nbsp; · &nbsp; PÁLPEBRAS &nbsp; · &nbsp; VIAS LACRIMAIS &nbsp; · &nbsp; ÓRBITA</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

if pagina == "Início":
    col1, col2 = st.columns([1.02, 1])

    with col1:
        st.markdown(
            """
            <div class="hero-title">
                Precisão médica para<br>
                a saúde e estética do olhar
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="hero-text">
                A Blink Clinic é especializada no diagnóstico e tratamento
                das alterações das pálpebras, vias lacrimais, órbita
                e região periocular, com abordagem funcional e estética.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.button("📅  Marcar Consulta")

    with col2:
        st.image(IMG_HERO, caption="Marcação cirúrgica palpebral", use_container_width=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="section-heading">BLEFAROPLASTIA</div>', unsafe_allow_html=True)
        st.image(IMG_BLEFARO, caption="Blefaroplastia", use_container_width=True)
        st.markdown(
            """
            <div class="service-text">
                Cirurgia das pálpebras superiores e/ou inferiores
                para correção do excesso de pele, bolsas ou flacidez,
                com finalidade funcional, estética ou ambas.
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown('<div class="section-heading">VIAS LACRIMAIS</div>', unsafe_allow_html=True)
        st.image(IMG_VIAS, caption="Sistema lacrimal", use_container_width=True)
        st.markdown(
            """
            <div class="service-text">
                Avaliação e tratamento do lacrimejo persistente,
                obstruções das vias lacrimais e outras alterações
                do sistema lacrimal.
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown('<div class="section-heading">PTOSE PALPEBRAL</div>', unsafe_allow_html=True)
        st.image(IMG_PTOSE_ANTES_DEPOIS, caption="Ptose palpebral", use_container_width=True)
        st.markdown(
            """
            <div class="service-text">
                Correção da queda da pálpebra superior que pode
                interferir com a visão, a expressão facial
                e a simetria do olhar.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="footer-text">OCULOPLÁSTICA &nbsp; · &nbsp; SAÚDE E ESTÉTICA DO OLHAR</div>',
        unsafe_allow_html=True
    )

elif pagina == "Serviços":
    st.header("Serviços")

    col1, col2 = st.columns(2)

    with col1:
        st.image(IMG_BLEFARO, caption="Blefaroplastia", use_container_width=True)
        st.subheader("Blefaroplastia")
        st.write(
            """
            Procedimento cirúrgico que trata o excesso de pele e/ou bolsas nas
            pálpebras superiores e inferiores, podendo melhorar a função e a estética.
            """
        )

        st.image(IMG_PTOSE, caption="Ptose palpebral", use_container_width=True)
        st.subheader("Ptose palpebral")
        st.write(
            """
            Tratamento da queda da pálpebra superior, quando existe impacto visual,
            funcional ou estético.
            """
        )

    with col2:
        st.image(IMG_VIAS, caption="Vias lacrimais", use_container_width=True)
        st.subheader("Vias lacrimais")
        st.write(
            """
            Avaliação de obstruções, lacrimejo persistente e alterações do sistema
            de drenagem lacrimal.
            """
        )

        st.image(IMG_OCULOPLASTICA, caption="Oculoplástica", use_container_width=True)
        st.subheader("Estética periocular")
        st.write(
            """
            Tratamentos orientados para a harmonia do olhar e rejuvenescimento
            da região periocular, com naturalidade.
            """
        )

elif pagina == "Sobre a Oculoplástica":
    col1, col2 = st.columns([0.9, 1.1])

    with col1:
        st.image(IMG_OCULOPLASTICA, caption="Oculoplástica", use_container_width=True)

    with col2:
        st.header("Sobre a Oculoplástica")
        st.write(
            """
            A oculoplástica é uma área da oftalmologia dedicada ao diagnóstico
            e tratamento das estruturas que rodeiam o olho:
            pálpebras, vias lacrimais, órbita e região periocular.
            """
        )
        st.write(
            """
            Esta área pode abranger patologias funcionais e procedimentos estéticos,
            sempre com foco na segurança, na função visual e na naturalidade do resultado.
            """
        )

elif pagina == "Galeria":
    st.header("Galeria")

    g1, g2 = st.columns(2)

    with g1:
        st.image(IMG_HERO, caption="Marcação cirúrgica", use_container_width=True)
        st.image(IMG_VIAS, caption="Vias lacrimais", use_container_width=True)

    with g2:
        st.image(IMG_BLEFARO, caption="Blefaroplastia", use_container_width=True)
        st.image(IMG_PTOSE_ANTES_DEPOIS, caption="Ptose palpebral", use_container_width=True)

elif pagina == "Informação Clínica":
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        st.subheader("Quando procurar avaliação?")
        st.markdown(
            """
            <div class="small-note">
                Quando há queda das pálpebras, excesso de pele, lacrimejo,
                irritação ocular, assimetrias ou alterações do olhar.
            </div>
            """,
            unsafe_allow_html=True
        )

    with a2:
        st.subheader("O que pode afetar as pálpebras?")
        st.markdown(
            """
            <div class="small-note">
                Ptose palpebral, excesso de pele, bolsas, lesões palpebrais,
                entrópio, ectrópio e alterações estéticas da região periocular.
            </div>
            """,
            unsafe_allow_html=True
        )

    with a3:
        st.subheader("O que pode afetar as vias lacrimais?")
        st.markdown(
            """
            <div class="small-note">
                Obstruções, inflamações e alterações da drenagem da lágrima,
                que podem provocar lacrimejo persistente.
            </div>
            """,
            unsafe_allow_html=True
        )

elif pagina == "Marcar Consulta":
    st.header("Marcar Consulta")

    col1, col2 = st.columns([1, 1])

    with col1:
        nome = st.text_input("Nome")
        contacto = st.text_input("Contacto")
        motivo = st.selectbox(
            "Motivo da consulta",
            [
                "Consulta de Oculoplástica",
                "Blefaroplastia",
                "Ptose palpebral",
                "Vias lacrimais",
                "Estética periocular",
                "Outro",
            ]
        )
        mensagem = st.text_area("Mensagem")

        if st.button("Enviar pedido"):
            st.success("Pedido registado com sucesso.")

    with col2:
        st.image(IMG_HERO, caption="Marcar consulta", use_container_width=True)

elif pagina == "Contactos":
    st.header("Contactos")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Blink Clinic")
        st.write("Oculoplástica")
        st.write("Pálpebras · Vias lacrimais · Órbita")
        st.write("Telefone: a definir")
        st.write("Email: a definir")
        st.write("Morada: a definir")

    with col2:
        st.image(IMG_HERO, caption="Blink Clinic", use_container_width=True)
