import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# =========================
# ESTILO
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(196, 157, 82, 0.15), transparent 25%),
            radial-gradient(circle at top right, rgba(218, 168, 135, 0.14), transparent 28%),
            linear-gradient(135deg, #fbf7ef 0%, #fffdf8 50%, #f4eadc 100%);
        color: #062f3a;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #062f3a 0%, #123f49 65%, #8a6a38 100%);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 4rem;
        padding-right: 4rem;
        max-width: 1450px;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        color: #062f3a;
    }

    .brand-title {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 72px;
        letter-spacing: 10px;
        color: #062f3a;
        margin-bottom: 0;
        line-height: 1;
    }

    .brand-subtitle {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 27px;
        color: #b1843f;
        font-style: italic;
        margin-top: 8px;
    }

    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 28px 0 42px 0;
    }

    .section-label {
        color: #b1843f;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 800;
        font-size: 13px;
    }

    .hero-box {
        background: rgba(255,255,255,0.72);
        border: 1px solid rgba(177,132,63,0.32);
        border-radius: 32px;
        padding: 44px;
        box-shadow: 0 18px 40px rgba(90,65,30,0.10);
    }

    .hero-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 54px;
        line-height: 1.08;
        color: #062f3a;
        margin-bottom: 18px;
    }

    .hero-text {
        font-size: 19px;
        line-height: 1.7;
        color: #32474e;
    }

    .visual-card {
        background: linear-gradient(145deg, #07323d, #0e4b58);
        border-radius: 32px;
        padding: 40px;
        color: white;
        min-height: 360px;
        box-shadow: 0 22px 50px rgba(6,47,58,0.24);
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
        border: 1px solid rgba(214,170,84,0.35);
    }

    .visual-eye {
        font-size: 94px;
        color: #d6aa54;
        margin-bottom: 16px;
    }

    .visual-card h3 {
        color: white;
        font-size: 32px;
        margin-bottom: 10px;
    }

    .visual-card p {
        color: #f2ead8;
        font-size: 17px;
        line-height: 1.6;
    }

    .pill {
        display: inline-block;
        background: rgba(177,132,63,0.14);
        color: #062f3a;
        border: 1px solid rgba(177,132,63,0.35);
        padding: 8px 14px;
        border-radius: 999px;
        margin: 5px;
        font-weight: 700;
        font-size: 14px;
    }

    .service-card {
        background: rgba(255,255,255,0.84);
        border: 1px solid rgba(177,132,63,0.32);
        border-radius: 24px;
        padding: 26px;
        min-height: 260px;
        box-shadow: 0 12px 28px rgba(90,65,30,0.08);
        margin-bottom: 18px;
    }

    .service-icon {
        font-size: 42px;
        margin-bottom: 10px;
    }

    .service-card h3 {
        font-size: 25px;
        margin-top: 0;
        margin-bottom: 10px;
    }

    .service-card p {
        color: #34484d;
        line-height: 1.62;
        font-size: 16px;
    }

    .note {
        background: rgba(255,255,255,0.82);
        border-left: 5px solid #b1843f;
        padding: 20px 24px;
        border-radius: 18px;
        margin-top: 18px;
        box-shadow: 0 8px 22px rgba(90,65,30,0.08);
        color: #33484e;
        line-height: 1.6;
    }

    .metric-box {
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(177,132,63,0.28);
        border-radius: 24px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 12px 28px rgba(90,65,30,0.08);
    }

    .metric-number {
        font-size: 34px;
        font-weight: 900;
        color: #b1843f;
        font-family: Georgia, "Times New Roman", serif;
    }

    .metric-label {
        color: #062f3a;
        font-weight: 700;
        margin-top: 4px;
    }

    .footer {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        color: #8a6a38;
        font-size: 21px;
        font-style: italic;
        margin-top: 45px;
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

    @media (max-width: 900px) {
        .brand-title {
            font-size: 42px;
            letter-spacing: 5px;
        }

        .brand-subtitle {
            font-size: 20px;
        }

        .block-container {
            padding-left: 1.2rem;
            padding-right: 1.2rem;
        }

        .hero-title {
            font-size: 34px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# MENU
# =========================
st.sidebar.title("BLINK CLINIC")
st.sidebar.caption("Oculoplástica · Saúde e estética do olhar")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "O que é Oculoplástica",
        "Serviços",
        "Informação Clínica",
        "Marcar Consulta",
        "Contactos"
    ]
)

# =========================
# CABEÇALHO
# =========================
st.markdown('<div class="brand-title">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="brand-subtitle">Oculoplástica · Pálpebras · Vias Lacrimais · Órbita</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# INÍCIO
# =========================
if pagina == "Início":
    col1, col2 = st.columns([1.15, 0.85])

    with col1:
        st.markdown(
            """
            <div class="hero-box">
                <div class="section-label">Clínica de Oculoplástica</div>
                <div class="hero-title">
                    Precisão médica para a saúde e estética do olhar
                </div>
                <div class="hero-text">
                    A Blink Clinic dedica-se à avaliação e tratamento das estruturas perioculares:
                    pálpebras, vias lacrimais, órbita e região envolvente do olho.
                    <br><br>
                    A abordagem combina rigor médico, segurança clínica, naturalidade estética
                    e atenção à função visual.
                </div>
                <br>
                <span class="pill">Blefaroplastia</span>
                <span class="pill">Ptose palpebral</span>
                <span class="pill">Vias lacrimais</span>
                <span class="pill">Órbita</span>
                <span class="pill">Estética periocular</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.button("Marcar Consulta")

    with col2:
        st.markdown(
            """
            <div class="visual-card">
                <div class="visual-eye">👁️</div>
                <h3>Saúde e estética do olhar</h3>
                <p>
                    Uma abordagem médica especializada para proteger a função ocular,
                    melhorar o conforto e preservar a naturalidade da expressão.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown(
            """
            <div class="metric-box">
                <div class="metric-number">01</div>
                <div class="metric-label">Pálpebras</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m2:
        st.markdown(
            """
            <div class="metric-box">
                <div class="metric-number">02</div>
                <div class="metric-label">Vias Lacrimais</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m3:
        st.markdown(
            """
            <div class="metric-box">
                <div class="metric-number">03</div>
                <div class="metric-label">Órbita</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.header("Áreas principais")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">👁️</div>
                <h3>Blefaroplastia</h3>
                <p>
                    Tratamento do excesso de pele e/ou bolsas palpebrais,
                    com finalidade funcional, estética ou combinada.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">💧</div>
                <h3>Vias lacrimais</h3>
                <p>
                    Avaliação de lacrimejo persistente, obstruções e alterações
                    do sistema de drenagem da lágrima.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">✨</div>
                <h3>Estética periocular</h3>
                <p>
                    Abordagem médica da estética do olhar, respeitando anatomia,
                    função palpebral e naturalidade facial.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# O QUE É OCULOPLÁSTICA
# =========================
elif pagina == "O que é Oculoplástica":
    col1, col2 = st.columns([0.9, 1.1])

    with col1:
        st.markdown(
            """
            <div class="visual-card">
                <div class="visual-eye">👁️</div>
                <h3>Oculoplástica</h3>
                <p>
                    Área da oftalmologia dedicada às pálpebras,
                    vias lacrimais, órbita e região periocular.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.header("O que é a Oculoplástica?")
        st.write(
            """
            A oculoplástica é uma área da oftalmologia dedicada ao diagnóstico
            e tratamento das estruturas que rodeiam e protegem o olho.
            """
        )
        st.write(
            """
            Inclui alterações das pálpebras, da órbita, das vias lacrimais
            e da região periocular. Pode ter objetivos funcionais, estéticos
            ou uma combinação dos dois.
            """
        )
        st.markdown(
            """
            <div class="note">
                A região periocular é delicada: protege o olho, participa na lubrificação,
                contribui para a qualidade da visão e tem grande impacto na expressão facial.
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# SERVIÇOS
# =========================
elif pagina == "Serviços":
    st.header("Serviços de Oculoplástica")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">👁️</div>
                <h3>Blefaroplastia superior e inferior</h3>
                <p>
                    Tratamento cirúrgico do excesso de pele nas pálpebras superiores
                    e/ou bolsas das pálpebras inferiores. Pode ter finalidade estética,
                    funcional ou ambas.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">⬇️</div>
                <h3>Ptose palpebral</h3>
                <p>
                    Correção da queda da pálpebra superior quando interfere com a visão,
                    a simetria facial ou a expressão do olhar.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">↔️</div>
                <h3>Entrópio e Ectrópio</h3>
                <p>
                    Correção de alterações da posição das pálpebras que podem causar
                    irritação ocular, lacrimejo ou exposição da superfície ocular.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">💧</div>
                <h3>Vias lacrimais e epífora</h3>
                <p>
                    Avaliação de lacrimejo excessivo, obstruções e alterações
                    associadas à drenagem da lágrima.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">🔬</div>
                <h3>Lesões palpebrais</h3>
                <p>
                    Observação, diagnóstico, acompanhamento e eventual remoção
                    de lesões benignas ou suspeitas localizadas nas pálpebras.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">✨</div>
                <h3>Estética periocular</h3>
                <p>
                    Tratamentos focados na harmonia do olhar, respeitando anatomia,
                    função palpebral e naturalidade facial.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# INFORMAÇÃO CLÍNICA
# =========================
elif pagina == "Informação Clínica":
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">📍</div>
                <h3>Quando procurar avaliação?</h3>
                <p>
                    Quando há queda das pálpebras, excesso de pele, lacrimejo,
                    irritação ocular, assimetrias ou alterações do olhar.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a2:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">👁️</div>
                <h3>O que pode afetar as pálpebras?</h3>
                <p>
                    Ptose, excesso de pele, bolsas, lesões palpebrais,
                    entrópio, ectrópio e alterações estéticas da região periocular.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a3:
        st.markdown(
            """
            <div class="service-card">
                <div class="service-icon">💧</div>
                <h3>O que pode afetar as vias lacrimais?</h3>
                <p>
                    Obstruções, inflamações e alterações da drenagem da lágrima,
                    que podem provocar lacrimejo persistente.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# MARCAR CONSULTA
# =========================
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
        st.markdown(
            """
            <div class="visual-card">
                <div class="visual-eye">📅</div>
                <h3>Pedido de marcação</h3>
                <p>
                    Esta área pode ser ligada futuramente a email,
                    WhatsApp ou sistema de marcação online.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# CONTACTOS
# =========================
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
        st.markdown(
            """
            <div class="visual-card">
                <div class="visual-eye">👁️</div>
                <h3>Blink Clinic</h3>
                <p>
                    Saúde, função e estética do olhar com precisão,
                    segurança e naturalidade.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="footer">Blink Clinic · Oculoplástica · Saúde e estética do olhar</div>',
    unsafe_allow_html=True
)
