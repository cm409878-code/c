import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# ---------- ESTILO ----------
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

    .block-container {
        padding-top: 1.8rem;
        padding-left: 3.5rem;
        padding-right: 3.5rem;
        max-width: 1450px;
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
        line-height: 1;
    }

    .frase-chave {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 27px;
        color: #b1843f;
        font-style: italic;
        margin-top: 12px;
        margin-bottom: 4px;
    }

    .subtitulo {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 19px;
        color: #6f5a34;
        letter-spacing: 2px;
        margin-top: 0;
    }

    .linha {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 25px 0 38px 0;
    }

    .etiqueta {
        color: #b1843f;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 800;
        font-size: 13px;
    }

    .caixa {
        background: rgba(255,255,255,0.82);
        border: 1px solid rgba(177,132,63,0.35);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 12px 28px rgba(90,65,30,0.10);
        margin-bottom: 20px;
    }

    .nota {
        background: rgba(255,255,255,0.80);
        border-left: 5px solid #b1843f;
        padding: 18px 22px;
        border-radius: 16px;
        margin-top: 18px;
        color: #34484d;
        line-height: 1.6;
    }

    .servico-titulo {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 23px;
        color: #062f3a;
        margin-top: 12px;
        margin-bottom: 8px;
    }

    .servico-texto {
        text-align: center;
        color: #34484d;
        line-height: 1.55;
        font-size: 15.5px;
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

    .rodape {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        color: #8a6a38;
        font-size: 20px;
        font-style: italic;
        margin-top: 40px;
    }

    @media (max-width: 900px) {
        .titulo {
            font-size: 42px;
            letter-spacing: 4px;
        }

        .frase-chave {
            font-size: 21px;
        }

        .subtitulo {
            font-size: 15px;
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

# ---------- IMAGENS CRIADAS NO CÓDIGO ----------
def mostrar_svg(svg, altura=300):
    components.html(svg, height=altura)


def imagem_blefaroplastia():
    return """
    <div style="background:#fffaf2;border:1px solid #d6b36a;border-radius:24px;padding:10px;box-shadow:0 10px 26px rgba(90,65,30,0.12);">
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
        <text x="450" y="480" text-anchor="middle" font-family="Georgia" font-size="30" fill="#8a6a38">Blefaroplastia</text>
    </svg>
    </div>
    """


def imagem_vias():
    return """
    <div style="background:#fffaf2;border:1px solid #d6b36a;border-radius:24px;padding:10px;box-shadow:0 10px 26px rgba(90,65,30,0.12);">
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
        <text x="450" y="480" text-anchor="middle" font-family="Georgia" font-size="30" fill="#8a6a38">Vias lacrimais</text>
    </svg>
    </div>
    """


def imagem_ptose():
    return """
    <div style="background:#fffaf2;border:1px solid #d6b36a;border-radius:24px;padding:10px;box-shadow:0 10px 26px rgba(90,65,30,0.12);">
    <svg viewBox="0 0 900 520" width="100%" height="270" xmlns="http://www.w3.org/2000/svg">
        <rect width="900" height="520" fill="#fff2e5"/>
        <text x="240" y="70" text-anchor="middle" font-family="Georgia" font-size="34" fill="#102c36">ANTES</text>
        <text x="660" y="70" text-anchor="middle" font-family="Georgia" font-size="34" fill="#102c36">DEPOIS</text>

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
        <text x="450" y="480" text-anchor="middle" font-family="Georgia" font-size="30" fill="#8a6a38">Ptose palpebral</text>
    </svg>
    </div>
    """


def imagem_estetica():
    return """
    <div style="background:#fffaf2;border:1px solid #d6b36a;border-radius:24px;padding:10px;box-shadow:0 10px 26px rgba(90,65,30,0.12);">
    <svg viewBox="0 0 900 520" width="100%" height="270" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <radialGradient id="irisE" cx="50%" cy="50%" r="50%">
                <stop offset="0" stop-color="#e5f2f2"/>
                <stop offset="0.45" stop-color="#579ba2"/>
                <stop offset="1" stop-color="#143d47"/>
            </radialGradient>
        </defs>
        <rect width="900" height="520" fill="#fff2e5"/>
        <ellipse cx="310" cy="250" rx="175" ry="125" fill="#f0c4a6"/>
        <ellipse cx="590" cy="250" rx="175" ry="125" fill="#f0c4a6"/>
        <path d="M150 255 C220 175, 400 175, 470 255 C400 335, 220 335, 150 255 Z"
              fill="white" stroke="#102c36" stroke-width="7"/>
        <path d="M430 255 C500 175, 680 175, 750 255 C680 335, 500 335, 430 255 Z"
              fill="white" stroke="#102c36" stroke-width="7"/>
        <circle cx="310" cy="255" r="54" fill="url(#irisE)" stroke="#102c36" stroke-width="5"/>
        <circle cx="590" cy="255" r="54" fill="url(#irisE)" stroke="#102c36" stroke-width="5"/>
        <circle cx="310" cy="255" r="24" fill="#0b2f3a"/>
        <circle cx="590" cy="255" r="24" fill="#0b2f3a"/>
        <circle cx="288" cy="230" r="10" fill="white"/>
        <circle cx="568" cy="230" r="10" fill="white"/>
        <path d="M185 160 C250 110, 375 110, 440 160"
              fill="none" stroke="#5b321a" stroke-width="18" stroke-linecap="round"/>
        <path d="M465 160 C530 110, 655 110, 720 160"
              fill="none" stroke="#5b321a" stroke-width="18" stroke-linecap="round"/>
        <text x="450" y="480" text-anchor="middle" font-family="Georgia" font-size="30" fill="#8a6a38">Estética periocular</text>
    </svg>
    </div>
    """


# ---------- MENU ----------
st.sidebar.title("BLINK CLINIC")
st.sidebar.caption("Oculoplástica · Saúde e estética do olhar")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "Serviços",
        "Galeria",
        "Informação Clínica",
        "Marcar Consulta",
        "Contactos"
    ]
)

# ---------- CABEÇALHO ----------
st.markdown('<div class="titulo">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="frase-chave">A arte de cuidar do olhar com precisão, segurança e naturalidade.</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitulo">Oculoplástica · Pálpebras · Vias Lacrimais · Órbita</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

# ---------- PÁGINAS ----------
if pagina == "Início":
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="etiqueta">Clínica de Oculoplástica</div>', unsafe_allow_html=True)
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
        mostrar_svg(imagem_blefaroplastia())

    st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        mostrar_svg(imagem_blefaroplastia(), 290)
        st.markdown('<div class="servico-titulo">Blefaroplastia</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="servico-texto">Cirurgia das pálpebras superiores e/ou inferiores.</div>',
            unsafe_allow_html=True
        )

    with c2:
        mostrar_svg(imagem_vias(), 290)
        st.markdown('<div class="servico-titulo">Vias lacrimais</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="servico-texto">Avaliação de lacrimejo persistente e obstruções lacrimais.</div>',
            unsafe_allow_html=True
        )

    with c3:
        mostrar_svg(imagem_ptose(), 290)
        st.markdown('<div class="servico-titulo">Ptose palpebral</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="servico-texto">Avaliação da queda da pálpebra superior.</div>',
            unsafe_allow_html=True
        )

elif pagina == "Serviços":
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            mostrar_svg(imagem_blefaroplastia())
            st.subheader("Blefaroplastia")
            st.write("Tratamento cirúrgico do excesso de pele e/ou bolsas palpebrais.")

        with st.container(border=True):
            mostrar_svg(imagem_ptose())
            st.subheader("Ptose palpebral")
            st.write("Correção da queda da pálpebra superior.")

        with st.container(border=True):
            st.subheader("Entrópio e Ectrópio")
            st.write("Correção de alterações da posição das pálpebras.")

    with col2:
        with st.container(border=True):
            mostrar_svg(imagem_vias())
            st.subheader("Vias lacrimais")
            st.write("Avaliação de lacrimejo persistente e alterações da drenagem lacrimal.")

        with st.container(border=True):
            mostrar_svg(imagem_estetica())
            st.subheader("Estética periocular")
            st.write("Tratamentos focados na harmonia do olhar, respeitando anatomia e naturalidade.")

        with st.container(border=True):
            st.subheader("Lesões palpebrais")
            st.write("Avaliação, diagnóstico e eventual remoção de lesões localizadas nas pálpebras.")

elif pagina == "Galeria":
    st.header("Galeria visual")

    g1, g2 = st.columns(2)

    with g1:
        mostrar_svg(imagem_blefaroplastia())
        mostrar_svg(imagem_vias())

    with g2:
        mostrar_svg(imagem_ptose())
        mostrar_svg(imagem_estetica())

elif pagina == "Informação Clínica":
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        with st.container(border=True):
            st.subheader("Quando procurar avaliação?")
            st.write("Queda das pálpebras, excesso de pele, lacrimejo, irritação ocular ou alterações do olhar.")

    with a2:
        with st.container(border=True):
            st.subheader("O que pode afetar as pálpebras?")
            st.write("Ptose, excesso de pele, bolsas, entrópio, ectrópio e lesões palpebrais.")

    with a3:
        with st.container(border=True):
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
        mostrar_svg(imagem_blefaroplastia())

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
        mostrar_svg(imagem_estetica())

st.markdown('<div class="linha"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="rodape">Blink Clinic · Oculoplástica · Saúde e estética do olhar</div>',
    unsafe_allow_html=True
)
