import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# =========================
# ESTILO
# =========================
st.markdown("""
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

.frase {
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

.gratis-box {
    background: linear-gradient(135deg, #062f3a, #0e4b58);
    color: white;
    border-radius: 22px;
    padding: 22px 26px;
    margin: 22px 0;
    border: 1px solid rgba(177,132,63,0.55);
    box-shadow: 0 16px 34px rgba(6,47,58,0.18);
}

.gratis-box h3 {
    color: #d8b76d;
    margin-top: 0;
    font-size: 26px;
}

.gratis-box p {
    color: #f8eedc;
    font-size: 17px;
    line-height: 1.55;
    margin-bottom: 0;
}

.nota {
    background: rgba(255,255,255,0.84);
    border-left: 5px solid #b1843f;
    padding: 18px 22px;
    border-radius: 16px;
    margin-top: 18px;
    color: #34484d;
    line-height: 1.6;
    box-shadow: 0 8px 22px rgba(90,65,30,0.08);
}

.card {
    background: rgba(255,255,255,0.86);
    border: 1px solid rgba(177,132,63,0.32);
    border-radius: 22px;
    padding: 24px;
    margin-bottom: 18px;
    box-shadow: 0 12px 28px rgba(90,65,30,0.08);
    min-height: 190px;
}

.card h3 {
    margin-top: 0;
}

.card p {
    color: #34484d;
    line-height: 1.6;
}

img {
    border-radius: 24px !important;
    border: 1px solid rgba(177,132,63,0.35);
    box-shadow: 0 14px 34px rgba(90,65,30,0.13);
}

.placeholder {
    background: rgba(255,255,255,0.78);
    border: 1px dashed #b1843f;
    border-radius: 22px;
    padding: 38px;
    text-align: center;
    color: #8a6a38;
    margin-bottom: 20px;
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

    .frase {
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
""", unsafe_allow_html=True)


# =========================
# FUNÇÃO PARA MOSTRAR FOTOS
# =========================
def mostrar_foto(foto, legenda):
    if foto is not None:
        st.image(foto, caption=legenda, use_container_width=True)
    else:
        st.markdown(
            f"""
            <div class="placeholder">
                <strong>Fotografia ainda não carregada</strong><br><br>
                Vai à barra lateral e carrega a imagem para:<br>
                {legenda}
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# MENU + UPLOAD DE FOTOS
# =========================
st.sidebar.title("BLINK CLINIC")
st.sidebar.caption("Oculoplástica · Saúde e estética do olhar")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "A Clínica",
        "Serviços",
        "Galeria",
        "Informação Clínica",
        "Marcar Consulta",
        "Contactos"
    ]
)

st.sidebar.divider()
st.sidebar.subheader("Carregar fotografias")

foto_principal = st.sidebar.file_uploader(
    "1. Fotografia principal",
    type=["png", "jpg", "jpeg"]
)

foto_rececao = st.sidebar.file_uploader(
    "2. Fotografia da receção",
    type=["png", "jpg", "jpeg"]
)

foto_sala = st.sidebar.file_uploader(
    "3. Fotografia da sala de espera",
    type=["png", "jpg", "jpeg"]
)

foto_consultorio = st.sidebar.file_uploader(
    "4. Fotografia do consultório",
    type=["png", "jpg", "jpeg"]
)

foto_extra = st.sidebar.file_uploader(
    "5. Fotografia extra",
    type=["png", "jpg", "jpeg"]
)


# =========================
# CABEÇALHO
# =========================
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


# =========================
# PÁGINA INÍCIO
# =========================
if pagina == "Início":
    col1, col2 = st.columns([1, 1.05])

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

        st.button("Marcar Avaliação Gratuita")

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
        mostrar_foto(foto_principal, "Fotografia principal da Blink Clinic")

    st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

    st.header("Áreas principais")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="card">
                <h3>Blefaroplastia</h3>
                <p>
                    Cirurgia das pálpebras superiores e/ou inferiores,
                    com objetivo funcional, estético ou combinado.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="card">
                <h3>Vias lacrimais</h3>
                <p>
                    Avaliação de lacrimejo persistente, obstruções e alterações
                    do sistema lacrimal.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="card">
                <h3>Ptose palpebral</h3>
                <p>
                    Avaliação e tratamento da queda da pálpebra superior.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# PÁGINA A CLÍNICA
# =========================
elif pagina == "A Clínica":
    st.header("A Clínica")

    col1, col2 = st.columns([1, 1])

    with col1:
        mostrar_foto(foto_rececao, "Receção da Blink Clinic")

    with col2:
        st.markdown('<div class="etiqueta">Sobre a clínica</div>', unsafe_allow_html=True)
        st.header("Um espaço pensado para cuidar do olhar")

        st.write(
            """
            A Blink Clinic foi pensada para transmitir conforto, sofisticação e segurança.
            A estética do espaço reflete a filosofia da clínica: detalhe, precisão e naturalidade.
            """
        )

        st.write("• Ambiente premium e acolhedor")
        st.write("• Consulta personalizada")
        st.write("• Foco em resultados naturais")
        st.write("• Acompanhamento próximo")
        st.write("• Abordagem médica rigorosa")

    st.markdown('<div class="linha"></div>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        mostrar_foto(foto_sala, "Sala de espera")

    with col4:
        mostrar_foto(foto_consultorio, "Consultório")


# =========================
# SERVIÇOS
# =========================
elif pagina == "Serviços":
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>Blefaroplastia</h3>
                <p>
                    Tratamento cirúrgico do excesso de pele e/ou bolsas palpebrais.
                    Pode ter finalidade funcional, estética ou combinada.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Ptose palpebral</h3>
                <p>
                    Correção da queda da pálpebra superior quando interfere com a visão,
                    a expressão facial ou a simetria do olhar.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Entrópio e Ectrópio</h3>
                <p>
                    Correção de alterações da posição das pálpebras que podem causar
                    irritação ocular, lacrimejo ou desconforto.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>Vias lacrimais</h3>
                <p>
                    Avaliação de lacrimejo persistente, obstruções lacrimais e alterações
                    associadas à drenagem da lágrima.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Lesões palpebrais</h3>
                <p>
                    Observação, diagnóstico, acompanhamento e eventual remoção de lesões
                    localizadas nas pálpebras.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Estética periocular</h3>
                <p>
                    Tratamentos focados na harmonia do olhar, respeitando anatomia,
                    função palpebral e naturalidade facial.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="nota">
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
    st.header("Galeria da Clínica")

    g1, g2 = st.columns(2)

    with g1:
        mostrar_foto(foto_principal, "Fotografia principal")
        mostrar_foto(foto_sala, "Sala de espera")

    with g2:
        mostrar_foto(foto_rececao, "Receção")
        mostrar_foto(foto_consultorio, "Consultório")

    mostrar_foto(foto_extra, "Fotografia extra / ambiente")


# =========================
# INFORMAÇÃO CLÍNICA
# =========================
elif pagina == "Informação Clínica":
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        st.markdown(
            """
            <div class="card">
                <h3>Quando procurar avaliação?</h3>
                <p>
                    Queda das pálpebras, excesso de pele, lacrimejo,
                    irritação ocular ou alterações do olhar.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a2:
        st.markdown(
            """
            <div class="card">
                <h3>O que pode afetar as pálpebras?</h3>
                <p>
                    Ptose, excesso de pele, bolsas, entrópio,
                    ectrópio e lesões palpebrais.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a3:
        st.markdown(
            """
            <div class="card">
                <h3>E as vias lacrimais?</h3>
                <p>
                    Alterações na drenagem da lágrima podem causar
                    lacrimejo persistente.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# MARCAR CONSULTA
# =========================
elif pagina == "Marcar Consulta":
    st.header("Marcar Avaliação Gratuita")

    st.markdown(
        """
        <div class="gratis-box">
            <h3>Primeira avaliação gratuita</h3>
            <p>
                Preenche o formulário para pedir a tua primeira avaliação.
                Esta etapa serve para perceber o motivo da consulta e orientar o próximo passo.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])

    with col1:
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

        if st.button("Enviar pedido de avaliação gratuita"):
            st.success("Pedido registado. Esta versão ainda não envia emails automaticamente.")

    with col2:
        mostrar_foto(foto_rececao, "Blink Clinic · Avaliação gratuita")


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
        st.write("Primeira avaliação: gratuita")
        st.write("Telefone: a definir")
        st.write("Email: a definir")
        st.write("Morada: a definir")

    with col2:
        mostrar_foto(foto_extra, "Blink Clinic")


# =========================
# RODAPÉ
# =========================
st.markdown('<div class="linha"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="rodape">Blink Clinic · Oculoplástica · Saúde e estética do olhar</div>',
    unsafe_allow_html=True
)
