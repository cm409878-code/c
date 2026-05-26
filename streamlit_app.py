import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

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
        background: rgba(255, 255, 255, 0.78);
        border-left: 5px solid #b1843f;
        padding: 20px 24px;
        border-radius: 16px;
        color: #34484d;
        margin-top: 18px;
        box-shadow: 0 8px 24px rgba(90, 65, 30, 0.08);
    }

    img {
        border-radius: 22px;
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

# Imagens por link
IMG_OCULOPLASTICA = "https://images.unsplash.com/photo-1494869042583-f6c911f04b4c?auto=format&fit=crop&w=1000&q=80"
IMG_OLHO = "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=1000&q=80"
IMG_MEDICO = "https://images.unsplash.com/photo-1582750433449-648ed127bb54?auto=format&fit=crop&w=1000&q=80"
IMG_CONSULTA = "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1000&q=80"
IMG_CLINICA = "https://images.unsplash.com/photo-151949402
