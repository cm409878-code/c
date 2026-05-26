import streamlit as st
import streamlit.components.v1 as components

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
        background: linear-gradient(135deg, #fbf7ef 0%, #fffdf8 48%, #f4eadc 100%);
        color: #062f3a;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #022c35 0%, #033845 60%, #8a6a38 100%);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1500px;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        color: #062f3a;
    }

    .brand-title {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 68px;
        letter-spacing: 9px;
        color: #062f3a;
        margin-bottom: 0;
    }

    .brand-subtitle {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 25px;
        color: #b1843f;
        font-style: italic;
        margin-top: -5px;
    }

    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 24px 0 38px 0;
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

    .note {
        background: rgba(255, 255, 255, 0.82);
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

# =========================
# IMAGENS CRIADAS NO CÓDIGO
# =========================
def imagem_oculoplastica(titulo="Oculoplástica"):
    return f"""
    <div style="background:#fffaf2;border:1px solid #d6b36a;border-radius:24px;padding:16px;box-shadow:0 10px 26px rgba(90,65,30,0.12);">
    <svg viewBox="0 0 900 560" width="100%" height="360" xmlns="http://www.w3.org/2000/svg">
        <rect width="900" height="560" rx="30" fill="#fff7ed"/>
        <ellipse cx="450" cy="280" rx="300" ry="135" fill="#f0c4a6" opacity="0.55"/>
        <path d="M140 280 C250 150, 650 150, 760 280 C650 410, 250 410, 140 280 Z" fill="white" stroke="#062f3a" stroke-width="8"/>
        <circle cx="450" cy="280" r="78" fill="#1f6f7a" stroke="#062f3a" stroke-width="6"/>
        <circle cx="450" cy="280" r="35" fill="#062f3a"/>
        <circle cx="420" cy="245" r="14" fill="white"/>
        <path d="M230 185 C330 105, 570 105, 670 185" fill="none" stroke="#5b3a1e" stroke-width="22" stroke-linecap="round"/>
        <path d="M235 205 C330 155, 570 155, 665 205" fill="none" stroke="#d8703b" stroke-width="8" stroke-dasharray="18 14"/>
        <path d="M235 370 C330 415, 570 415, 665 370" fill="none" stroke="#d8703b" stroke-width="8" stroke-dasharray="18 14"/>
        <line x1="450" y1="85" x2="450" y2="475" stroke="#b1843f" stroke-width="4" opacity="0.7"/>
        <line x1="170" y1="280" x2="730" y2="280" stroke="#b1843f" stroke-width="4" opacity="0.7"/>
        <text x="450" y="520" text-anchor="middle" font-family="Georgia" font-size="32" fill="#8a6a38">{titulo}</text>
    </svg>
    </div>
    """

def imagem_blefaroplastia():
    return """
    <div style="background:#fffaf2;border:1px solid #d6b36a;border-radius:24px;padding:16px;box-shadow:0 10px 26px rgba(90,65,30,0.12);">
    <svg viewBox="0 0 900 560" width="100%" height="360" xmlns="http://www.w3.org/2000/svg">
        <rect width="900" height="560" rx="30" fill="#fff7ed"/>
        <ellipse cx="450" cy="280" rx="300" ry="135" fill="#f0c4a6" opacity="0.55"/>
        <path d="M140 280 C250 150, 650 150, 760 280 C650 410, 250 410, 140 280 Z" fill="white" stroke="#062f3a" stroke-width="8"/>
        <circle cx="450" cy="280" r="78" fill="#1f6f7a" stroke="#062f3a" stroke-width="6"/>
        <circle cx="450" cy="280" r="35" fill="#062f3a"/>
        <circle cx="420" cy="245" r="14" fill="white"/>
        <path d="M230 185 C330 105, 570 105, 670 185" fill="none" stroke="#5b3a1e" stroke-width="22" stroke-linecap="round"/>
        <path d="M240 210 C335 165, 565 165, 660 210" fill="none" stroke="#d8703b" stroke-width="10" stroke-dasharray="18 14"/>
        <path d="M245 365 C340 410, 560 410, 655 365" fill="none" stroke="#d8703b" stroke-width="10" stroke-dasharray="18 14"/>
        <g stroke="#d8703b" stroke-width="6" stroke-linecap="round">
            <line x1="285" y1="170" x2="265" y2="130"/>
            <line x1="355" y1="155" x2="345" y2="110"/>
            <line x1="450" y1="150" x2="450" y2="100"/>
            <line x1="545" y1="155" x2="555" y2="110"/>
            <line x1="615" y1="170" x2="640" y2="132"/>
        </g>
        <text x="450" y="520" text-anchor="middle" font-family="Georgia" font-size="32" fill="#8a6a38">Blefaroplastia · Marcação palpebral</text>
    </svg>
    </div>
    """

def imagem_vias_lacrimais():
    return """
    <div style="background:#fffaf2;border:1px solid #d6b36a;border-radius:24px;padding:16px;box-shadow:0 10px 26px rgba(90,65,30,0.12);">
    <svg viewBox="0 0 900 560" width="100%" height="360" xmlns="http://www.w3.org/2000/svg">
        <rect width="900" height="560" rx="30" fill="#fff7ed"/>
        <ellipse cx="420" cy="260" rx="270" ry="125" fill="#f0c4a6" opacity="0.50"/>
        <path d="M130 260 C240 140, 600 140, 710 260 C600 380, 240 380, 130 260 Z" fill="white" stroke="#062f3a" stroke-width="8"/>
        <circle cx="410" cy="260" r="70" fill="#1f6f7a" stroke="#062f3a" stroke-width="6"/>
        <circle cx="410" cy="260" r="32" fill="#062f3a"/>
        <circle cx="385" cy="232" r="12" fill="white"/>
        <path d="M230 175 C320 105, 510 105, 610 175" fill="none" stroke="#5b3a1e" stroke-width="22" stroke-linecap="round"/>
        <circle cx="705" cy="245" r="14" fill="#d8703b"/>
        <path d="M705 250 C760 290, 760 380, 690 430" fill="none" stroke="#d8703b" stroke-width="12" stroke-linecap="round"/>
        <circle cx="690" cy="430" r="16" fill="#d8703b"/>
        <path d="M765 210 C810 270, 810 330, 765 385 C720 330, 720 270, 765 210 Z" fill="#5aa6c8" opacity="0.85"/>
        <text x="450" y="520" text-anchor="middle" font-family="Georgia" font-size="32" fill="#8a6a38">Vias lacrimais · Drenagem da lágrima</text>
    </svg>
    </div>
    """

def imagem_ptose():
    return """
    <div style="background:#fffaf2;border:1px solid #d6b36a;border-radius:24px;padding:16px;box-shadow:0 10px 26px rgba(90,65,30,0.12);">
    <svg viewBox="0 0 900 560" width="100%" height="360" xmlns="http://www.w3.org/2000/svg">
        <rect width="900" height="560" rx="30" fill="#fff7ed"/>
        <text x="240" y="80" text-anchor="middle" font-family="Georgia" font-size="36" fill="#062f3a">Antes</text>
        <text x="660" y="80" text-anchor="middle" font-family="Georgia" font-size="36" fill="#062f3a">Depois</text>

        <ellipse cx="240" cy="280" rx="170" ry="115" fill="#f0c4a6" opacity="0.55"/>
        <path d="M85 280 C145 210, 335 210, 395 280 C335 350, 145 350, 85 280 Z" fill="white" stroke="#062f3a" stroke-width="7"/>
        <circle cx="240" cy="285" r="52" fill="#1f6f7a" stroke="#062f3a" stroke-width="5"/>
        <circle cx="240" cy="285" r="24" fill="#062f3a"/>
        <path d="M95 210 C160 160, 320 160, 385 210" fill="none" stroke="#5b3a1e" stroke-width="18" stroke-linecap="round"/>
        <rect x="90" y="190" width="300" height="95" rx="30" fill="#f0c4a6" opacity="0.78"/>
        <text x="240" y="455" text-anchor="middle" font-family="Georgia" font-size="28" fill="#8a6a38">Ptose</text>

        <ellipse cx="660" cy="280" rx="170" ry="115" fill="#f0c4a6" opacity="0.55"/>
        <path d="M505 280 C565 200, 755 200, 815 280 C755 360, 565 360, 505 280 Z" fill="white" stroke="#062f3a" stroke-width="7"/>
        <circle cx="660" cy="280" r="52" fill="#1f6f7a" stroke="#062f3a" stroke-width="5"/>
        <circle cx="660" cy="280" r="24" fill="#062f3a"/>
        <circle cx="638" cy="255" r="10" fill="white"/>
        <path d="M515 190 C580 145, 740 145, 805 190" fill="none" stroke="#5b3a1e" stroke-width="18" stroke-linecap="round"/>
        <path d="M525 215 C590 175, 730 175, 795 215" fill="none" stroke="#d8703b" stroke-width="7" stroke-dasharray="14 12"/>
        <text x="660" y="455" text-anchor="middle" font-family="Georgia" font-size="28" fill="#8a6a38">Correção</text>
    </svg>
    </div>
    """

def imagem_estetica():
    return """
    <div style="background:#fffaf2;border:1px solid #d6b36a;border-radius:24px;padding:16px;box-shadow:0 10px 26px rgba(90,65,30,0.12);">
    <svg viewBox="0 0 900 560" width="100%" height="360" xmlns="http://www.w3.org/2000/svg">
        <rect width="900" height="560" rx="30" fill="#fff7ed"/>
        <ellipse cx="310" cy="270" rx="170" ry="115" fill="#f0c4a6" opacity="0.55"/>
        <ellipse cx="590" cy="270" rx="170" ry="115" fill="#f0c4a6" opacity="0.55"/>
        <path d="M160 270 C220 205, 400 205, 460 270 C400 335, 220 335, 160 270 Z" fill="white" stroke="#062f3a" stroke-width="7"/>
        <path d="M440 270 C500 205, 680 205, 740 270 C680 335, 500 335, 440 270 Z" fill="white" stroke="#062f3a" stroke-width="7"/>
        <circle cx="310" cy="270" r="50" fill="#1f6f7a" stroke="#062f3a" stroke-width="5"/>
        <circle cx="590" cy="270" r="50" fill="#1f6f7a" stroke="#062f3a" stroke-width="5"/>
        <circle cx="310" cy="270" r="22" fill="#062f3a"/>
        <circle cx="590" cy="270" r="22" fill="#062f3a"/>
        <circle cx="290" cy="248" r="9" fill="white"/>
        <circle cx="570" cy="248" r="9" fill="white"/>
        <path d="M190 190 C245 145, 370 145, 430 190" fill="none" stroke="#5b3a1e" stroke-width="18" stroke-linecap="round"/>
        <path d="M470 190 C525 145, 650 145, 710 190" fill="none" stroke="#5b3a1e" stroke-width="18" stroke-linecap="round"/>
        <path d="M200 210 C250 175, 365 175, 420 210" fill="none" stroke="#d8703b" stroke-width="6" stroke-dasharray="12 10"/>
        <path d="M480 210 C530 175, 645 175, 700 210" fill="none" stroke="#d8703b" stroke-width="6" stroke-dasharray="12 10"/>
        <text x="450" y="505" text-anchor="middle" font-family="Georgia" font-size="32" fill="#8a6a38">Estética periocular · Harmonia do olhar</text>
    </svg>
    </div>
    """

def mostrar_svg(svg, altura=390):
    components.html(svg, height=altura)

# =========================
# MENU
# =========================
st.sidebar.title("BLINK CLINIC")
st.sidebar.caption("Oculoplástica · Saúde e estética do olhar")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "Serviços",
        "Galeria",
        "Sobre",
        "Informação Clínica",
        "Marcar Consulta"
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
# PÁGINAS
# =========================
if pagina == "Início":
    col1, col2 = st.columns([1.1, 0.9])

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
        mostrar_svg(imagem_oculoplastica())

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        mostrar_svg(imagem_blefaroplastia(), 330)
        st.subheader("Blefaroplastia")
        st.write("Cirurgia das pálpebras superiores e/ou inferiores, com objetivo funcional, estético ou combinado.")

    with c2:
        mostrar_svg(imagem_vias_lacrimais(), 330)
        st.subheader("Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente, obstruções e alterações do sistema lacrimal.")

    with c3:
        mostrar_svg(imagem_ptose(), 330)
        st.subheader("Ptose palpebral")
        st.write("Avaliação da queda da pálpebra superior e impacto funcional ou estético.")

elif pagina == "Serviços":
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        mostrar_svg(imagem_blefaroplastia())
        st.subheader("Blefaroplastia")
        st.write("Tratamento cirúrgico do excesso de pele e/ou bolsas palpebrais.")

        mostrar_svg(imagem_ptose())
        st.subheader("Ptose palpebral")
        st.write("Correção da queda da pálpebra superior.")

    with col2:
        mostrar_svg(imagem_vias_lacrimais())
        st.subheader("Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente e alterações da drenagem lacrimal.")

        mostrar_svg(imagem_estetica())
        st.subheader("Estética periocular")
        st.write("Tratamentos focados na harmonia do olhar, respeitando anatomia e naturalidade.")

elif pagina == "Galeria":
    st.header("Galeria criada para a Blink Clinic")

    g1, g2 = st.columns(2)

    with g1:
        mostrar_svg(imagem_oculoplastica())
        mostrar_svg(imagem_blefaroplastia())

    with g2:
        mostrar_svg(imagem_vias_lacrimais())
        mostrar_svg(imagem_ptose())

    mostrar_svg(imagem_estetica())

elif pagina == "Sobre":
    col1, col2 = st.columns([0.9, 1.1])

    with col1:
        mostrar_svg(imagem_estetica())

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

elif pagina == "Informação Clínica":
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        mostrar_svg(imagem_blefaroplastia(), 320)
        st.subheader("Quando procurar avaliação?")
        st.write("Queda das pálpebras, excesso de pele, lacrimejo, irritação ocular ou alterações do olhar.")

    with a2:
        mostrar_svg(imagem_ptose(), 320)
        st.subheader("O que pode afetar as pálpebras?")
        st.write("Ptose, excesso de pele, bolsas, entrópio, ectrópio e lesões palpebrais.")

    with a3:
        mostrar_svg(imagem_vias_lacrimais(), 320)
        st.subheader("E as vias lacrimais?")
        st.write("Alterações na drenagem da lágrima podem causar lacrimejo persistente.")

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
        mostrar_svg(imagem_oculoplastica())

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="footer">Blink Clinic · Oculoplástica · Saúde e estética do olhar</div>',
    unsafe_allow_html=True
)
