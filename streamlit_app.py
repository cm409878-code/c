import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

PASTA = Path(__file__).parent

IMG_HERO = PASTA / "clinica_hero.png"
IMG_MOSAICO = PASTA / "clinica_mosaico.png"
IMG_RECECAO = PASTA / "rececao.png"
IMG_SALA = PASTA / "sala_espera.png"
IMG_CONSULTORIO = PASTA / "consultorio.png"


def mostrar_imagem(caminho, legenda):
    if caminho.exists():
        st.image(str(caminho), caption=legenda, use_container_width=True)
    else:
        st.error(f"Imagem não encontrada: {caminho.name}")


st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fbf7ef 0%, #fffdf8 50%, #f3e8d8 100%);
        color: #062f3a;
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
        margin-top: 12px;
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

    img {
        border-radius: 24px !important;
        border: 1px solid rgba(177,132,63,0.35);
        box-shadow: 0 14px 34px rgba(90,65,30,0.13);
    }

    .gratis-box {
        background: linear-gradient(135deg, #062f3a, #0e4b58);
        color: white;
        border-radius: 22px;
        padding: 22px 26px;
        margin: 22px 0;
    }

    .gratis-box h3 {
        color: #d8b76d;
        margin-top: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

st.sidebar.title("BLINK CLINIC")
pagina = st.sidebar.radio(
    "Menu",
    ["Início", "A Clínica", "Galeria", "Serviços", "Marcar Consulta", "Contactos"]
)

if pagina == "Início":
    col1, col2 = st.columns([1, 1.1])

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
        mostrar_imagem(IMG_HERO, "Blink Clinic · Clínica premium")

    st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

    st.header("Áreas principais")

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
        mostrar_imagem(IMG_RECECAO, "Receção Blink Clinic")

    with col2:
        st.subheader("Um espaço pensado para cuidar do olhar")
        st.write(
            """
            A Blink Clinic foi pensada para transmitir conforto, sofisticação e segurança.
            A estética do espaço reflete a filosofia da clínica: detalhe, precisão e naturalidade.
            """
        )

    st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        mostrar_imagem(IMG_SALA, "Sala de espera")

    with col4:
        mostrar_imagem(IMG_CONSULTORIO, "Consultório")

elif pagina == "Galeria":
    st.header("Galeria da Clínica")

    mostrar_imagem(IMG_MOSAICO, "Identidade visual Blink Clinic")

    col1, col2 = st.columns(2)

    with col1:
        mostrar_imagem(IMG_HERO, "Entrada / ambiente principal")
        mostrar_imagem(IMG_SALA, "Sala de espera")

    with col2:
        mostrar_imagem(IMG_RECECAO, "Receção")
        mostrar_imagem(IMG_CONSULTORIO, "Consultório")

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
        st.write("Tratamentos focados na harmonia do olhar.")

        st.subheader("Lesões palpebrais")
        st.write("Avaliação, diagnóstico e eventual remoção de lesões palpebrais.")

elif pagina == "Marcar Consulta":
    st.header("Marcar Avaliação Gratuita")

    st.markdown(
        """
        <div class="gratis-box">
            <h3>Primeira avaliação gratuita</h3>
            <p>
                Preenche o formulário para pedir a tua primeira avaliação.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

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

    if st.button("Enviar pedido"):
        st.success("Pedido registado. Esta versão ainda não envia emails automaticamente.")

elif pagina == "Contactos":
    st.header("Contactos")
    st.write("Blink Clinic")
    st.write("Oculoplástica")
    st.write("Primeira avaliação: gratuita")
    st.write("Telefone: a definir")
    st.write("Email: a definir")
    st.write("Morada: a definir")
