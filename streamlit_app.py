import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# =========================
# CSS PREMIUM
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(212, 170, 84, 0.16), transparent 28%),
            radial-gradient(circle at top right, rgba(214, 170, 84, 0.12), transparent 30%),
            linear-gradient(135deg, #fbf7ef 0%, #fffdf8 46%, #f3eadc 100%);
        color: #082f3a;
    }

    [data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #021f27 0%, #063946 48%, #08242c 100%);
        border-right: 1px solid rgba(214,170,84,0.35);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .block-container {
        padding-top: 1.6rem;
        padding-left: 3.2rem;
        padding-right: 3.2rem;
        max-width: 1500px;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        color: #082f3a;
    }

    .brand {
        text-align: center;
        margin-bottom: 8px;
    }

    .brand-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 76px;
        letter-spacing: 10px;
        color: #082f3a;
        line-height: 1;
    }

    .brand-subtitle {
        font-family: Georgia, "Times New Roman", serif;
        color: #b78735;
        font-size: 24px;
        letter-spacing: 3px;
        margin-top: 12px;
    }

    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b78735, transparent);
        margin: 20px 0 38px 0;
    }

    .hero {
        background:
            linear-gradient(135deg, rgba(255,255,255,0.86), rgba(255,250,241,0.92));
        border: 1px solid rgba(183,135,53,0.35);
        border-radius: 34px;
        padding: 42px;
        box-shadow: 0 22px 55px rgba(49,32,8,0.12);
        margin-bottom: 34px;
    }

    .hero-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 58px;
        line-height: 1.08;
        color: #082f3a;
        margin-bottom: 22px;
    }

    .hero-text {
        font-size: 19px;
        line-height: 1.7;
        color: #33484e;
        max-width: 680px;
    }

    .eyebrow {
        color: #b78735;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 13px;
        font-weight: 800;
        margin-bottom: 14px;
    }

    .premium-button {
        display: inline-block;
        margin-top: 24px;
        background: linear-gradient(135deg, #062f3a, #0d4c59);
        color: white;
        padding: 14px 24px;
        border-radius: 999px;
        font-weight: 800;
        box-shadow: 0 12px 26px rgba(6,47,58,0.25);
    }

    .tag {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        margin: 5px 5px 0 0;
        background: rgba(183,135,53,0.12);
        border: 1px solid rgba(183,135,53,0.35);
        color: #082f3a;
        font-weight: 700;
        font-size: 14px;
    }

    .visual-frame {
        background: linear-gradient(145deg, #07323d, #0d4c59);
        border: 1px solid rgba(214,170,84,0.45);
        border-radius: 32px;
        padding: 18px;
        box-shadow: 0 24px 60px rgba(6,47,58,0.24);
    }

    .section-title {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 30px;
        letter-spacing: 6px;
        color: #b78735;
        margin: 38px 0 30px 0;
    }

    .service-card {
        background: rgba(255,255,255,0.90);
        border: 1px solid rgba(183,135,53,0.32);
        border-radius: 28px;
        box-shadow: 0 18px 42px rgba(49,32,8,0.10);
        overflow: hidden;
        min-height: 520px;
        margin-bottom: 20px;
    }

    .service-body {
        padding: 24px 26px 28px 26px;
        text-align: center;
    }

    .service-icon {
        width: 68px;
        height: 68px;
        border-radius: 999px;
        margin: -46px auto 18px auto;
        background: linear-gradient(135deg, #062f3a, #0d4c59);
        border: 2px solid #d6aa54;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 30px;
        position: relative;
        z-index: 2;
        box-shadow: 0 10px 20px rgba(6,47,58,0.25);
    }

    .service-card h3 {
        font-size: 24px;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }

    .service-card p {
        color: #33484e;
        font-size: 16px;
        line-height: 1.62;
    }

    .lux-band {
        background: linear-gradient(90deg, #062f3a, #0b4654, #062f3a);
        border-radius: 32px;
        padding: 36px 44px;
        margin: 36px 0;
        color: white;
        border: 1px solid rgba(214,170,84,0.35);
        box-shadow: 0 22px 55px rgba(6,47,58,0.20);
    }

    .lux-band h2 {
        color: #d6aa54;
        letter-spacing: 4px;
        font-size: 34px;
    }

    .lux-band p {
        color: #f5ead3;
        font-size: 17px;
        line-height: 1.65;
    }

    .feature-card {
        background: rgba(255,255,255,0.86);
        border: 1px solid rgba(183,135,53,0.32);
        border-radius: 24px;
        padding: 26px;
        min-height: 230px;
        box-shadow: 0 14px 32px rgba(49,32,8,0.08);
    }

    .feature-card h3 {
        font-size: 23px;
    }

    .feature-card p {
        color: #33484e;
        line-height: 1.62;
    }

    .footer {
        text-align: center;
        color: #b78735;
        font-family: Georgia, "Times New Roman", serif;
        letter-spacing: 4px;
        font-size: 17px;
        margin: 38px 0 12px 0;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #062f3a 0%, #b78735 100%);
        color: white;
        border: none;
        border-radius: 999px;
        padding: 0.8rem 1.6rem;
        font-weight: 800;
    }

    div.stButton > button:hover {
        background: #b78735;
        color: white;
        border: none;
    }

    @media (max-width: 900px) {
        .brand-title {
            font-size: 42px;
            letter-spacing: 5px;
        }

        .brand-subtitle {
            font-size: 17px;
        }

        .hero-title {
            font-size: 36px;
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

# =========================
# IMAGENS SVG PREMIUM
# =========================
def svg_hero():
    return """
    <svg viewBox="0 0 1000 620" width="100%" height="440" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="skinHero" x1="0" x2="1">
                <stop offset="0" stop-color="#f7c9a7"/>
                <stop offset="1" stop-color="#e2a17a"/>
            </linearGradient>
            <radialGradient id="irisHero" cx="50%" cy="50%" r="50%">
                <stop offset="0" stop-color="#e8f7f7"/>
                <stop offset="0.45" stop-color="#6daab1"/>
                <stop offset="1" stop-color="#123c46"/>
            </radialGradient>
        </defs>

        <rect width="1000" height="620" rx="28" fill="#fff8ec"/>
        <rect width="1000" height="620" rx="28" fill="url(#skinHero)" opacity="0.9"/>
        <circle cx="820" cy="100" r="160" fill="#fff" opacity="0.18"/>
        <circle cx="150" cy="560" r="190" fill="#fff" opacity="0.18"/>

        <ellipse cx="535" cy="300" rx="310" ry="145" fill="#f1c2a1" opacity="0.65"/>
        <path d="M170 300 C300 135, 770 135, 900 300 C770 465, 300 465, 170 300 Z"
              fill="white" stroke="#082f3a" stroke-width="10"/>
        <circle cx="540" cy="300" r="92" fill="url(#irisHero)" stroke="#082f3a" stroke-width="7"/>
        <circle cx="540" cy="300" r="40" fill="#071d24"/>
        <circle cx="505" cy="260" r="16" fill="white"/>
        <circle cx="575" cy="330" r="8" fill="white" opacity="0.7"/>

        <path d="M280 185 C390 88, 695 90, 815 185"
              fill="none" stroke="#5b321a" stroke-width="28" stroke-linecap="round"/>
        <path d="M285 220 C405 155, 690 155, 805 220"
              fill="none" stroke="white" stroke-width="8" stroke-dasharray="20 18"/>
        <path d="M300 430 C420 485, 680 485, 790 430"
              fill="none" stroke="white" stroke-width="8" stroke-dasharray="20 18"/>

        <path d="M865 88 C935 130, 975 210, 990 300" fill="none" stroke="#f5f3ec" stroke-width="42" stroke-linecap="round"/>
        <path d="M116 525 C170 405, 250 340, 365 315" fill="none" stroke="#111" stroke-width="12" stroke-linecap="round"/>
        <path d="M365 315 L435 286" stroke="#111" stroke-width="8" stroke-linecap="round"/>
        <circle cx="435" cy="286" r="10" fill="#111"/>
    </svg>
    """

def svg_blefaro():
    return """
    <svg viewBox="0 0 900 520" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <radialGradient id="irisB" cx="50%" cy="50%" r="50%">
                <stop offset="0" stop-color="#effafa"/>
                <stop offset="0.45" stop-color="#68aab0"/>
                <stop offset="1" stop-color="#143d47"/>
            </radialGradient>
        </defs>
        <rect width="900" height="520" fill="#fff2e5"/>
        <ellipse cx="450" cy="250" rx="315" ry="150" fill="#f0c4a6"/>
        <path d="M115 255 C245 120, 655 120, 785 255 C655 390, 245 390, 115 255 Z"
              fill="white" stroke="#102c36" stroke-width="8"/>
        <circle cx="450" cy="255" r="82" fill="url(#irisB)" stroke="#102c36" stroke-width="6"/>
        <circle cx="450" cy="255" r="36" fill="#0b2f3a"/>
        <circle cx="420" cy="222" r="14" fill="white"/>
        <path d="M225 145 C340 65, 570 70, 685 145"
              fill="none" stroke="#5b321a" stroke-width="22" stroke-linecap="round"/>
        <path d="M230 184 C340 120, 565 120, 675 184"
              fill="none" stroke="#1b1b1b" stroke-width="7" stroke-dasharray="17 15"/>
        <path d="M245 365 C350 410, 555 410, 660 365"
              fill="none" stroke="#1b1b1b" stroke-width="7" stroke-dasharray="17 15"/>
    </svg>
    """

def svg_vias():
    return """
    <svg viewBox="0 0 900 520" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <radialGradient id="irisV" cx="50%" cy="50%" r="50%">
                <stop offset="0" stop-color="#effafa"/>
                <stop offset="0.45" stop-color="#68aab0"/>
                <stop offset="1" stop-color="#143d47"/>
            </radialGradient>
        </defs>
        <rect width="900" height="520" fill="#fff2e5"/>
        <ellipse cx="420" cy="250" rx="285" ry="140" fill="#f0c4a6"/>
        <path d="M125 255 C240 130, 620 130, 735 255 C620 380, 240 380, 125 255 Z"
              fill="white" stroke="#102c36" stroke-width="8"/>
        <circle cx="430" cy="255" r="76" fill="url(#irisV)" stroke="#102c36" stroke-width="6"/>
        <circle cx="430" cy="255" r="34" fill="#0b2f3a"/>
        <circle cx="405" cy="225" r="12" fill="white"/>
        <path d="M240 160 C345 85, 525 90, 635 160"
              fill="none" stroke="#5b321a" stroke-width="22" stroke-linecap="round"/>
        <circle cx="718" cy="240" r="14" fill="#d78754"/>
        <path d="M718 252 C780 305, 778 398, 700 445"
              fill="none" stroke="#d78754" stroke-width="14" stroke-linecap="round"/>
        <circle cx="700" cy="445" r="18" fill="#d78754"/>
        <path d="M795 170 C855 245, 855 335, 795 410 C735 335, 735 245, 795 170 Z"
              fill="#4b9bb5" opacity="0.9"/>
    </svg>
    """

def svg_ptose():
    return """
    <svg viewBox="0 0 900 520" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
        <rect width="900" height="520" fill="#fff2e5"/>
        <text x="240" y="70" text-anchor="middle" font-family="Georgia" font-size="34" fill="#102c36">ANTES</text>
        <text x="660" y="70" text-anchor="middle" font-family="Georgia" font-size="34" fill="#102c36">DEPOIS</text>

        <ellipse cx="240" cy="265" rx="170" ry="120" fill="#f0c4a6"/>
        <path d="M80 270 C145 195, 335 195, 400 270 C335 345, 145 345, 80 270 Z"
              fill="white" stroke="#102c36" stroke-width="7"/>
        <circle cx="240" cy="276" r="50" fill="#579ba2" stroke="#102c36" stroke-width="5"/>
        <circle cx="240" cy="276" r="23" fill="#0b2f3a"/>
        <rect x="85" y="170" width="310" height="105" rx="30" fill="#f0c4a6" opacity="0.85"/>
        <path d="M95 165 C165 115, 315 115, 385 165"
              fill="none" stroke="#5b321a" stroke-width="18" stroke-linecap="round"/>

        <ellipse cx="660" cy="265" rx="170" ry="120" fill="#f0c4a6"/>
        <path d="M500 270 C565 185, 755 185, 820 270 C755 355, 565 355, 500 270 Z"
              fill="white" stroke="#102c36" stroke-width="7"/>
        <circle cx="660" cy="270" r="50" fill="#579ba2" stroke="#102c36" stroke-width="5"/>
        <circle cx="660" cy="270" r="23" fill="#0b2f3a"/>
        <circle cx="640" cy="245" r="10" fill="white"/>
        <path d="M515 150 C585 100, 735 100, 805 150"
              fill="none" stroke="#5b321a" stroke-width="18" stroke-linecap="round"/>
    </svg>
    """

def svg_banner():
    return """
    <svg viewBox="0 0 1200 360" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <radialGradient id="eyeX" cx="50%" cy="50%" r="50%">
                <stop offset="0" stop-color="#e9f6f6"/>
                <stop offset="0.5" stop-color="#5d9ba1"/>
                <stop offset="1" stop-color="#143d47"/>
            </radialGradient>
        </defs>
        <rect width="1200" height="360" fill="#062f3a"/>
        <rect x="0" y="0" width="520" height="360" fill="#071d24"/>
        <path d="M40 180 C130 70, 390 70, 480 180 C390 290, 130 290, 40 180 Z"
              fill="white" opacity="0.88"/>
        <circle cx="260" cy="180" r="72" fill="url(#eyeX)"/>
        <circle cx="260" cy="180" r="34" fill="#071d24"/>
        <circle cx="235" cy="150" r="13" fill="white"/>
        <text x="610" y="128" font-family="Georgia" font-size="38" fill="#d6aa54" letter-spacing="5">OCULOPLÁSTICA</text>
        <text x="610" y="185" font-family="Arial" font-size="21" fill="#f5ead3">
            Área dedicada às pálpebras, vias lacrimais, órbita e região periocular.
        </text>
        <text x="610" y="230" font-family="Arial" font-size="21" fill="#f5ead3">
            Saúde, função e estética em harmonia.
        </text>
        <circle cx="1050" cy="180" r="85" fill="none" stroke="#d6aa54" stroke-width="3"/>
        <path d="M985 180 C1015 145, 1085 145, 1115 180 C1085 215, 1015 215, 985 180 Z"
              fill="none" stroke="#d6aa54" stroke-width="4"/>
        <circle cx="1050" cy="180" r="28" fill="none" stroke="#d6aa54" stroke-width="4"/>
    </svg>
    """

# =========================
# SIDEBAR
# =========================
st.sidebar.markdown("## 👁️ BLINK CLINIC")
st.sidebar.caption("OCULOPLÁSTICA")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "Serviços",
        "Sobre a Oculoplástica",
        "Galeria",
        "Informação Clínica",
        "Marcar Consulta",
        "Contactos"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div style="font-family:Georgia; font-size:20px; color:#f5ead3; text-align:center; line-height:1.6;">
    “Cuidamos do olhar<br>
    com precisão,<br>
    segurança<br>
    e naturalidade.”
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# HEADER
# =========================
st.markdown(
    """
    <div class="brand">
        <div class="brand-title">BLINK CLINIC</div>
        <div class="brand-subtitle">OCULOPLÁSTICA · PÁLPEBRAS · VIAS LACRIMAIS · ÓRBITA</div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# PAGES
# =========================
if pagina == "Início":
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.1])

    with col1:
        st.markdown('<div class="eyebrow">Clínica de Oculoplástica</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="hero-title">
            Precisão médica para<br>
            a saúde e estética do olhar
            </div>
            <div class="hero-text">
            A Blink Clinic é especializada no diagnóstico e tratamento das alterações das pálpebras,
            vias lacrimais, órbita e região periocular, com abordagem funcional e estética.
            </div>
            <div class="premium-button">📅 Marcar Consulta</div>
            <br><br>
            <span class="tag">Blefaroplastia</span>
            <span class="tag">Ptose palpebral</span>
            <span class="tag">Vias lacrimais</span>
            <span class="tag">Órbita</span>
            <span class="tag">Estética periocular</span>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown('<div class="visual-frame">' + svg_hero() + '</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">ÁREAS PRINCIPAIS</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="service-card">
                {svg_blefaro()}
                <div class="service-body">
                    <div class="service-icon">👁️</div>
                    <h3>BLEFAROPLASTIA</h3>
                    <p>Cirurgia das pálpebras superiores e/ou inferiores para correção do excesso de pele, bolsas ou flacidez.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="service-card">
                {svg_vias()}
                <div class="service-body">
                    <div class="service-icon">💧</div>
                    <h3>VIAS LACRIMAIS</h3>
                    <p>Avaliação e tratamento do lacrimejo persistente, obstruções e alterações do sistema lacrimal.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="service-card">
                {svg_ptose()}
                <div class="service-body">
                    <div class="service-icon">⬆️</div>
                    <h3>PTOSE PALPEBRAL</h3>
                    <p>Correção da queda da pálpebra superior que pode interferir com a visão, expressão facial e simetria.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="lux-band">
            {svg_banner()}
        </div>
        """,
        unsafe_allow_html=True
    )

elif pagina == "Serviços":
    st.header("Serviços em destaque")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(svg_blefaro(), unsafe_allow_html=True)
        st.subheader("Blefaroplastia")
        st.write("Tratamento cirúrgico do excesso de pele e/ou bolsas palpebrais, com finalidade funcional, estética ou ambas.")

        st.markdown(svg_ptose(), unsafe_allow_html=True)
        st.subheader("Ptose palpebral")
        st.write("Correção da queda da pálpebra superior, quando interfere com a visão ou a expressão facial.")

    with c2:
        st.markdown(svg_vias(), unsafe_allow_html=True)
        st.subheader("Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente e alterações da drenagem lacrimal.")

        st.markdown(svg_hero(), unsafe_allow_html=True)
        st.subheader("Estética periocular")
        st.write("Tratamentos focados na harmonia do olhar, respeitando anatomia e naturalidade.")

elif pagina == "Sobre a Oculoplástica":
    col1, col2 = st.columns([0.9, 1.1])

    with col1:
        st.markdown(svg_banner(), unsafe_allow_html=True)

    with col2:
        st.header("Sobre a Oculoplástica")
        st.write("A oculoplástica é uma área da oftalmologia dedicada ao diagnóstico e tratamento das estruturas que rodeiam o olho.")
        st.write("Inclui pálpebras, vias lacrimais, órbita e região periocular, com objetivos funcionais, estéticos ou ambos.")

elif pagina == "Galeria":
    st.header("Galeria visual")

    g1, g2 = st.columns(2)

    with g1:
        st.markdown(svg_hero(), unsafe_allow_html=True)
        st.markdown(svg_vias(), unsafe_allow_html=True)

    with g2:
        st.markdown(svg_blefaro(), unsafe_allow_html=True)
        st.markdown(svg_ptose(), unsafe_allow_html=True)

    st.markdown(svg_banner(), unsafe_allow_html=True)

elif pagina == "Informação Clínica":
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        st.markdown(
            """
            <div class="feature-card">
                <h3>Quando procurar avaliação?</h3>
                <p>Queda das pálpebras, excesso de pele, lacrimejo, irritação ocular, assimetrias ou alterações do olhar.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a2:
        st.markdown(
            """
            <div class="feature-card">
                <h3>O que pode afetar as pálpebras?</h3>
                <p>Ptose, excesso de pele, bolsas, lesões palpebrais, entrópio, ectrópio e alterações estéticas perioculares.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a3:
        st.markdown(
            """
            <div class="feature-card">
                <h3>Vias lacrimais</h3>
                <p>Alterações da drenagem da lágrima podem causar lacrimejo persistente, infeções e desconforto ocular.</p>
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
                "Outro"
            ]
        )
        mensagem = st.text_area("Mensagem")
        if st.button("Enviar pedido"):
            st.success("Pedido registado. Esta versão ainda não envia emails automaticamente.")

    with col2:
        st.markdown(svg_hero(), unsafe_allow_html=True)

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
        st.markdown(svg_banner(), unsafe_allow_html=True)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="footer">BLINK CLINIC · OCULOPLÁSTICA · SAÚDE E ESTÉTICA DO OLHAR</div>',
    unsafe_allow_html=True
)
