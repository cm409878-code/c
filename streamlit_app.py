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
        background: #fbf8f1;
        color: #17333b;
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    .block-container {
        padding-top: 0rem;
        padding-left: 4rem;
        padding-right: 4rem;
        max-width: 1400px;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
    }

    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 26px 0;
        border-bottom: 1px solid rgba(174, 133, 65, 0.35);
        margin-bottom: 30px;
    }

    .logo {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 32px;
        letter-spacing: 0.12em;
        color: #062f3a;
        font-weight: 500;
    }

    .nav {
        font-size: 15px;
        color: #6d5a3b;
    }

    .nav span {
        margin-left: 24px;
    }

    .hero {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 40px;
        align-items: center;
        padding: 60px 0 70px 0;
    }

    .eyebrow {
        color: #b28a43;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 18px;
    }

    .hero-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 72px;
        line-height: 1.02;
        color: #062f3a;
        margin-bottom: 24px;
    }

    .hero-text {
        font-size: 20px;
        line-height: 1.7;
        color: #4c5d61;
        max-width: 700px;
        margin-bottom: 30px;
    }

    .button-row {
        margin-top: 28px;
    }

    .primary-button {
        display: inline-block;
        background: #062f3a;
        color: white;
        padding: 15px 25px;
        border-radius: 999px;
        text-decoration: none;
        font-weight: 700;
        margin-right: 14px;
        box-shadow: 0 12px 25px rgba(6,47,58,0.22);
    }

    .secondary-button {
        display: inline-block;
        border: 1px solid #b28a43;
        color: #062f3a;
        padding: 14px 24px;
        border-radius: 999px;
        text-decoration: none;
        font-weight: 700;
        background: rgba(255,255,255,0.65);
    }

    .hero-card {
        background: linear-gradient(145deg, #ffffff, #f6ead8);
        border: 1px solid rgba(178, 138, 67, 0.45);
        border-radius: 34px;
        padding: 42px;
        box-shadow: 0 25px 60px rgba(90, 65, 30, 0.16);
        text-align: center;
    }

    .eye-symbol {
        font-size: 96px;
        margin-bottom: 18px;
    }

    .hero-card h3 {
        font-size: 30px;
        color: #062f3a;
        margin-bottom: 12px;
    }

    .hero-card p {
        color: #5c625f;
        font-size: 17px;
        line-height: 1.6;
    }

    .section {
        padding: 55px 0;
        border-top: 1px solid rgba(178, 138, 67, 0.20);
    }

    .section-label {
        color: #b28a43;
        text-transform: uppercase;
        letter-spacing: 0.16em;
        font-size: 13px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .section-title {
        font-size: 44px;
        color: #062f3a;
        margin-bottom: 32px;
        font-family: Georgia, "Times New Roman", serif;
    }

    .service-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 22px;
    }

    .service-card {
        background: #ffffff;
        border-radius: 26px;
        padding: 30px;
        border: 1px solid rgba(178, 138, 67, 0.28);
        box-shadow: 0 16px 35px rgba(90, 65, 30, 0.08);
        min-height: 260px;
    }

    .number {
        color: #b28a43;
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 20px;
    }

    .service-card h3 {
        color: #062f3a;
        font-size: 25px;
        margin-bottom: 14px;
    }

    .service-card p {
        color: #566466;
        line-height: 1.65;
        font-size: 16px;
    }

    .about {
        display: grid;
        grid-template-columns: 0.9fr 1.1fr;
        gap: 40px;
        align-items: center;
    }

    .portrait-card {
        background: linear-gradient(145deg, #0b3440, #174e5d);
        color: white;
        border-radius: 34px;
        padding: 48px;
        min-height: 420px;
        box-shadow: 0 24px 55px rgba(6,47,58,0.20);
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }

    .portrait-card .icon {
        font-size: 90px;
        margin-bottom: 18px;
    }

    .portrait-card h3 {
        font-size: 34px;
        margin-bottom: 10px;
    }

    .about-text {
        background: rgba(255,255,255,0.70);
        border: 1px solid rgba(178, 138, 67, 0.28);
        border-radius: 34px;
        padding: 42px;
    }

    .about-text p {
        color: #4e5b5e;
        font-size: 18px;
        line-height: 1.8;
    }

    .bullet {
        margin: 12px 0;
        color: #34484d;
        font-size: 17px;
    }

    .locations {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 22px;
    }

    .location-card {
        background: #ffffff;
        border-radius: 24px;
        padding: 26px;
        border: 1px solid rgba(178, 138, 67, 0.26);
        box-shadow: 0 12px 28px rgba(90, 65, 30, 0.07);
    }

    .location-card h3 {
        color: #062f3a;
        font-size: 24px;
        margin-bottom: 8px;
    }

    .location-card p {
        color: #5c625f;
        font-size: 16px;
    }

    .article-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 22px;
    }

    .article-card {
        background: #ffffff;
        border-radius: 26px;
        padding: 30px;
        border: 1px solid rgba(178, 138, 67, 0.28);
        box-shadow: 0 16px 35px rgba(90, 65, 30, 0.08);
        min-height: 230px;
    }

    .date {
        color: #b28a43;
        font-weight: 700;
        font-size: 14px;
        margin-bottom: 12px;
    }

    .contact-box {
        background: linear-gradient(135deg, #062f3a, #174e5d);
        color: white;
        border-radius: 34px;
        padding: 45px;
        text-align: center;
        box-shadow: 0 24px 55px rgba(6,47,58,0.20);
    }

    .contact-box h2 {
        font-size: 44px;
        margin-bottom: 14px;
    }

    .contact-box p {
        font-size: 18px;
        opacity: 0.9;
    }

    .footer {
        text-align: center;
        padding: 35px 0 20px 0;
        color: #8a6a38;
        font-family: Georgia, "Times New Roman", serif;
        font-style: italic;
        font-size: 20px;
    }

    @media (max-width: 900px) {
        .hero, .about {
            grid-template-columns: 1fr;
        }

        .service-grid, .locations, .article-grid {
            grid-template-columns: 1fr;
        }

        .hero-title {
            font-size: 48px;
        }

        .block-container {
            padding-left: 1.5rem;
            padding-right: 1.5rem;
        }

        .nav {
            display: none;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="topbar">
        <div class="logo">BLINK CLINIC</div>
        <div class="nav">
            <span>Início</span>
            <span>Sobre</span>
            <span>Serviços</span>
            <span>Localizações</span>
            <span>Artigos</span>
            <span>Contacto</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <div>
            <div class="eyebrow">Oculoplástica · Pálpebras · Vias Lacrimais</div>
            <div class="hero-title">Oculoplástica com precisão e elegância</div>
            <div class="hero-text">
                Consultas, procedimentos e cirurgia periocular com uma abordagem médica personalizada,
                discreta e focada na saúde, função e harmonia do olhar.
            </div>
            <div class="button-row">
                <span class="primary-button">Marcar Consulta</span>
                <span class="secondary-button">Conhecer Serviços</span>
            </div>
        </div>

        <div class="hero-card">
            <div class="eye-symbol">👁️</div>
            <h3>Saúde e estética do olhar</h3>
            <p>
                Uma clínica dedicada à região periocular, combinando rigor médico,
                sensibilidade estética e acompanhamento personalizado.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">
        <div class="section-label">O que fazemos</div>
        <div class="section-title">Serviços de Oculoplástica</div>

        <div class="service-grid">
            <div class="service-card">
                <div class="number">01</div>
                <h3>Consulta de Oculoplástica</h3>
                <p>
                Avaliação médica especializada das pálpebras, vias lacrimais,
                órbita e região periocular.
                </p>
            </div>

            <div class="service-card">
                <div class="number">02</div>
                <h3>Blefaroplastia</h3>
                <p>
                Cirurgia das pálpebras superiores e/ou inferiores, com objetivo funcional,
                estético ou combinado.
                </p>
            </div>

            <div class="service-card">
                <div class="number">03</div>
                <h3>Ptose Palpebral</h3>
                <p>
                Avaliação e tratamento da queda da pálpebra superior, quando afeta
                a visão ou a simetria do olhar.
                </p>
            </div>

            <div class="service-card">
                <div class="number">04</div>
                <h3>Vias Lacrimais</h3>
                <p>
                Diagnóstico e tratamento de lacrimejo persistente, obstruções
                lacrimais e alterações associadas.
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">
        <div class="about">
            <div class="portrait-card">
                <div class="icon">⚕️</div>
                <h3>Blink Clinic</h3>
                <p>Clínica de Oculoplástica</p>
            </div>

            <div class="about-text">
                <div class="section-label">Sobre a clínica</div>
                <div class="section-title">Cuidar do olhar com rigor médico</div>
                <p>
                A Blink Clinic é dedicada à avaliação e tratamento das alterações das pálpebras,
                vias lacrimais, órbita e região periocular. A abordagem combina segurança clínica,
                detalhe técnico e atenção à harmonia estética.
                </p>

                <div class="bullet">• Avaliação individualizada de cada paciente</div>
                <div class="bullet">• Foco em resultados naturais e discretos</div>
                <div class="bullet">• Tratamento funcional e estético da região periocular</div>
                <div class="bullet">• Comunicação clara e acompanhamento cuidadoso</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">
        <div class="section-label">Áreas clínicas</div>
        <div class="section-title">Outros tratamentos</div>

        <div class="service-grid">
            <div class="service-card">
                <div class="number">05</div>
                <h3>Entrópio e Ectrópio</h3>
                <p>Correção de alterações da posição das pálpebras que podem causar irritação, desconforto ou lacrimejo.</p>
            </div>

            <div class="service-card">
                <div class="number">06</div>
                <h3>Lesões Palpebrais</h3>
                <p>Avaliação, acompanhamento e eventual remoção de lesões localizadas nas pálpebras.</p>
            </div>

            <div class="service-card">
                <div class="number">07</div>
                <h3>Órbita</h3>
                <p>Avaliação médica de alterações orbitárias e da região em redor do olho.</p>
            </div>

            <div class="service-card">
                <div class="number">08</div>
                <h3>Estética Periocular</h3>
                <p>Abordagem médica da estética do olhar, respeitando a anatomia e a naturalidade facial.</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">
        <div class="section-label">Onde estamos</div>
        <div class="section-title">Localizações</div>

        <div class="locations">
            <div class="location-card">
                <h3>Lisboa</h3>
                <p>Consulta de Oculoplástica</p>
                <p>Contacto a definir</p>
            </div>

            <div class="location-card">
                <h3>Porto</h3>
                <p>Consulta e procedimentos</p>
                <p>Contacto a definir</p>
            </div>

            <div class="location-card">
                <h3>Online</h3>
                <p>Pedido de informação e pré-marcação</p>
                <p>Formulário disponível brevemente</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">
        <div class="section-label">Saúde ocular</div>
        <div class="section-title">Artigos e informação</div>

        <div class="article-grid">
            <div class="article-card">
                <div class="date">Informação Clínica</div>
                <h3>O que é a Oculoplástica?</h3>
                <p>Uma área da oftalmologia dedicada às pálpebras, vias lacrimais, órbita e região periocular.</p>
            </div>

            <div class="article-card">
                <div class="date">Tratamentos</div>
                <h3>Blefaroplastia</h3>
                <p>Quando pode ser funcional, estética ou uma combinação das duas abordagens.</p>
            </div>

            <div class="article-card">
                <div class="date">Sintomas</div>
                <h3>Lacrimejo persistente</h3>
                <p>Quando o lacrimejo pode estar relacionado com alterações das vias lacrimais.</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">
        <div class="contact-box">
            <h2>Marcar Consulta</h2>
            <p>
            Para avaliação em oculoplástica, cirurgia palpebral, vias lacrimais
            ou estética periocular.
            </p>
            <br>
            <span class="primary-button" style="background:white;color:#062f3a;">Contactar a Blink Clinic</span>
        </div>
    </div>

    <div class="footer">
        Blink Clinic · Oculoplástica · Saúde e estética do olhar
    </div>
    """,
    unsafe_allow_html=True
)
