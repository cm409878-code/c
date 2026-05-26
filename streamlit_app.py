import streamlit as st

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fbf7ef 0%, #fffdf8 45%, #f3e8d8 100%);
    color: #062f3a;
}

[data-testid="stSidebar"] {
    display: none;
}

.block-container {
    padding-top: 1rem;
    padding-left: 4rem;
    padding-right: 4rem;
    max-width: 1400px;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px 0;
    border-bottom: 1px solid rgba(177, 132, 63, 0.35);
}

.logo {
    font-family: Georgia, serif;
    font-size: 34px;
    letter-spacing: 0.14em;
    color: #062f3a;
}

.nav span {
    margin-left: 22px;
    color: #8a6a38;
    font-weight: 600;
    font-size: 15px;
}

.hero {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 44px;
    align-items: center;
    padding: 70px 0;
}

.eyebrow {
    color: #b1843f;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 18px;
}

.hero-title {
    font-family: Georgia, serif;
    font-size: 72px;
    line-height: 1.02;
    color: #062f3a;
    margin-bottom: 24px;
}

.hero-text {
    font-size: 20px;
    line-height: 1.75;
    color: #4c5d61;
    max-width: 720px;
}

.button {
    display: inline-block;
    margin-top: 28px;
    margin-right: 12px;
    padding: 15px 26px;
    border-radius: 999px;
    font-weight: 800;
}

.button-dark {
    background: #062f3a;
    color: white;
    box-shadow: 0 12px 25px rgba(6, 47, 58, 0.22);
}

.button-light {
    background: rgba(255,255,255,0.7);
    color: #062f3a;
    border: 1px solid #b1843f;
}

.hero-card {
    background: linear-gradient(145deg, #ffffff, #f6ead8);
    border: 1px solid rgba(177, 132, 63, 0.45);
    border-radius: 34px;
    padding: 46px;
    box-shadow: 0 25px 60px rgba(90, 65, 30, 0.16);
    text-align: center;
}

.hero-card .icon {
    font-size: 92px;
    margin-bottom: 18px;
}

.hero-card h3 {
    font-family: Georgia, serif;
    color: #062f3a;
    font-size: 31px;
    margin-bottom: 14px;
}

.hero-card p {
    color: #5c625f;
    font-size: 17px;
    line-height: 1.7;
}

.section {
    padding: 58px 0;
    border-top: 1px solid rgba(177, 132, 63, 0.22);
}

.section-label {
    color: #b1843f;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 13px;
    font-weight: 900;
    margin-bottom: 10px;
}

.section-title {
    font-family: Georgia, serif;
    font-size: 46px;
    color: #062f3a;
    margin-bottom: 34px;
}

.grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 22px;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}

.card {
    background: white;
    border-radius: 26px;
    padding: 30px;
    border: 1px solid rgba(177, 132, 63, 0.28);
    box-shadow: 0 16px 35px rgba(90, 65, 30, 0.08);
    min-height: 245px;
}

.card-number {
    color: #b1843f;
    font-size: 22px;
    font-weight: 900;
    margin-bottom: 20px;
}

.card h3 {
    font-family: Georgia, serif;
    color: #062f3a;
    font-size: 24px;
    margin-bottom: 14px;
}

.card p {
    color: #566466;
    line-height: 1.68;
    font-size: 16px;
}

.about {
    display: grid;
    grid-template-columns: 0.9fr 1.1fr;
    gap: 40px;
    align-items: center;
}

.about-left {
    background: linear-gradient(145deg, #0b3440, #174e5d);
    color: white;
    border-radius: 34px;
    padding: 50px;
    min-height: 390px;
    box-shadow: 0 24px 55px rgba(6,47,58,0.20);
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
}

.about-left .icon {
    font-size: 88px;
    margin-bottom: 18px;
}

.about-left h3 {
    font-family: Georgia, serif;
    font-size: 36px;
    margin-bottom: 10px;
}

.about-right {
    background: rgba(255,255,255,0.74);
    border: 1px solid rgba(177, 132, 63, 0.28);
    border-radius: 34px;
    padding: 44px;
}

.about-right p {
    color: #4e5b5e;
    font-size: 18px;
    line-height: 1.85;
}

.bullet {
    margin: 13px 0;
    color: #34484d;
    font-size: 17px;
}

.contact-box {
    background: linear-gradient(135deg, #062f3a, #174e5d);
    color: white;
    border-radius: 34px;
    padding: 48px;
    text-align: center;
    box-shadow: 0 24px 55px rgba(6,47,58,0.20);
}

.contact-box h2 {
    font-family: Georgia, serif;
    font-size: 44px;
    margin-bottom: 14px;
}

.contact-box p {
    font-size: 18px;
    opacity: 0.92;
    line-height: 1.7;
}

.footer {
    text-align: center;
    padding: 38px 0 20px 0;
    color: #8a6a38;
    font-family: Georgia, serif;
    font-style: italic;
    font-size: 20px;
}

@media (max-width: 900px) {
    .hero, .about {
        grid-template-columns: 1fr;
    }

    .grid-4, .grid-3 {
        grid-template-columns: 1fr;
    }

    .hero-title {
        font-size: 46px;
    }

    .block-container {
        padding-left: 1.2rem;
        padding-right: 1.2rem;
    }

    .nav {
        display: none;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
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
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div>
        <div class="eyebrow">Oculoplástica · Pálpebras · Vias Lacrimais</div>
        <div class="hero-title">Oculoplástica com precisão e elegância</div>
        <div class="hero-text">
            Consultas, procedimentos e cirurgia periocular com uma abordagem médica personalizada,
            discreta e focada na saúde, função e harmonia do olhar.
        </div>
        <span class="button button-dark">Marcar Consulta</span>
        <span class="button button-light">Conhecer Serviços</span>
    </div>

    <div class="hero-card">
        <div class="icon">👁️</div>
        <h3>Saúde e estética do olhar</h3>
        <p>
            Uma clínica dedicada à região periocular, combinando rigor médico,
            sensibilidade estética e acompanhamento personalizado.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">O que fazemos</div>
    <div class="section-title">Serviços de Oculoplástica</div>

    <div class="grid-4">
        <div class="card">
            <div class="card-number">01</div>
            <h3>Consulta de Oculoplástica</h3>
            <p>Avaliação médica especializada das pálpebras, vias lacrimais, órbita e região periocular.</p>
        </div>

        <div class="card">
            <div class="card-number">02</div>
            <h3>Blefaroplastia</h3>
            <p>Cirurgia das pálpebras superiores e/ou inferiores, com objetivo funcional, estético ou combinado.</p>
        </div>

        <div class="card">
            <div class="card-number">03</div>
            <h3>Ptose Palpebral</h3>
            <p>Avaliação e tratamento da queda da pálpebra superior, quando afeta a visão ou a simetria do olhar.</p>
        </div>

        <div class="card">
            <div class="card-number">04</div>
            <h3>Vias Lacrimais</h3>
            <p>Diagnóstico e tratamento de lacrimejo persistente, obstruções lacrimais e alterações associadas.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="about">
        <div class="about-left">
            <div class="icon">⚕️</div>
            <h3>Blink Clinic</h3>
            <p>Clínica de Oculoplástica</p>
        </div>

        <div class="about-right">
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
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">Áreas clínicas</div>
    <div class="section-title">Outros tratamentos</div>

    <div class="grid-4">
        <div class="card">
            <div class="card-number">05</div>
            <h3>Entrópio e Ectrópio</h3>
            <p>Correção de alterações da posição das pálpebras que podem causar irritação, desconforto ocular ou lacrimejo.</p>
        </div>

        <div class="card">
            <div class="card-number">06</div>
            <h3>Lesões Palpebrais</h3>
            <p>Avaliação, acompanhamento e eventual remoção de lesões localizadas nas pálpebras.</p>
        </div>

        <div class="card">
            <div class="card-number">07</div>
            <h3>Órbita</h3>
            <p>Avaliação médica de alterações orbitárias e da região em redor do olho.</p>
        </div>

        <div class="card">
            <div class="card-number">08</div>
            <h3>Estética Periocular</h3>
            <p>Abordagem médica da estética do olhar, respeitando a anatomia e a naturalidade facial.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">Onde estamos</div>
    <div class="section-title">Localizações</div>

    <div class="grid-3">
        <div class="card">
            <h3>Lisboa</h3>
            <p>Consulta de Oculoplástica.</p>
            <p>Contacto a definir.</p>
        </div>

        <div class="card">
            <h3>Porto</h3>
            <p>Consulta e procedimentos.</p>
            <p>Contacto a definir.</p>
        </div>

        <div class="card">
            <h3>Online</h3>
            <p>Pedido de informação e pré-marcação.</p>
            <p>Formulário disponível brevemente.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">Saúde ocular</div>
    <div class="section-title">Artigos e informação</div>

    <div class="grid-3">
        <div class="card">
            <div class="card-number">Informação Clínica</div>
            <h3>O que é a Oculoplástica?</h3>
            <p>Uma área da oftalmologia dedicada às pálpebras, vias lacrimais, órbita e região periocular.</p>
        </div>

        <div class="card">
            <div class="card-number">Tratamentos</div>
            <h3>Blefaroplastia</h3>
            <p>Quando pode ser funcional, estética ou uma combinação das duas abordagens.</p>
        </div>

        <div class="card">
            <div class="card-number">Sintomas</div>
            <h3>Lacrimejo persistente</h3>
            <p>Quando o lacrimejo pode estar relacionado com alterações das vias lacrimais.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="contact-box">
        <h2>Marcar Consulta</h2>
        <p>
            Para avaliação em oculoplástica, cirurgia palpebral, vias lacrimais
            ou estética periocular.
        </p>
        <span class="button button-light" style="background:white; color:#062f3a;">
            Contactar a Blink Clinic
        </span>
    </div>
</div>

<div class="footer">
    Blink Clinic · Oculoplástica · Saúde e estética do olhar
</div>
""", unsafe_allow_html=True)
