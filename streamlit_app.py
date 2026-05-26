import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background: #f8f5ef;
        color: #0b2f3a;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002f3a 0%, #063d49 55%, #071d24 100%);
        border-right: 1px solid rgba(205, 160, 72, 0.35);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .block-container {
        padding-top: 1.6rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1500px;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        color: #0b2f3a;
    }

    .brand-title {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 76px;
        letter-spacing: 8px;
        color: #0b2f3a;
        line-height: 1;
        margin-bottom: 0;
    }

    .brand-subtitle {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        color: #b78735;
        font-size: 24px;
        letter-spacing: 2px;
        margin-top: 10px;
        margin-bottom: 1rem;
    }

    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, #c79b49, transparent);
        margin: 18px 0 34px 0;
    }

    .hero-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 56px;
        line-height: 1.08;
        color: #0b2f3a;
        margin-bottom: 22px;
    }

    .hero-text {
        font-size: 19px;
        line-height: 1.65;
        color: #31464d;
        max-width: 700px;
    }

    .section-label {
        color: #b78735;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 13px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .section-title {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        color: #b78735;
        letter-spacing: 5px;
        font-size: 27px;
        margin: 20px 0 26px 0;
    }

    .visual-card {
        background: #fffaf2;
        border: 1px solid rgba(199,155,73,0.38);
        border-radius: 26px;
        box-shadow: 0 16px 35px rgba(68, 44, 13, 0.12);
        overflow: hidden;
        margin-bottom: 16px;
    }

    .service-card {
        background: white;
        border: 1px solid rgba(199,155,73,0.28);
        border-radius: 22px;
        box-shadow: 0 14px 32px rgba(68, 44, 13, 0.09);
        padding: 0 0 22px 0;
        overflow: hidden;
        min-height: 520px;
    }

    .service-card h3 {
        text-align: center;
        font-size: 24px;
        letter-spacing: 2px;
        margin: 18px 0 10px 0;
    }

    .service-card p {
        text-align: center;
        font-size: 16px;
        line-height: 1.55;
        color: #31464d;
        padding: 0 24px;
    }

    .icon-circle {
        width: 68px;
        height: 68px;
        background: #063d49;
        color: white;
        border-radius: 999px;
        margin: -34px auto 0 auto;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        border: 2px solid #c79b49;
        position: relative;
        z-index: 5;
    }

    .highlight-band {
        background: linear-gradient(90deg, #062f3a, #063d49);
        border-radius: 0;
        padding: 34px 42px;
        color: white;
        margin: 40px -3rem 40px -3rem;
        display: grid;
        grid-template-columns: 0.9fr 1.1fr 0.4fr;
        gap: 34px;
        align-items: center;
    }

    .highlight-band h2 {
        color: #d6aa54;
        letter-spacing: 4px;
        font-size: 32px;
    }

    .highlight-band p {
        font-size: 17px;
        line-height: 1.65;
        color: #f5ead3;
    }

    .feature-card {
        background: rgba(255,255,255,0.82);
        border: 1px solid rgba(199,155,73,0.35);
        padding: 24px;
        border-radius: 22px;
        min-height: 220px;
        box-shadow: 0 12px 28px rgba(68,44,13,0.08);
    }

    .feature-card h3 {
        font-size: 23px;
    }

    .feature-card p {
        color: #31464d;
        line-height: 1.6;
    }

    .footer {
        text-align: center;
        color: #b78735;
        font-family: Georgia, "Times New Roman", serif;
        letter-spacing: 3px;
        margin-top: 36px;
        font-size: 17px;
    }

    div.stButton > button {
        background: #063d49;
        color: white;
        border: none;
        border-radius: 14px;
        padding: 0.78rem 1.5rem;
        font-size: 17px;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background: #b78735;
        color: white;
        border: none;
    }

    @media (max-width: 900px) {
        .brand-title {
            font-size: 42px;
            letter-spacing: 4px;
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

        .highlight-band {
            grid-template-columns: 1fr;
            margin-left: -1rem;
            margin-right: -1rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# SVG IMAGES
# =========================
def svg_hero():
    return """
    <div class="visual-card">
    <svg viewBox="0 0 1000 540" width="100%" height="430" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="skin" x1="0" x2="1">
                <stop offset="0" stop-color="#f4c7a8"/>
                <stop offset="1" stop-color="#e7a982"/>
            </linearGradient>
            <radialGradient id="iris" cx="50%" cy="50%" r="50%">
                <stop offset="0" stop-color="#d6e8e9"/>
                <stop offset="0.45" stop-color="#4b8b93"/>
                <stop offset="1" stop-color="#123b45"/>
            </radialGradient>
        </defs>
        <rect width="1000" height="540" fill="#fffaf2"/>
        <rect x="0" y="0" width="1000" height="540" fill="url(#skin)" opacity="0.92"/>
        <path d="M0 0 H1000 V540 H0 Z" fill="#fffaf2" opacity="0.18"/>

        <ellipse cx="535" cy="255" rx="300" ry="138" fill="#f0bf9d" opacity="0.55"/>
        <path d="M190 255 C315 95, 760 95, 890 255 C760 415, 315 415, 190 255 Z"
              fill="white" stroke="#0b2f3a" stroke-width="9"/>
        <circle cx="540" cy="255" r="86" fill="url(#iris)" stroke="#0b2f3a" stroke-width="6"/>
        <circle cx="540" cy="255" r="37" fill="#071d24"/>
        <circle cx="510" cy="218" r="15" fill="white"/>
        <circle cx="570" cy="285" r="8" fill="white" opacity="0.7"/>

        <path d="M285 150 C395 60, 685 65, 800 150"
              fill="none" stroke="#5b321a" stroke-width="26" stroke-linecap="round"/>
        <path d="M290 180 C400 120, 690 120, 795 180"
              fill="none" stroke="white" stroke-width="7" stroke-dasharray="18 18"/>
        <path d="M300 375 C410 430, 675 430, 785 375"
              fill="none" stroke="white" stroke-width="7" stroke-dasharray="18 18"/>

        <path d="M820 80 C900 110, 960 180, 985 260" fill="none" stroke="#f2f2f2" stroke-width="36" stroke-linecap="round"/>
        <path d="M120 440 C160 350, 220 300, 320 285" fill="none" stroke="#111" stroke-width="12" stroke-linecap="round"/>
        <path d="M320 285 L395 252" stroke="#111" stroke-width="8" stroke-linecap="round"/>
        <circle cx="395" cy="252" r="10" fill="#111"/>
    </svg>
    </div>
    """

def svg_blefaro():
    return """
    <div class="visual-card">
    <svg viewBox="0 0 900 520" width="100%" height="270" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <radialGradient id="irisB" cx="50%" cy="50%" r="50%">
                <stop offset="0" stop-color="#e5f2f2"/>
                <stop offset="0.45" stop-color="#579ba2"/>
                <stop offset="1" stop-color="#143d47"/>
            </radialGradient>
        </defs>
        <rect width="900" height="520" fill="#fff2e5"/>
        <ellipse cx="450" cy="245" rx="310" ry="150" fill="#f0c4a6"/>
        <path d="M120 250 C245 120, 655 120, 780 250 C655 380, 245 380, 120 250 Z"
              fill="white" stroke="#102c36" stroke-width="8"/>
        <circle cx="450" cy="250" r="80" fill="url(#irisB)" stroke="#102c36" stroke-width="6"/>
        <circle cx="450" cy="250" r="36" fill="#0b2f3a"/>
        <circle cx="420" cy="218" r="14" fill="white"/>
        <path d="M230 145 C340 65, 565 70, 675 145"
              fill="none" stroke="#5b321a" stroke-width="22" stroke-linecap="round"/>
        <path d="M230 180 C340 120, 560 120, 675 180"
              fill="none" stroke="#1b1b1b" stroke-width="7" stroke-dasharray="17 15"/>
        <path d="M240 360 C350 405, 555 405, 665 360"
              fill="none" stroke="#1b1b1b" stroke-width="7" stroke-dasharray="17 15"/>
    </svg>
    </div>
    """

def svg_vias():
    return """
    <div class="visual-card">
    <svg viewBox="0 0 900 520" width="100%" height="270" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <radialGradient id="irisV" cx="50%" cy="50%" r="50%">
                <stop offset="0" stop-color="#e5f2f2"/>
                <stop offset="0.45" stop-color="#579ba2"/>
                <stop offset="1" stop-color="#143d47"/>
            </radialGradient>
        </defs>
        <rect width="900" height="520" fill="#fff2e5"/>
        <ellipse cx="430" cy="245" rx="280" ry="140" fill="#f0c4a6"/>
        <path d="M130 250 C240 130, 620 130, 730 250 C620 370, 240 370, 130 250 Z"
              fill="white" stroke="#102c36" stroke-width="8"/>
        <circle cx="430" cy="250" r="75" fill="url(#irisV)" stroke="#102c36" stroke-width="6"/>
        <circle cx="430" cy="250" r="34" fill="#0b2f3a"/>
        <circle cx="405" cy="222" r="12" fill="white"/>
        <path d="M245 160 C345 85, 520 90, 630 160"
              fill="none" stroke="#5b321a" stroke-width="22" stroke-linecap="round"/>
        <circle cx="718" cy="238" r="14" fill="#d78754"/>
        <path d="M718 250 C780 300, 778 395, 700 445"
              fill="none" stroke="#d78754" stroke-width="14" stroke-linecap="round"/>
        <circle cx="700" cy="445" r="18" fill="#d78754"/>
        <path d="M795 170 C855 245, 855 335, 795 410 C735 335, 735 245, 795 170 Z"
              fill="#4b9bb5" opacity="0.9"/>
    </svg>
    </div>
    """

def svg_ptose():
    return """
    <div class="visual-card">
    <svg viewBox="0 0 900 520" width="100%" height="270" xmlns="http://www.w3.org/2000/svg">
        <rect width="900" height="520" fill="#fff2e5"/>
        <text x="240" y="70" text-anchor="middle" font-family="Georgia" font-size="36" fill="#102c36">ANTES</text>
        <text x="660" y="70" text-anchor="middle" font-family="Georgia" font-size="36" fill="#102c36">DEPOIS</text>

        <ellipse cx="240" cy="260" rx="170" ry="120" fill="#f0c4a6"/>
        <path d="M80 265 C145 190, 335 190, 400 265 C335 340, 145 340, 80 265 Z"
              fill="white" stroke="#102c36" stroke-width="7"/>
        <circle cx="240" cy="270" r="50" fill="#579ba2" stroke="#102c36" stroke-width="5"/>
        <circle cx="240" cy="270" r="23" fill="#0b2f3a"/>
        <rect x="85" y="170" width="310" height="100" rx="30" fill="#f0c4a6" opacity="0.85"/>
        <path d="M95 165 C165 115, 315 115, 385 165"
              fill="none" stroke="#5b321a" stroke-width="18" stroke-linecap="round"/>

        <ellipse cx="660" cy="260" rx="170" ry="120" fill="#f0c4a6"/>
        <path d="M500 265 C565 180, 755 180, 820 265 C755 350, 565 350, 500 265 Z"
              fill="white" stroke="#102c36" stroke-width="7"/>
        <circle cx="660" cy="265" r="50" fill="#579ba2" stroke="#102c36" stroke-width="5"/>
        <circle cx="660" cy="265" r="23" fill="#0b2f3a"/>
        <circle cx="640" cy="240" r="10" fill="white"/>
        <path d="M515 150 C585 100, 735 100, 805 150"
              fill="none" stroke="#5b321a" stroke-width="18" stroke-linecap="round"/>
    </svg>
    </div>
    """

def svg_extra():
    return """
    <div class="visual-card">
    <svg viewBox="0 0 1200 360" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
        <rect width="1200" height="360" fill="#062f3a"/>
        <defs>
            <radialGradient id="eyeX" cx="50%" cy="50%" r="50%">
                <stop offset="0" stop-color="#e9f6f6"/>
                <stop offset="0.5" stop-color="#5d9ba1"/>
                <stop offset="1" stop-color="#143d47"/>
            </radialGradient>
        </defs>
        <rect x="0" y="0" width="520" height="360" fill="#071d24"/>
        <path d="M40 180 C130 70, 390 70, 480 180 C390 290, 130 290, 40 180 Z"
              fill="white" opacity="0.88"/>
        <circle cx="260" cy="180" r="72" fill="url(#eyeX)"/>
        <circle cx="260" cy="180" r="34" fill="#071d24"/>
        <circle cx="235" cy="150" r="13" fill="white"/>
        <text x="610" y="130" font-family="Georgia" font-size="38" fill="#d6aa54" letter-spacing="5">OCULOPLÁSTICA</text>
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
    </div>
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
st.markdown('<div class="brand-title">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="brand-subtitle">OCULOPLÁSTICA · PÁLPEBRAS · VIAS LACRIMAIS · ÓRBITA</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# PAGES
# =========================
if pagina == "Início":
    col1, col2 = st.columns([1, 1.1])

    with col1:
        st.markdown('<div class="section-label">Clínica de Oculoplástica</div>', unsafe_allow_html=True)
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
            A Blink Clinic é especializada no diagnóstico e tratamento das alterações das pálpebras,
            vias lacrimais, órbita e região periocular, com abordagem funcional e estética.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.button("📅 Marcar Consulta")

    with col2:
        st.markdown(svg_hero(), unsafe_allow_html=True)

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">ÁREAS PRINCIPAIS</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.markdown(svg_blefaro(), unsafe_allow_html=True)
        st.markdown('<div class="icon-circle">👁️</div>', unsafe_allow_html=True)
        st.markdown("<h3>BLEFAROPLASTIA</h3>", unsafe_allow_html=True)
        st.markdown("<p>Cirurgia das pálpebras superiores e/ou inferiores para correção do excesso de pele, bolsas ou flacidez.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.markdown(svg_vias(), unsafe_allow_html=True)
        st.markdown('<div class="icon-circle">💧</div>', unsafe_allow_html=True)
        st.markdown("<h3>VIAS LACRIMAIS</h3>", unsafe_allow_html=True)
        st.markdown("<p>Avaliação e tratamento do lacrimejo persistente, obstruções das vias lacrimais e alterações do sistema lacrimal.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.markdown(svg_ptose(), unsafe_allow_html=True)
        st.markdown('<div class="icon-circle">⬆️</div>', unsafe_allow_html=True)
        st.markdown("<h3>PTOSE PALPEBRAL</h3>", unsafe_allow_html=True)
        st.markdown("<p>Correção da queda da pálpebra superior que pode interferir com a visão, expressão facial e simetria.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(svg_extra(), unsafe_allow_html=True)

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
        st.markdown(svg_extra(), unsafe_allow_html=True)
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
    st.markdown(svg_extra(), unsafe_allow_html=True)

elif pagina == "Informação Clínica":
    st.header("Informação Clínica")
    a1, a2, a3 = st.columns(3)

    with a1:
        st.markdown('<div class="feature-card"><h3>Quando procurar avaliação?</h3><p>Queda das pálpebras, excesso de pele, lacrimejo, irritação ocular, assimetrias ou alterações do olhar.</p></div>', unsafe_allow_html=True)

    with a2:
        st.markdown('<div class="feature-card"><h3>O que pode afetar as pálpebras?</h3><p>Ptose, excesso de pele, bolsas, lesões palpebrais, entrópio, ectrópio e alterações estéticas perioculares.</p></div>', unsafe_allow_html=True)

    with a3:
        st.markdown('<div class="feature-card"><h3>Vias lacrimais</h3><p>Alterações da drenagem da lágrima podem causar lacrimejo persistente, infeções e desconforto ocular.</p></div>', unsafe_allow_html=True)

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
        st.markdown(svg_extra(), unsafe_allow_html=True)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">BLINK CLINIC · OCULOPLÁSTICA · SAÚDE E ESTÉTICA DO OLHAR</div>', unsafe_allow_html=True)
