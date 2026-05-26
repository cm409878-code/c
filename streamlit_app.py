import streamlit as st
import os

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# -------------------------
# IMAGENS
# -------------------------
def mostrar_imagem(nome, legenda=""):
    if os.path.exists(nome):
        st.image(nome, use_container_width=True, caption=legenda)
    else:
        st.warning(f"Imagem em falta: {nome}")


# -------------------------
# ESTILO
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
        box-shadow: 0 8px 22px rgba(90, 65, 30, 0.08);
    }

    .service-card {
        background: rgba(255, 255, 255, 0.86);
        border: 1px solid rgba(177, 132, 63, 0.30);
        border-radius: 22px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 8px 22px rgba(90, 65, 30, 0.08);
        min-height: 210px;
    }

    .service-card h3 {
        margin-top: 0;
        color: #062f3a;
    }

    .service-card p {
        color: #34484d;
        line-height: 1.65;
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

    @media (max-width: 900px) {
        .brand-title {
            font-size: 40px;
            letter-spacing: 5px;
        }

        .brand-subtitle {
            font-size: 20px;
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
# INÍCIO
# -------------------------
if pagina == "Início":
    col1, col2 = st.columns([1.15, 0.85])

    with col1:
        st.markdown(
            '<div class="section-label">Clínica de Oculoplástica</div>',
            unsafe_allow_html=True
        )

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
        mostrar_imagem(
            "oculoplastica.png",
            "Planeamento e avaliação em oculoplástica"
        )

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-label">Áreas principais</div>',
        unsafe_allow_html=True
    )
    st.header("Cuidado especializado do olhar")

    c1, c2, c3 = st.columns(3)

    with c1:
        mostrar_imagem("blefaroplastia.png", "Blefaroplastia")
        st.subheader("Pálpebras")
        st.write(
            """
            Tratamento de excesso de pele, bolsas palpebrais, ptose,
            entrópio, ectrópio e lesões das pálpebras.
            """
        )

    with c2:
        mostrar_imagem("vias_lacrimais.png", "Vias lacrimais")
        st.subheader("Vias lacrimais")
        st.write(
            """
            Avaliação de lacrimejo persistente, obstruções e alterações
            da drenagem lacrimal.
            """
        )

    with c3:
        mostrar_imagem("ptose_palpebral.png", "Ptose palpebral")
        st.subheader("Ptose palpebral")
        st.write(
            """
            Avaliação da queda da pálpebra superior e do impacto na visão,
            expressão facial e simetria do olhar.
            """
        )


# -------------------------
# O QUE É OCULOPLÁSTICA
# -------------------------
elif pagina == "O que é Oculoplástica":
    col1, col2 = st.columns([0.95, 1.05])

    with col1:
        mostrar_imagem("oculoplastica.png", "Oculoplástica")

    with col2:
        st.markdown(
            '<div class="section-label">Especialidade</div>',
            unsafe_allow_html=True
        )
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

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.header("Estruturas tratadas")

    e1, e2, e3 = st.columns(3)

    with e1:
        with st.container(border=True):
            st.subheader("Pálpebras")
            st.write(
                """
                Protegem o olho, ajudam na distribuição da lágrima e podem sofrer alterações
                de posição, excesso de pele, queda ou lesões.
                """
            )

    with e2:
        with st.container(border=True):
            st.subheader("Órbita")
            st.write(
                """
                Cavidade óssea que envolve o globo ocular e contém gordura, músculos,
                vasos, nervos e estruturas anexas.
                """
            )

    with e3:
        with st.container(border=True):
            st.subheader("Vias lacrimais")
            st.write(
                """
                Sistema responsável pela produção, distribuição e drenagem da lágrima.
                Alterações podem provocar lacrimejo ou infeções.
                """
            )


# -------------------------
# SERVIÇOS
# -------------------------
elif pagina == "Serviços":
    st.markdown(
        '<div class="section-label">Serviços médicos</div>',
        unsafe_allow_html=True
    )
    st.header("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            mostrar_imagem("blefaroplastia.png", "Blefaroplastia")
            st.subheader("Blefaroplastia superior e inferior")
            st.write(
                """
                Tratamento cirúrgico do excesso de pele nas pálpebras superiores
                e/ou das bolsas das pálpebras inferiores. Pode ter finalidade estética,
                funcional ou ambas.
                """
            )

        with st.container(border=True):
            mostrar_imagem("ptose_palpebral.png", "Ptose palpebral")
            st.subheader("Ptose palpebral")
            st.write(
                """
                Correção da queda da pálpebra superior quando esta interfere com a visão,
                a simetria facial ou dá uma expressão persistente de cansaço.
                """
            )

        with st.container(border=True):
            st.subheader("Entrópio")
            st.write(
                """
                Alteração em que a pálpebra vira para dentro, fazendo com que as pestanas
                toquem no olho. Pode causar irritação, sensação de corpo estranho,
                lacrimejo e desconforto ocular.
                """
            )

        with st.container(border=True):
            st.subheader("Ectrópio")
            st.write(
                """
                Alteração em que a pálpebra vira para fora, podendo causar lacrimejo,
                irritação, secreção e exposição da superfície ocular.
                """
            )

    with col2:
        with st.container(border=True):
            mostrar_imagem("vias_lacrimais.png", "Vias lacrimais")
            st.subheader("Vias lacrimais e epífora")
            st.write(
                """
                Avaliação de lacrimejo excessivo, obstruções dos pontos lacrimais,
                canalículos, saco lacrimal ou ducto nasolacrimal.
                """
            )

        with st.container(border=True):
            mostrar_imagem("oculoplastica.png", "Lesões palpebrais")
            st.subheader("Lesões e tumores palpebrais")
            st.write(
                """
                Observação, diagnóstico, acompanhamento e eventual remoção de lesões
                benignas ou suspeitas localizadas nas pálpebras.
                """
            )

        with st.container(border=True):
            st.subheader("Xantelasmas")
            st.write(
                """
                Lesões amareladas ou placas de gordura que surgem frequentemente
                junto às pálpebras. A abordagem depende da avaliação clínica individual.
                """
            )

        with st.container(border=True):
            mostrar_imagem("estetica_periocular.png", "Estética periocular")
            st.subheader("Estética periocular")
            st.write(
                """
                Tratamentos focados na harmonia do olhar, respeitando a anatomia,
                a função palpebral e a naturalidade facial.
                """
            )

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.header("Órbita e condições associadas")

    o1, o2, o3 = st.columns(3)

    with o1:
        with st.container(border=True):
            st.subheader("Orbitopatia tiroideia")
            st.write(
                """
                Alteração orbitária associada a doença tiroideia autoimune.
                Pode provocar protrusão ocular, alterações palpebrais e desconforto.
                """
            )

    with o2:
        with st.container(border=True):
            st.subheader("Traumatismos orbitários")
            st.write(
                """
                Avaliação de sequelas após traumatismos, fraturas orbitárias
                ou alterações da posição ocular.
                """
            )

    with o3:
        with st.container(border=True):
            st.subheader("Ptose da sobrancelha")
            st.write(
                """
                Descida da sobrancelha que pode contribuir para excesso de pele
                palpebral e sensação de peso no olhar.
                """
            )

    st.markdown(
        """
        <div class="note">
        Todos os procedimentos dependem de avaliação médica individual.
        Esta informação é geral e não substitui uma consulta de oftalmologia/oculoplástica.
        </div>
        """,
        unsafe_allow_html=True
    )


# -------------------------
# GALERIA
# -------------------------
elif pagina == "Galeria":
    st.markdown(
        '<div class="section-label">Imagens clínicas e educativas</div>',
        unsafe_allow_html=True
    )
    st.header("Galeria de Oculoplástica")

    g1, g2, g3 = st.columns(3)

    with g1:
        mostrar_imagem("oculoplastica.png", "Oculoplástica")
        mostrar_imagem("blefaroplastia.png", "Blefaroplastia")

    with g2:
        mostrar_imagem("vias_lacrimais.png", "Vias lacrimais")
        mostrar_imagem("ptose_palpebral.png", "Ptose palpebral")

    with g3:
        mostrar_imagem("estetica_periocular.png", "Estética periocular")


# -------------------------
# INFORMAÇÃO CLÍNICA
# -------------------------
elif pagina == "Informação Clínica":
    st.markdown(
        '<div class="section-label">Educação do paciente</div>',
        unsafe_allow_html=True
    )
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        with st.container(border=True):
            st.subheader("Quando procurar avaliação?")
            st.write(
                """
                Quando há queda das pálpebras, excesso de pele, lacrimejo,
                irritação ocular, lesões palpebrais, assimetria ou alterações do olhar.
                """
            )

    with a2:
        with st.container(border=True):
            st.subheader("O que pode afetar as pálpebras?")
            st.write(
                """
                Excesso de pele, bolsas, ptose, entrópio, ectrópio, retração palpebral,
                xantelasmas, inflamação e lesões palpebrais.
                """
            )

    with a3:
        with st.container(border=True):
            st.subheader("O que pode afetar as vias lacrimais?")
            st.write(
                """
                Alterações na produção, distribuição ou drenagem da lágrima,
                podendo causar lacrimejo persistente, infeções ou desconforto.
                """
            )

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.header("Perguntas frequentes")

    with st.expander("A blefaroplastia é estética ou funcional?"):
        st.write(
            """
            Pode ser estética, funcional ou ambas. Em alguns casos, o excesso de pele
            interfere com o campo visual ou causa sensação de peso nas pálpebras.
            """
        )

    with st.expander("A ptose palpebral pode afetar a visão?"):
        st.write(
            """
            Sim. Quando a pálpebra superior está caída, pode obstruir parcialmente
            o campo visual e causar compensações como elevação das sobrancelhas.
            """
        )

    with st.expander("O lacrimejo persistente tem tratamento?"):
        st.write(
            """
            Depende da causa. Pode estar relacionado com inflamação, olho seco,
            alterações palpebrais ou obstrução das vias lacrimais.
            """
        )

    with st.expander("Lesões nas pálpebras devem ser avaliadas?"):
        st.write(
            """
            Sim. Algumas lesões são benignas, mas outras exigem diagnóstico e seguimento.
            A avaliação médica é importante para decidir a melhor abordagem.
            """
        )


# -------------------------
# CONTACTOS
# -------------------------
elif pagina == "Contactos":
    st.markdown(
        '<div class="section-label">Marcação</div>',
        unsafe_allow_html=True
    )
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
                    "Xantelasma",
                    "Estética periocular",
                    "Outro"
                ]
            )
            mensagem = st.text_area("Mensagem")

            if st.button("Enviar pedido"):
                st.success("Pedido registado. Esta versão ainda não envia emails automaticamente.")

    with col2:
        mostrar_imagem("estetica_periocular.png", "Blink Clinic · Contactos")

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
