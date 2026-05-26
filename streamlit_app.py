import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# =========================
# ESTILO VISUAL
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

    .soft-box {
        background: rgba(255, 255, 255, 0.72);
        border-left: 5px solid #b1843f;
        padding: 20px 24px;
        border-radius: 16px;
        color: #34484d;
        margin-top: 18px;
        box-shadow: 0 8px 24px rgba(90, 65, 30, 0.08);
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
# MENU
# =========================
st.sidebar.title("BLINK CLINIC")
st.sidebar.caption("Oculoplástica · Saúde do olhar")
pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "Serviços",
        "Sobre",
        "Informação Clínica",
        "Contactos"
    ]
)

# =========================
# CABEÇALHO GLOBAL
# =========================
st.markdown('<div class="brand-title">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="brand-subtitle">Oculoplástica · Pálpebras · Vias Lacrimais · Órbita</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# PÁGINA INÍCIO
# =========================
if pagina == "Início":
    col1, col2 = st.columns([1.25, 0.75])

    with col1:
        st.markdown(
            '<div class="section-label">Clínica de Oculoplástica</div>',
            unsafe_allow_html=True
        )

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
        with st.container(border=True):
            st.markdown("## 👁️")
            st.subheader("Oculoplástica")
            st.write(
                """
                Área da oftalmologia dedicada às pálpebras, vias lacrimais,
                órbita e região periocular.
                """
            )

        with st.container(border=True):
            st.markdown("## ✨")
            st.subheader("Estética periocular")
            st.write(
                """
                Intervenções pensadas para preservar a identidade facial,
                respeitando a anatomia e a naturalidade do olhar.
                """
            )

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Especialidade", "Oculoplástica")

    with m2:
        st.metric("Foco", "Região periocular")

    with m3:
        st.metric("Abordagem", "Médica e estética")

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-label">Áreas principais</div>',
        unsafe_allow_html=True
    )
    st.header("Cuidado especializado do olhar")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown("## 👁️")
            st.subheader("Pálpebras")
            st.write(
                """
                Avaliação e tratamento de alterações palpebrais, incluindo
                excesso de pele, ptose, entrópio, ectrópio e lesões palpebrais.
                """
            )

    with c2:
        with st.container(border=True):
            st.markdown("## 💧")
            st.subheader("Vias lacrimais")
            st.write(
                """
                Estudo de lacrimejo persistente, obstrução das vias lacrimais
                e alterações do sistema de drenagem lacrimal.
                """
            )

    with c3:
        with st.container(border=True):
            st.markdown("## 🩺")
            st.subheader("Órbita")
            st.write(
                """
                Avaliação de alterações orbitárias, assimetrias, sequelas
                pós-traumáticas ou outras condições perioculares.
                """
            )

# =========================
# PÁGINA SERVIÇOS
# =========================
elif pagina == "Serviços":
    st.markdown(
        '<div class="section-label">Serviços médicos</div>',
        unsafe_allow_html=True
    )
    st.header("Serviços de Oculoplástica")

    s1, s2 = st.columns(2)

    with s1:
        with st.container(border=True):
            st.markdown("## 01 · Blefaroplastia")
            st.write(
                """
                Cirurgia das pálpebras superiores e/ou inferiores, indicada para
                excesso de pele, bolsas palpebrais ou alterações com impacto funcional
                e/ou estético.
                """
            )

        with st.container(border=True):
            st.markdown("## 02 · Ptose palpebral")
            st.write(
                """
                Avaliação e tratamento da queda da pálpebra superior, que pode
                interferir com o campo visual, a simetria facial ou o conforto visual.
                """
            )

        with st.container(border=True):
            st.markdown("## 03 · Entrópio e ectrópio")
            st.write(
                """
                Correção de alterações da posição das pálpebras que podem causar
                irritação ocular, lacrimejo, desconforto ou exposição da superfície ocular.
                """
            )

    with s2:
        with st.container(border=True):
            st.markdown("## 04 · Vias lacrimais")
            st.write(
                """
                Avaliação de lacrimejo persistente, obstruções lacrimais e alterações
                associadas à drenagem da lágrima.
                """
            )

        with st.container(border=True):
            st.markdown("## 05 · Lesões palpebrais")
            st.write(
                """
                Observação, diagnóstico, acompanhamento e eventual remoção de lesões
                localizadas nas pálpebras.
                """
            )

        with st.container(border=True):
            st.markdown("## 06 · Estética periocular")
            st.write(
                """
                Abordagem médica da estética do olhar, respeitando a anatomia,
                a função palpebral e a naturalidade facial.
                """
            )

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
# PÁGINA SOBRE
# =========================
elif pagina == "Sobre":
    col1, col2 = st.columns([0.85, 1.15])

    with col1:
        with st.container(border=True):
            st.markdown("## ⚕️")
            st.header("Blink Clinic")
            st.write("Clínica especializada em Oculoplástica")
            st.write("Pálpebras · Vias lacrimais · Órbita · Estética periocular")

        with st.container(border=True):
            st.markdown("## 🎯")
            st.subheader("Missão")
            st.write(
                """
                Cuidar da saúde, função e estética do olhar com rigor médico,
                comunicação clara e acompanhamento próximo.
                """
            )

    with col2:
        st.markdown(
            '<div class="section-label">Sobre a clínica</div>',
            unsafe_allow_html=True
        )
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

        st.markdown(
            """
            <div class="soft-box">
            A região periocular é delicada e expressiva. Por isso, cada tratamento
            deve respeitar a anatomia, a função ocular e a identidade facial.
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# PÁGINA INFORMAÇÃO CLÍNICA
# =========================
elif pagina == "Informação Clínica":
    st.markdown(
        '<div class="section-label">Educação do paciente</div>',
        unsafe_allow_html=True
    )
    st.header("Informação Clínica")

    a1, a2, a3 = st.columns(3)

    with a1:
        with st.container(border=True):
            st.markdown("## O que é a Oculoplástica?")
            st.write(
                """
                É uma área da oftalmologia dedicada ao diagnóstico e tratamento
                das pálpebras, vias lacrimais, órbita e região periocular.
                """
            )

    with a2:
        with st.container(border=True):
            st.markdown("## Quando procurar avaliação?")
            st.write(
                """
                Quando há queda das pálpebras, excesso de pele, lacrimejo,
                lesões palpebrais, irritação ocular ou alterações do olhar.
                """
            )

    with a3:
        with st.container(border=True):
            st.markdown("## A consulta substitui informação online?")
            st.write(
                """
                Não. A informação online é geral. A decisão clínica depende sempre
                de observação médica e avaliação individual.
                """
            )

    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    st.header("Temas frequentes")

    with st.expander("Blefaroplastia"):
        st.write(
            """
            A blefaroplastia pode ter finalidade funcional, estética ou ambas.
            A indicação depende da avaliação da pele, bolsas palpebrais, posição
            das pálpebras e impacto visual.
            """
        )

    with st.expander("Ptose palpebral"):
        st.write(
            """
            A ptose é a queda da pálpebra superior. Pode estar associada a queixas
            visuais, assimetria ou cansaço ocular.
            """
        )

    with st.expander("Lacrimejo persistente"):
        st.write(
            """
            O lacrimejo pode estar relacionado com alterações das vias lacrimais,
            inflamação ocular, alterações palpebrais ou outros fatores.
            """
        )

    with st.expander("Lesões palpebrais"):
        st.write(
            """
            Lesões nas pálpebras devem ser avaliadas para diagnóstico correto,
            seguimento e eventual tratamento.
            """
        )

# =========================
# PÁGINA CONTACTOS
# =========================
elif pagina == "Contactos":
    st.markdown(
        '<div class="section-label">Marcação</div>',
        unsafe_allow_html=True
    )
    st.header("Marcar Consulta")

    col1, col2 = st.columns([1, 1])

    with col1:
        with st.container(border=True):
            st.subheader("Pedido de marcação")
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
        with st.container(border=True):
            st.subheader("Blink Clinic")
            st.write("Oculoplástica")
            st.write("Pálpebras · Vias lacrimais · Órbita")
            st.write("Contacto: a definir")
            st.write("Localização: a definir")

        with st.container(border=True):
            st.subheader("Nota")
            st.write(
                """
                Esta aplicação é uma versão inicial. Para uso real com pacientes,
                é necessário configurar privacidade, proteção de dados e sistema
                seguro de marcações.
                """
            )

st.markdown(
    '<div class="footer">Blink Clinic · Oculoplástica · Saúde e estética do olhar</div>',
    unsafe_allow_html=True
)
