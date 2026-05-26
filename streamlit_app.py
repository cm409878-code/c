import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# -------------------------
# Funções para criar imagens
# -------------------------
def font(size=24):
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()


def criar_base(titulo):
    img = Image.new("RGB", (900, 560), "#fff7ed")
    d = ImageDraw.Draw(img)

    # fundo suave
    d.rounded_rectangle((20, 20, 880, 540), radius=35, fill="#fffaf2", outline="#d6b36a", width=3)

    # pele / zona periocular
    d.ellipse((170, 150, 730, 405), fill="#f0c4a6")

    # olho
    d.polygon(
        [
            (160, 280), (250, 200), (450, 175), (650, 200),
            (740, 280), (650, 360), (450, 385), (250, 360)
        ],
        fill="white",
        outline="#062f3a"
    )

    # íris e pupila
    d.ellipse((380, 210, 520, 350), fill="#1f6f7a", outline="#062f3a", width=4)
    d.ellipse((420, 250, 480, 310), fill="#062f3a")
    d.ellipse((405, 232, 430, 257), fill="white")

    # sobrancelha
    d.arc((220, 95, 680, 250), start=200, end=340, fill="#5b3a1e", width=18)

    # título
    d.text((450, 500), titulo, anchor="mm", fill="#8a6a38", font=font(28))

    return img


def imagem_blefaroplastia():
    img = criar_base("Blefaroplastia · Marcação palpebral")
    d = ImageDraw.Draw(img)

    # linhas cirúrgicas
    d.arc((220, 140, 680, 315), start=200, end=340, fill="#d8703b", width=8)
    d.arc((230, 260, 670, 430), start=20, end=160, fill="#d8703b", width=8)

    # tracejado simples
    for x in range(250, 660, 55):
        d.line((x, 150, x + 20, 120), fill="#d8703b", width=5)
        d.line((x, 405, x + 20, 435), fill="#d8703b", width=5)

    return img


def imagem_ptose():
    img = Image.new("RGB", (900, 560), "#fff7ed")
    d = ImageDraw.Draw(img)

    d.rounded_rectangle((20, 20, 880, 540), radius=35, fill="#fffaf2", outline="#d6b36a", width=3)

    d.text((230, 70), "Antes", anchor="mm", fill="#062f3a", font=font(34))
    d.text((670, 70), "Depois", anchor="mm", fill="#062f3a", font=font(34))

    # antes
    d.ellipse((90, 170, 370, 395), fill="#f0c4a6")
    d.polygon([(100, 280), (170, 220), (230, 210), (300, 220), (360, 280), (300, 335), (230, 345), (170, 335)], fill="white", outline="#062f3a")
    d.ellipse((190, 245, 270, 325), fill="#1f6f7a", outline="#062f3a", width=4)
    d.ellipse((220, 275, 245, 300), fill="#062f3a")
    d.rounded_rectangle((105, 185, 355, 270), radius=25, fill="#f0c4a6")
    d.arc((120, 130, 340, 245), start=200, end=340, fill="#5b3a1e", width=14)
    d.text((230, 455), "Ptose palpebral", anchor="mm", fill="#8a6a38", font=font(25))

    # depois
    d.ellipse((530, 170, 810, 395), fill="#f0c4a6")
    d.polygon([(540, 280), (610, 210), (670, 195), (740, 210), (800, 280), (740, 350), (670, 365), (610, 350)], fill="white", outline="#062f3a")
    d.ellipse((630, 235, 710, 315), fill="#1f6f7a", outline="#062f3a", width=4)
    d.ellipse((660, 265, 685, 290), fill="#062f3a")
    d.ellipse((645, 247, 660, 262), fill="white")
    d.arc((560, 115, 790, 240), start=200, end=340, fill="#5b3a1e", width=14)
    d.arc((565, 155, 785, 280), start=200, end=340, fill="#d8703b", width=6)
    d.text((670, 455), "Correção palpebral", anchor="mm", fill="#8a6a38", font=font(25))

    return img


def imagem_vias_lacrimais():
    img = criar_base("Vias lacrimais · Drenagem da lágrima")
    d = ImageDraw.Draw(img)

    # sistema lacrimal
    d.ellipse((650, 230, 680, 260), fill="#d8703b")
    d.line((665, 260, 700, 330), fill="#d8703b", width=10)
    d.arc((650, 300, 760, 450), start=290, end=80, fill="#d8703b", width=10)
    d.ellipse((715, 405, 745, 435), fill="#d8703b")

    # lágrima
    d.polygon([(735, 230), (765, 300), (705, 300)], fill="#5aa6c8")
    d.ellipse((705, 270, 765, 330), fill="#5aa6c8")

    d.text((700, 160), "sistema lacrimal", anchor="mm", fill="#062f3a", font=font(22))

    return img


def imagem_estetica():
    img = Image.new("RGB", (900, 560), "#fff7ed")
    d = ImageDraw.Draw(img)

    d.rounded_rectangle((20, 20, 880, 540), radius=35, fill="#fffaf2", outline="#d6b36a", width=3)

    # dois olhos estilizados
    for cx in [310, 590]:
        d.ellipse((cx - 170, 170, cx + 170, 380), fill="#f0c4a6")
        d.polygon(
            [
                (cx - 150, 275), (cx - 90, 220), (cx, 205),
                (cx + 90, 220), (cx + 150, 275), (cx + 90, 330),
                (cx, 345), (cx - 90, 330)
            ],
            fill="white",
            outline="#062f3a"
        )
        d.ellipse((cx - 45, 230, cx + 45, 320), fill="#1f6f7a", outline="#062f3a", width=4)
        d.ellipse((cx - 18, 260, cx + 18, 296), fill="#062f3a")
        d.ellipse((cx - 28, 242, cx - 10, 260), fill="white")
        d.arc((cx - 130, 120, cx + 130, 245), start=200, end=340, fill="#5b3a1e", width=14)
        d.arc((cx - 120, 160, cx + 120, 290), start=200, end=340, fill="#d8703b", width=6)

    d.text((450, 485), "Estética periocular · Naturalidade e harmonia", anchor="mm", fill="#8a6a38", font=font(28))

    return img


def imagem_oculoplastica():
    img = criar_base("Oculoplástica · Avaliação periocular")
    d = ImageDraw.Draw(img)

    # linhas de planeamento facial
    d.line((450, 90, 450, 455), fill="#d8703b", width=4)
    d.line((210, 280, 690, 280), fill="#d8703b", width=4)
    d.arc((220, 120, 680, 440), start=200, end=340, fill="#b1843f", width=6)
    d.arc((220, 120, 680, 440), start=20, end=160, fill="#b1843f", width=6)

    d.text((450, 80), "planeamento", anchor="mm", fill="#062f3a", font=font(22))

    return img


# criar imagens
IMG_OCULOPLASTICA = imagem_oculoplastica()
IMG_BLEFARO = imagem_blefaroplastia()
IMG_VIAS = imagem_vias_lacrimais()
IMG_PTOSE = imagem_ptose()
IMG_ESTETICA = imagem_estetica()


# -------------------------
# ESTILO DA APP
# -------------------------
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
        font-size: 64px;
        letter-spacing: 9px;
        color: #062f3a;
        margin-bottom: 0;
    }

    .brand-subtitle {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 27px;
        color: #b1843f;
        font-style: italic;
        margin-top: -6px;
    }

    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 26px 0 40px 0;
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

# -------------------------
# MENU
# -------------------------
st.sidebar.title("BLINK CLINIC")
st.sidebar.caption("Oculoplástica · Saúde e estética do olhar")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "O que é Oculoplástica",
        "Serviços",
        "Galeria",
        "Informação Clínica",
        "Contactos"
    ]
)

# -------------------------
# CABEÇALHO
# -------------------------
st.markdown('<div class="brand-title">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="brand-subtitle">Oculoplástica · Pálpebras · Vias Lacrimais · Órbita</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# -------------------------
# PÁGINAS
# -------------------------
if pagina == "Início":
    col1, col2 = st.columns([1.15, 0.85])

    with col1:
        st.markdown('<div class="section-label">Clínica de Oculoplástica</div>', unsafe_allow_html=True)
        st.title("Precisão médica para a saúde e estética do olhar")

        st.write(
            """
            A Blink Clinic dedica-se à avaliação e tratamento das estruturas perioculares:
            pálpebras, vias lacrimais, órbita e região envolvente do olho.
            """
        )

        st.write(
            """
            A abordagem combina rigor médico, segurança clínica, naturalidade estética
            e atenção à função visual.
            """
        )

        st.button("Marcar Consulta")

        st.markdown(
            """
            <div class="note">
            Cuidado especializado em blefaroplastia, ptose palpebral, entrópio,
            ectrópio, vias lacrimais, lesões palpebrais, órbita e estética periocular.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image(IMG_OCULOPLASTICA, caption="Planeamento e avaliação em oculoplástica", use_container_width=True)

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.image(IMG_BLEFARO, caption="Blefaroplastia", use_container_width=True)
        st.subheader("Blefaroplastia")
        st.write("Cirurgia das pálpebras superiores e/ou inferiores, com objetivo funcional, estético ou combinado.")

    with c2:
        st.image(IMG_VIAS, caption="Vias lacrimais", use_container_width=True)
        st.subheader("Vias lacrimais")
        st.write("Avaliação de lacrimejo persistente, obstruções e alterações do sistema lacrimal.")

    with c3:
        st.image(IMG_PTOSE, caption="Ptose palpebral", use_container_width=True)
        st.subheader("Ptose palpebral")
        st.write("Avaliação da queda da pálpebra superior e impacto funcional ou estético.")


elif pagina == "O que é Oculoplástica":
    col1, col2 = st.columns([0.95, 1.05])

    with col1:
        st.image(IMG_OCULOPLASTICA, caption="Oculoplástica", use_container_width=True)

    with col2:
        st.markdown('<div class="section-label">Especialidade</div>', unsafe_allow_html=True)
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


elif pagina == "Serviços":
    st.markdown('<div class="section-label">Serviços médicos</div>', unsafe_allow_html=True)
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        st.image(IMG_BLEFARO, caption="Blefaroplastia", use_container_width=True)
        with st.container(border=True):
            st.subheader("Blefaroplastia superior e inferior")
            st.write("Tratamento cirúrgico do excesso de pele e/ou bolsas palpebrais.")

        st.image(IMG_PTOSE, caption="Ptose palpebral", use_container_width=True)
        with st.container(border=True):
            st.subheader("Ptose palpebral")
            st.write("Correção da queda da pálpebra superior.")

        with st.container(border=True):
            st.subheader("Entrópio e Ectrópio")
            st.write("Correção de alterações da posição das pálpebras.")

    with col2:
        st.image(IMG_VIAS, caption="Vias lacrimais", use_container_width=True)
        with st.container(border=True):
            st.subheader("Vias lacrimais")
            st.write("Avaliação de lacrimejo persistente e alterações da drenagem lacrimal.")

        st.image(IMG_ESTETICA, caption="Estética periocular", use_container_width=True)
        with st.container(border=True):
            st.subheader("Estética periocular")
            st.write("Tratamentos focados na harmonia do olhar, respeitando anatomia e naturalidade.")

        with st.container(border=True):
            st.subheader("Lesões palpebrais")
            st.write("Observação, diagnóstico e eventual remoção de lesões nas pálpebras.")


elif pagina == "Galeria":
    st.markdown('<div class="section-label">Imagens criadas para a Blink Clinic</div>', unsafe_allow_html=True)
    st.header("Galeria de Oculoplástica")

    g1, g2, g3 = st.columns(3)

    with g1:
        st.image(IMG_OCULOPLASTICA, caption="Oculoplástica", use_container_width=True)
        st.image(IMG_BLEFARO, caption="Blefaroplastia", use_container_width=True)

    with g2:
        st.image(IMG_VIAS, caption="Vias lacrimais", use_container_width=True)
        st.image(IMG_PTOSE, caption="Ptose palpebral", use_container_width=True)

    with g3:
        st.image(IMG_ESTETICA, caption="Estética periocular", use_container_width=True)


elif pagina == "Informação Clínica":
    st.markdown('<div class="section-label">Educação do paciente</div>', unsafe_allow_html=True)
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        with st.container(border=True):
            st.subheader("Quando procurar avaliação?")
            st.write("Queda das pálpebras, excesso de pele, lacrimejo, irritação ocular, lesões palpebrais ou alterações do olhar.")

    with a2:
        with st.container(border=True):
            st.subheader("O que pode afetar as pálpebras?")
            st.write("Excesso de pele, bolsas, ptose, entrópio, ectrópio, retração palpebral e lesões palpebrais.")

    with a3:
        with st.container(border=True):
            st.subheader("O que pode afetar as vias lacrimais?")
            st.write("Alterações na produção, distribuição ou drenagem da lágrima, podendo causar lacrimejo persistente.")


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
        st.image(IMG_ESTETICA, caption="Blink Clinic · Contactos", use_container_width=True)
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
