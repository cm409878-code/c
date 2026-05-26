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
        background: linear-gradient(135deg, #fbf7ef 0%, #fffdf8 45%, #f4eadc 100%);
        color: #062f3a;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #062f3a 0%, #123f49 60%, #8a6a38 100%);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 4rem;
        padding-right: 4rem;
        max-width: 1400px;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        color: #062f3a;
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

    .brand-title {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 68px;
        letter-spacing: 10px;
        color: #062f3a;
        margin-bottom: 0px;
    }

    .brand-subtitle {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 28px;
        color: #b1843f;
        font-style: italic;
        margin-top: -8px;
    }

    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 26px 0 42px 0;
    }

    .section-label {
        color: #b1843f;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 800;
        font-size: 13px;
    }

    .card {
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid rgba(177, 132, 63, 0.35);
        border-radius: 22px;
        padding: 22px;
        box-shadow: 0 10px 28px rgba(90, 65, 30, 0.10);
        margin-bottom: 20px;
    }

    .soft-box {
        background: rgba(255, 255, 255, 0.78);
        border-left: 5px solid #b1843f;
        padding: 20px 24px;
        border-radius: 16px;
        color: #34484d;
        margin-top: 18px;
        box-shadow: 0 8px 24px rgba(90, 65, 30, 0.08);
    }

    .svg-wrap {
        background: #fffaf2;
        border: 1px solid rgba(177, 132, 63, 0.35);
        border-radius: 24px;
        padding: 12px;
        margin-bottom: 16px;
        box-shadow: 0 10px 26px rgba(90, 65, 30, 0.08);
    }

    .footer {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        color: #8a6a38;
        font-size: 22px;
        font-style: italic;
        margin-top: 45px;
    }

    [data-testid="stMetricValue"] {
        color: #b1843f;
    }

    @media (max-width: 900px) {
        .brand-title {
            font-size: 42px;
            letter-spacing: 5px;
        }

        .brand-subtitle {
            font-size: 22px;
        }

        .block-container {
            padding-left: 1.2rem;
            padding-right: 1.2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# DESENHOS / IMAGENS SVG
# =========================
def render_svg(svg):
    st.markdown(
        "<div class='svg-wrap'>" + svg + "</div>",
        unsafe_allow_html=True
    )


def svg_blefaroplastia():
    return """
    <svg viewBox="0 0 600 340" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
        <rect width="600" height="340" rx="26" fill="#fff7ed"/>
        <ellipse cx="300" cy="175" rx="190" ry="82" fill="#f3c7a6" opacity="0.55"/>
        <path d="M120 175 C185 92, 405 92, 480 175 C405 250, 190 250, 120 175 Z" fill="#ffffff" stroke="#062f3a" stroke-width="6"/>
        <circle cx="300" cy="175" r="54" fill="#1b6b78"/>
        <circle cx="300" cy="175" r="28" fill="#062f3a"/>
        <circle cx="282" cy="154" r="10" fill="#ffffff"/>
        <path d="M170 130 C230 82, 375 80, 430 130" fill="none" stroke="#5b3a1b" stroke-width="14" stroke-linecap="round"/>
        <path d="M172 142 C230 108, 374 108, 432 142" fill="none" stroke="#d8703b" stroke-width="6" stroke-dasharray="12 10"/>
        <path d="M172 220 C230 252, 374 252, 432 220" fill="none" stroke="#d8703b" stroke-width="6" stroke-dasharray="12 10"/>
        <g stroke="#d8703b" stroke-width="5" stroke-linecap="round">
            <path d="M205 105 L192 78"/><path d="M250 95 L243 65"/><path d="M300 92 L300 60"/>
            <path d="M350 96 L360 66"/><path d="M395 108 L415 82"/>
            <path d="M205 245 L192 272"/><path d="M250 255 L243 285"/><path d="M300 258 L300 290"/>
            <path d="M350 254 L360 284"/><path d="M395 242 L415 268"/>
        </g>
        <text x="300" y="320" text-anchor="middle" font-family="Georgia" font-size="22" fill="#8a6a38">
            Marcação pré-operatória de blefaroplastia
        </text>
    </svg>
    """


def svg_ptose():
    return """
    <svg viewBox="0 0 600 340" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
        <rect width="600" height="340" rx="26" fill="#fff7ed"/>
        <text x="150" y="45" text-anchor="middle" font-family="Georgia" font-size="24" fill="#062f3a">Antes</text>
        <text x="450" y="45" text-anchor="middle" font-family="Georgia" font-size="24" fill="#062f3a">Depois</text>

        <ellipse cx="150" cy="170" rx="110" ry="62" fill="#f3c7a6" opacity="0.55"/>
        <path d="M55 170 C95 118, 205 118, 245 170 C205 220, 95 220, 55 170 Z" fill="#fff" stroke="#062f3a" stroke-width="5"/>
        <path d="M65 142 C100 108, 200 108, 235 142" fill="none" stroke="#5b3a1b" stroke-width="12" stroke-linecap="round"/>
        <path d="M70 150 C120 138, 190 138, 230 150" fill="none" stroke="#d8703b" stroke-width="5" stroke-dasharray="10 8"/>
        <circle cx="150" cy="172" r="38" fill="#1b6b78"/>
        <circle cx="150" cy="172" r="18" fill="#062f3a"/>
        <rect x="55" y="118" width="190" height="50" fill="#f3c7a6" opacity="0.74"/>
        <text x="150" y="270" text-anchor="middle" font-family="Georgia" font-size="20" fill="#8a6a38">Ptose palpebral</text>

        <ellipse cx="450" cy="170" rx="110" ry="62" fill="#f3c7a6" opacity="0.55"/>
        <path d="M355 170 C395 118, 505 118, 545 170 C505 220, 395 220, 355 170 Z" fill="#fff" stroke="#062f3a" stroke-width="5"/>
        <path d="M365 128 C405 100, 495 100, 535 128" fill="none" stroke="#5b3a1b" stroke-width="12" stroke-linecap="round"/>
        <path d="M370 134 C420 112, 490 112, 530 134" fill="none" stroke="#d8703b" stroke-width="5" stroke-dasharray="10 8"/>
        <circle cx="450" cy="170" r="38" fill="#1b6b78"/>
        <circle cx="450" cy="170" r="18" fill="#062f3a"/>
        <circle cx="438" cy="156" r="7" fill="#fff"/>
        <text x="450" y="270" text-anchor="middle" font-family="Georgia" font-size="20" fill="#8a6a38">Correção palpebral</text>
    </svg>
    """


def svg_vias_lacrimais():
    return """
    <svg viewBox="0 0 600 340" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
        <rect width="600" height="340" rx="26" fill="#fff7ed"/>
        <path d="M120 160 C190 85, 360 85, 440 160 C360 235, 190 235, 120 160 Z" fill="#fff" stroke="#062f3a" stroke-width="6"/>
        <circle cx="280" cy="160" r="54" fill="#1b6b78"/>
        <circle cx="280" cy="160" r="25" fill="#062f3a"/>
        <circle cx="264" cy="144" r="8" fill="#fff"/>
        <path d="M170 116 C220 80, 330 78, 388 112" fill="none" stroke="#5b3a1b" stroke-width="13" stroke-linecap="round"/>
        <path d="M420 150 C475 170, 485 225, 440 270" fill="none" stroke="#d8703b" stroke-width="8" stroke-linecap="round"/>
        <path d="M438 270 C420 292, 380 292, 360 270" fill="none" stroke="#d8703b" stroke-width="8" stroke-linecap="round"/>
        <circle cx="420" cy="150" r="10" fill="#d8703b"/>
        <circle cx="438" cy="270" r="10" fill="#d8703b"/>
        <g fill="#1b6b78" opacity="0.85">
            <path d="M485 132 C505 160, 505 188, 485 210 C465 188, 465 160, 485 132 Z"/>
        </g>
        <text x="300" y="315" text-anchor="middle" font-family="Georgia" font-size="22" fill="#8a6a38">
            Avaliação das vias lacrimais
        </text>
    </svg>
    """


def svg_lesao_palpebral():
    return """
    <svg viewBox="0 0 600 340" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
        <rect width="600" height="340" rx="26" fill="#fff7ed"/>
        <ellipse cx="300" cy="170" rx="175" ry="80" fill="#f3c7a6" opacity="0.52"/>
        <path d="M130 170 C200 105, 400 105, 470 170 C400 235, 200 235, 130 170 Z" fill="#fff" stroke="#062f3a" stroke-width="6"/>
        <circle cx="300" cy="170" r="52" fill="#1b6b78"/>
        <circle cx="300" cy="170" r="25" fill="#062f3a"/>
        <circle cx="284" cy="154" r="9" fill="#fff"/>
        <path d="M175 120 C225 82, 375 82, 425 120" fill="none" stroke="#5b3a1b" stroke-width="14" stroke-linecap="round"/>
        <circle cx="395" cy="136" r="18" fill="#b1843f" opacity="0.9"/>
        <circle cx="395" cy="136" r="28" fill="none" stroke="#d8703b" stroke-width="5" stroke-dasharray="8 6"/>
        <path d="M430 95 L480 60" stroke="#d8703b" stroke-width="5" stroke-linecap="round"/>
        <path d="M480 60 L470 82" stroke="#d8703b" stroke-width="5" stroke-linecap="round"/>
        <path d="M480 60 L456 64" stroke="#d8703b" stroke-width="5" stroke-linecap="round"/>
        <text x="300" y="315" text-anchor="middle" font-family="Georgia" font-size="22" fill="#8a6a38">
            Lesão palpebral / avaliação médica
        </text>
    </svg>
    """


def svg_antes_depois():
    return """
    <svg viewBox="0 0 600 340" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
        <rect width="600" height="340" rx="26" fill="#fff7ed"/>
        <line x1="300" y1="45" x2="300" y2="285" stroke="#b1843f" stroke-width="2" opacity="0.7"/>
        <text x="150" y="45" text-anchor="middle" font-family="Georgia" font-size="24" fill="#062f3a">Antes</text>
        <text x="450" y="45" text-anchor="middle" font-family="Georgia" font-size="24" fill="#062f3a">Depois</text>

        <path d="M60 160 C105 110, 195 110, 240 160 C195 210, 105 210, 60 160 Z" fill="#fff" stroke="#062f3a" stroke-width="5"/>
        <circle cx="150" cy="160" r="38" fill="#1b6b78"/>
        <circle cx="150" cy="160" r="18" fill="#062f3a"/>
        <path d="M75 122 C115 94, 185 94, 225 122" fill="none" stroke="#5b3a1b" stroke-width="13" stroke-linecap="round"/>
        <path d="M88 208 C120 230, 180 230, 212 208" fill="none" stroke="#d8703b" stroke-width="5" stroke-dasharray="8 8"/>
        <path d="M96 222 C120 245, 180 245, 204 222" fill="none" stroke="#d8703b" stroke-width="4" opacity="0.7"/>

        <path d="M360 160 C405 110, 495 110, 540 160 C495 210, 405 210, 360 160 Z" fill="#fff" stroke="#062f3a" stroke-width="5"/>
        <circle cx="450" cy="160" r="38" fill="#1b6b78"/>
        <circle cx="450" cy="160" r="18" fill="#062f3a"/>
        <circle cx="438" cy="146" r="7" fill="#fff"/>
        <path d="M375 116 C415 90, 485 90, 525 116" fill="none" stroke="#5b3a1b" stroke-width="13" stroke-linecap="round"/>
        <path d="M390 208 C420 220, 480 220, 510 208" fill="none" stroke="#b1843f" stroke-width="4" opacity="0.5"/>
        <text x="300" y="315" text-anchor="middle" font-family="Georgia" font-size="22" fill="#8a6a38">
            Resultado natural e discreto
        </text>
    </svg>
    """


# =========================
# MENU
# =========================
st.sidebar.title("BLINK CLINIC")
st.sidebar.caption("Oculoplástica · Saúde do olhar")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "Serviços",
        "Galeria",
        "Sobre",
        "Informação Clínica",
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
        st.markdown('<div class="section-label">Clínica de Oculoplástica</div>', unsafe_allow_html=True)

        st.title("Precisão médica para a saúde e estética do olhar")

        st.write(
            """
            A Blink Clinic dedica-se à avaliação e tratamento das alterações das pálpebras,
            vias lacrimais, órbita e região periocular, combinando rigor médico,
            segurança clínica e atenção à harmonia estética.
            """
        )

        b1, b2 = st.columns(2)
        with b1:
            st.button("Marcar Consulta")
        with b2:
            st.button("Conhecer Serviços")

        st.markdown(
            """
            <div class="soft-box">
            Uma abordagem personalizada para cada paciente, com foco na função,
            naturalidade, discrição e acompanhamento cuidadoso.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        render_svg(svg_blefaroplastia())

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Especialidade", "Oculoplástica")

    with m2:
        st.metric("Foco", "Região periocular")

    with m3:
        st.metric("Abordagem", "Médica e estética")

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Áreas principais</div>', unsafe_allow_html=True)
    st.header("Cuidado especializado do olhar")

    c1, c2, c3 = st.columns(3)

    with c1:
        render_svg(svg_blefaroplastia())
        st.subheader("Pálpebras")
        st.write("Blefaroplastia, ptose, entrópio, ectrópio e lesões palpebrais.")

    with c2:
        render_svg(svg_vias_lacrimais())
        st.subheader("Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente e obstrução das vias lacrimais.")

    with c3:
        render_svg(svg_ptose())
        st.subheader("Ptose palpebral")
        st.write("Avaliação da queda da pálpebra superior e impacto funcional ou estético.")

# =========================
# SERVIÇOS
# =========================
elif pagina == "Serviços":
    st.markdown('<div class="section-label">Serviços médicos</div>', unsafe_allow_html=True)
    st.header("Serviços de Oculoplástica")

    s1, s2 = st.columns(2)

    with s1:
        render_svg(svg_blefaroplastia())
        st.subheader("01 · Blefaroplastia")
        st.write("Cirurgia das pálpebras superiores e/ou inferiores, com objetivo funcional, estético ou combinado.")

        render_svg(svg_ptose())
        st.subheader("02 · Ptose palpebral")
        st.write("Avaliação e tratamento da queda da pálpebra superior.")

    with s2:
        render_svg(svg_vias_lacrimais())
        st.subheader("03 · Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente e alterações da drenagem lacrimal.")

        render_svg(svg_lesao_palpebral())
        st.subheader("04 · Lesões palpebrais")
        st.write("Observação, diagnóstico e eventual remoção de lesões nas pálpebras.")

    st.markdown(
        """
        <div class="soft-box">
        Todos os procedimentos dependem de avaliação médica individual.
        A informação apresentada é geral e não substitui uma consulta.
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# GALERIA
# =========================
elif pagina == "Galeria":
    st.markdown('<div class="section-label">Imagens educativas</div>', unsafe_allow_html=True)
    st.header("Galeria de Oculoplástica")

    g1, g2 = st.columns(2)

    with g1:
        render_svg(svg_blefaroplastia())
        st.caption("Marcação de blefaroplastia")

        render_svg(svg_vias_lacrimais())
        st.caption("Vias lacrimais")

    with g2:
        render_svg(svg_ptose())
        st.caption("Ptose palpebral")

        render_svg(svg_antes_depois())
        st.caption("Antes e depois ilustrativo")

# =========================
# SOBRE
# =========================
elif pagina == "Sobre":
    col1, col2 = st.columns([0.9, 1.1])

    with col1:
        render_svg(svg_antes_depois())

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

# =========================
# INFORMAÇÃO CLÍNICA
# =========================
elif pagina == "Informação Clínica":
    st.markdown('<div class="section-label">Educação do paciente</div>', unsafe_allow_html=True)
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        render_svg(svg_blefaroplastia())
        st.subheader("O que é a Oculoplástica?")
        st.write("Área da oftalmologia dedicada às pálpebras, vias lacrimais, órbita e região periocular.")

    with a2:
        render_svg(svg_ptose())
        st.subheader("Quando procurar avaliação?")
        st.write("Quando há queda das pálpebras, excesso de pele, lacrimejo ou alterações do olhar.")

    with a3:
        render_svg(svg_vias_lacrimais())
        st.subheader("A consulta é essencial?")
        st.write("Sim. A decisão clínica depende sempre de observação médica e avaliação individual.")

# =========================
# CONTACTOS
# =========================
elif pagina == "Contactos":
    st.markdown('<div class="section-label">Marcação</div>', unsafe_allow_html=True)
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
                "Lesão palpebral",
                "Estética periocular",
                "Outro"
            ]
        )
        mensagem = st.text_area("Mensagem")

        if st.button("Enviar pedido"):
            st.success("Pedido registado. Esta versão ainda não envia emails automaticamente.")

    with col2:
        render_svg(svg_blefaroplastia())
        st.subheader("Blink Clinic")
        st.write("Oculoplástica")
        st.write("Pálpebras · Vias lacrimais · Órbita")
        st.write("Contacto: a definir")
        st.write("Localização: a definir")

st.markdown(
    '<div class="footer">Blink Clinic · Oculoplástica · Saúde e estética do olhar</div>',
    unsafe_allow_html=True
)
