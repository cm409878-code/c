import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# Estilo visual simples e seguro
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fbf7ef;
        color: #062f3a;
    }

    [data-testid="stSidebar"] {
        background-color: #062f3a;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    .main-title {
        text-align: center;
        font-family: Georgia, serif;
        font-size: 64px;
        letter-spacing: 8px;
        color: #062f3a;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        font-family: Georgia, serif;
        font-size: 28px;
        color: #b1843f;
        font-style: italic;
        margin-top: 0;
    }

    .gold-line {
        height: 1px;
        background: #b1843f;
        margin: 25px 0 35px 0;
    }

    .card {
        background-color: white;
        padding: 28px;
        border-radius: 22px;
        border: 1px solid #d8b76d;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
        min-height: 260px;
    }

    .card-title {
        font-family: Georgia, serif;
        font-size: 28px;
        color: white;
        background-color: #062f3a;
        padding: 14px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
    }

    .card-title-gold {
        font-family: Georgia, serif;
        font-size: 28px;
        color: white;
        background-color: #b1843f;
        padding: 14px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
    }

    .card-title-rose {
        font-family: Georgia, serif;
        font-size: 28px;
        color: white;
        background-color: #d58b73;
        padding: 14px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
    }

    .icon {
        text-align: center;
        font-size: 55px;
        margin-bottom: 15px;
    }

    li {
        font-size: 17px;
        line-height: 1.7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho
st.markdown('<h1 class="main-title">BLINK CLINIC</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Oculoplástica · Planeamento Estratégico</p>', unsafe_allow_html=True)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# Primeira linha
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Proposta de Valor</div>
            <div class="icon">👁️</div>
            <ul>
                <li>Blefaroplastia estética e funcional</li>
                <li>Ptose palpebral, ectrópio e entrópio</li>
                <li>Reconstrução lacrimal e orbitária</li>
                <li>Abordagem médica personalizada</li>
                <li>Resultados naturais e discretos</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="card-title-rose">Pacientes</div>
            <div class="icon">👥</div>
            <ul>
                <li>Adultos com alterações palpebrais</li>
                <li>Pacientes com lacrimejo persistente</li>
                <li>Casos funcionais e estéticos</li>
                <li>Referenciados por oftalmologistas</li>
                <li>Público premium e exigente</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# Segunda linha
col3, col4 = st.columns(2)

with col3:
    st.markdown(
        """
        <div class="card">
            <div class="card-title-gold">Canais</div>
            <div class="icon">📱</div>
            <ul>
                <li>Website e marcação online</li>
                <li>Instagram e LinkedIn</li>
                <li>Parcerias médicas</li>
                <li>Indicação de pacientes</li>
                <li>Comunicação profissional e elegante</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Receitas</div>
            <div class="icon">€</div>
            <ul>
                <li>Consultas de especialidade</li>
                <li>Cirurgias estéticas privadas</li>
                <li>Cirurgias funcionais</li>
                <li>Procedimentos perioculares</li>
                <li>Acompanhamento pré e pós-operatório</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <h2 style="text-align:center; font-family:Georgia, serif; color:#062f3a;">
        Blink Clinic · Visão 2026
    </h2>
    """,
    unsafe_allow_html=True
)
