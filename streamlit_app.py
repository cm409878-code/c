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
        background: linear-gradient(135deg, #fbf7ef 0%, #fffdf8 45%, #f3e8d8 100%);
        color: #062f3a;
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-left: 4rem;
        padding-right: 4rem;
        max-width: 1400px;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        color: #062f3a;
    }

    div.stButton > button {
        background-color: #062f3a;
        color: white;
        border-radius: 999px;
        padding: 0.7rem 1.5rem;
        border: none;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background-color: #b1843f;
        color: white;
        border: none;
    }

    [data-testid="stMetricValue"] {
        color: #b1843f;
    }

    .big-title {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 68px;
        letter-spacing: 10px;
        color: #062f3a;
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 28px;
        color: #b1843f;
        font-style: italic;
        margin-top: -10px;
    }

    .gold-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b1843f, transparent);
        margin: 25px 0 45px 0;
    }

    .section-label {
        color: #b1843f;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 800;
        font-size: 13px;
    }

    .soft-note {
        background: rgba(255, 255, 255, 0.7);
        border-left: 4px solid #b1843f;
        padding: 18px 22px;
        border-radius: 14px;
        color: #34484d;
        margin-top: 18px;
    }

    .footer {
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        color: #8a6a38;
        font-size: 22px;
        font-style: italic;
        margin-top: 40px;
    }

    img {
        border-radius: 24px;
    }

    @media (max-width: 900px) {
        .big-title {
            font-size: 42px;
            letter-spacing: 5px;
        }

        .subtitle {
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
# CABEÇALHO
# =========================
st.markdown('<div class="big-title">BLINK CLINIC</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Oculoplástica · Saúde e estética do olhar</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# HERO
# =========================
col1, col2 = st.columns([1.25, 0.75])

with col1:
    st.markdown(
        '<div class="section-label">Oculoplástica · Pálpebras · Vias Lacrimais</div>',
        unsafe_allow_html=True
    )

    st.title("Oculoplástica com precisão e elegância")

    st.write(
        """
        Consultas, procedimentos e cirurgia periocular com uma abordagem médica personalizada,
        discreta e focada na saúde, função e harmonia do olhar.
        """
    )

    b1, b2 = st.columns([1, 1])
    with b1:
        st.button("Marcar Consulta")
    with b2:
        st.button("Conhecer Serviços")

    st.markdown(
        """
        <div class="soft-note">
            Uma experiência clínica pensada para quem procura cuidado médico,
            discrição, segurança e naturalidade.
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.image(
        "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?auto=format&fit=crop&w=900&q=80",
        use_container_width=True
    )

    with st.container(border=True):
        st.subheader("Saúde e estética do olhar")
        st.write(
            """
            Uma clínica dedicada à região periocular, combinando rigor médico,
            sensibilidade estética e acompanhamento personalizado.
            """
        )

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# MÉTRICAS
# =========================
m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Especialidade", "Oculoplástica")

with m2:
    st.metric("Foco clínico", "Pálpebras")

with m3:
    st.metric("Abordagem", "Premium")

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# SERVIÇOS
# =========================
st.markdown(
    '<div class="section-label">O que fazemos</div>',
    unsafe_allow_html=True
)
st.header("Serviços de Oculoplástica")

st.image(
    "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=1400&q=80",
    use_container_width=True
)

s1, s2, s3, s4 = st.columns(4)

with s1:
    with st.container(border=True):
        st.markdown("### 01")
        st.subheader("Consulta de Oculoplástica")
        st.write(
            """
            Avaliação médica especializada das pálpebras, vias lacrimais,
            órbita e região periocular.
            """
        )

with s2:
    with st.container(border=True):
        st.markdown("### 02")
        st.subheader("Blefaroplastia")
        st.write(
            """
            Cirurgia das pálpebras superiores e/ou inferiores, com objetivo
            funcional, estético ou combinado.
            """
        )

with s3:
    with st.container(border=True):
        st.markdown("### 03")
        st.subheader("Ptose Palpebral")
        st.write(
            """
            Avaliação e tratamento da queda da pálpebra superior, quando afeta
            a visão ou a simetria do olhar.
            """
        )

with s4:
    with st.container(border=True):
        st.markdown("### 04")
        st.subheader("Vias Lacrimais")
        st.write(
            """
            Diagnóstico e tratamento de lacrimejo persistente, obstruções
            lacrimais e alterações associadas.
            """
        )

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# SOBRE A CLÍNICA
# =========================
col3, col4 = st.columns([0.85, 1.15])

with col3:
    st.image(
        "https://images.unsplash.com/photo-1580281657527-47f249e8f4df?auto=format&fit=crop&w=900&q=80",
        use_container_width=True
    )

    with st.container(border=True):
        st.header("Blink Clinic")
        st.write("Clínica de Oculoplástica")
        st.write("Pálpebras · Vias lacrimais · Órbita · Estética periocular")

with col4:
    st.markdown(
        '<div class="section-label">Sobre a clínica</div>',
        unsafe_allow_html=True
    )

    st.header("Cuidar do olhar com rigor médico")

    st.write(
        """
        A Blink Clinic é dedicada à avaliação e tratamento das alterações das pálpebras,
        vias lacrimais, órbita e região periocular. A abordagem combina segurança clínica,
        detalhe técnico e atenção à harmonia estética.
        """
    )

    st.write("• Avaliação individualizada de cada paciente")
    st.write("• Foco em resultados naturais e discretos")
    st.write("• Tratamento funcional e estético da região periocular")
    st.write("• Comunicação clara e acompanhamento cuidadoso")

    st.markdown(
        """
        <div class="soft-note">
            A missão da Blink Clinic é unir precisão médica, estética natural
            e acompanhamento próximo em cada etapa do cuidado periocular.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# OUTROS TRATAMENTOS
# =========================
st.markdown(
    '<div class="section-label">Áreas clínicas</div>',
    unsafe_allow_html=True
)
st.header("Outros tratamentos")

t1, t2, t3, t4 = st.columns(4)

with t1:
    with st.container(border=True):
        st.image(
            "https://images.unsplash.com/photo-1530497610245-94d3c16cda28?auto=format&fit=crop&w=700&q=80",
            use_container_width=True
        )
        st.subheader("Entrópio e Ectrópio")
        st.write(
            """
            Correção de alterações da posição das pálpebras que podem causar
            irritação, desconforto ou lacrimejo.
            """
        )

with t2:
    with st.container(border=True):
        st.image(
            "https://images.unsplash.com/photo-1584515933487-779824d29309?auto=format&fit=crop&w=700&q=80",
            use_container_width=True
        )
        st.subheader("Lesões Palpebrais")
        st.write(
            """
            Avaliação, acompanhamento e eventual remoção de lesões localizadas
            nas pálpebras.
            """
        )

with t3:
    with st.container(border=True):
        st.image(
            "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=700&q=80",
            use_container_width=True
        )
        st.subheader("Órbita")
        st.write(
            """
            Avaliação médica de alterações orbitárias e da região em redor do olho.
            """
        )

with t4:
    with st.container(border=True):
        st.image(
            "https://images.unsplash.com/photo-1606811971618-4486d14f3f99?auto=format&fit=crop&w=700&q=80",
            use_container_width=True
        )
        st.subheader("Estética Periocular")
        st.write(
            """
            Abordagem médica da estética do olhar, respeitando a anatomia
            e a naturalidade facial.
            """
        )

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# LOCALIZAÇÕES
# =========================
st.markdown(
    '<div class="section-label">Onde estamos</div>',
    unsafe_allow_html=True
)
st.header("Localizações")

l1, l2, l3 = st.columns(3)

with l1:
    with st.container(border=True):
        st.subheader("Lisboa")
        st.write("Consulta de Oculoplástica")
        st.write("Contacto a definir")

with l2:
    with st.container(border=True):
        st.subheader("Porto")
        st.write("Consulta e procedimentos")
        st.write("Contacto a definir")

with l3:
    with st.container(border=True):
        st.subheader("Online")
        st.write("Pedido de informação e pré-marcação")
        st.write("Formulário disponível brevemente")

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# ARTIGOS
# =========================
st.markdown(
    '<div class="section-label">Saúde ocular</div>',
    unsafe_allow_html=True
)
st.header("Artigos e informação")

a1, a2, a3 = st.columns(3)

with a1:
    with st.container(border=True):
        st.image(
            "https://images.unsplash.com/photo-1551190822-a9333d879b1f?auto=format&fit=crop&w=700&q=80",
            use_container_width=True
        )
        st.subheader("O que é a Oculoplástica?")
        st.write(
            """
            Área da oftalmologia dedicada às pálpebras, vias lacrimais,
            órbita e região periocular.
            """
        )

with a2:
    with st.container(border=True):
        st.image(
            "https://images.unsplash.com/photo-1582750433449-648ed127bb54?auto=format&fit=crop&w=700&q=80",
            use_container_width=True
        )
        st.subheader("Blefaroplastia")
        st.write(
            """
            Quando pode ser funcional, estética ou uma combinação das duas abordagens.
            """
        )

with a3:
    with st.container(border=True):
        st.image(
            "https://images.unsplash.com/photo-1581093458791-9f3c3900df7b?auto=format&fit=crop&w=700&q=80",
            use_container_width=True
        )
        st.subheader("Lacrimejo persistente")
        st.write(
            """
            Quando o lacrimejo pode estar relacionado com alterações das vias lacrimais.
            """
        )

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# =========================
# CONTACTO
# =========================
with st.container(border=True):
    c1, c2 = st.columns([1, 1])

    with c1:
        st.header("Marcar Consulta")
        st.write(
            """
            Para avaliação em oculoplástica, cirurgia palpebral, vias lacrimais
            ou estética periocular.
            """
        )
        st.button("Contactar a Blink Clinic")

    with c2:
        st.image(
            "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w=900&q=80",
            use_container_width=True
        )

st.markdown(
    '<div class="footer">Blink Clinic · Oculoplástica · Saúde e estética do olhar</div>',
    unsafe_allow_html=True
)
