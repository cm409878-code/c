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
            background: #f7f1e7;
        }

        [data-testid="stSidebar"] {
            display: none;
        }

        .block-container {
            padding-top: 1rem;
            padding-left: 3rem;
            padding-right: 3rem;
            max-width: 1500px;
        }

        .page {
            background:
                radial-gradient(circle at top left, rgba(196, 157, 82, 0.16), transparent 25%),
                radial-gradient(circle at top right, rgba(218, 168, 135, 0.18), transparent 28%),
                linear-gradient(135deg, #fffaf1 0%, #f8efe3 50%, #fffdf8 100%);
            border-radius: 34px;
            padding: 45px;
            border: 1px solid rgba(177, 132, 63, 0.35);
            box-shadow: 0 24px 60px rgba(70, 48, 20, 0.14);
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
        }

        .brand {
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 76px;
            letter-spacing: 0.14em;
            color: #062f3a;
            font-weight: 500;
            margin-bottom: 5px;
        }

        .subtitle {
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 32px;
            color: #a47a3c;
            font-style: italic;
            margin-bottom: 20px;
        }

        .gold-line {
            width: 72%;
            height: 1px;
            margin: 20px auto 30px auto;
            background: linear-gradient(90deg, transparent, #b1843f, transparent);
        }

        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 28px;
        }

        .box {
            background: rgba(255, 255, 255, 0.78);
            border: 1px solid rgba(177, 132, 63, 0.38);
            border-radius: 28px;
            overflow: hidden;
            box-shadow: 0 16px 35px rgba(70, 48, 20, 0.12);
            min-height: 310px;
        }

        .box-title {
            font-family: Georgia, 'Times New Roman', serif;
            color: white;
            text-align: center;
            font-size: 30px;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            padding: 18px;
            text-shadow: 0 2px 6px rgba(0,0,0,0.22);
        }

        .navy {
            background: linear-gradient(135deg, #062f3a, #164b56);
        }

        .rose {
            background: linear-gradient(135deg, #d58b73, #e5ad99);
        }

        .gold {
            background: linear-gradient(135deg, #b1843f, #d8b76d);
        }

        .box-content {
            display: grid;
            grid-template-columns: 0.42fr 0.58fr;
            gap: 20px;
            padding: 30px;
            align-items: center;
        }

        .icon-area {
            text-align: center;
            font-size: 92px;
            color: #b1843f;
        }

        .euro-icon {
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 110px;
            color: #b1843f;
            font-weight: bold;
        }

        ul {
            margin: 0;
            padding-left: 22px;
        }

        li {
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 18px;
            line-height: 1.75;
            color: #20383d;
            margin-bottom: 6px;
        }

        li::marker {
            color: #0b3b45;
        }

        .footer {
            margin-top: 34px;
            text-align: center;
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 28px;
            color: #062f3a;
            font-style: italic;
        }

        .footer-line {
            width: 64%;
            height: 1px;
            margin: 18px auto;
            background: linear-gradient(90deg, transparent, #b1843f, transparent);
        }

        @media (max-width: 900px) {
            .brand {
                font-size: 42px;
                letter-spacing: 0.08em;
            }

            .subtitle {
                font-size: 22px;
            }

            .grid {
                grid-template-columns: 1fr;
            }

            .box-content {
                grid-template-columns: 1fr;
            }

            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
    </style>

    <div class="page">

        <div class="header">
            <div class="brand">BLINK CLINIC</div>
            <div class="subtitle">Oculoplástica · Planeamento Estratégico</div>
            <div class="gold-line"></div>
        </div>

        <div class="grid">

            <div class="box">
                <div class="box-title navy">Proposta de Valor</div>
                <div class="box-content">
                    <div class="icon-area">👁️</div>
                    <ul>
                        <li>Blefaroplastia estética e funcional</li>
                        <li>Ptose, ectrópio e entrópio</li>
                        <li>Reconstrução lacrimal e orbitária</li>
                        <li>Abordagem médica personalizada</li>
                        <li>Resultados naturais e discretos</li>
                    </ul>
                </div>
            </div>

            <div class="box">
                <div class="box-title rose">Clientes</div>
                <div class="box-content">
                    <div class="icon-area">👥</div>
                    <ul>
                        <li>Adultos 40+ com rejuvenescimento periocular</li>
                        <li>Patologia palpebral e lacrimal</li>
                        <li>Casos pós-traumáticos e oncológicos</li>
                        <li>Referenciados por oftalmologistas</li>
                        <li>Público premium e exigente</li>
                    </ul>
                </div>
            </div>

            <div class="box">
                <div class="box-title gold">Canais</div>
                <div class="box-content">
                    <div class="icon-area">📱</div>
                    <ul>
                        <li>Website e marcação online</li>
                        <li>Instagram e LinkedIn</li>
                        <li>Parcerias médicas multidisciplinares</li>
                        <li>Seguros de saúde e ADSE</li>
                        <li>Indicação de pacientes</li>
                    </ul>
                </div>
            </div>

            <div class="box">
                <div class="box-title navy">Receitas</div>
                <div class="box-content">
                    <div class="euro-icon">€</div>
                    <ul>
                        <li>Consultas de especialidade</li>
                        <li>Cirurgias estéticas privadas</li>
                        <li>Cirurgias funcionais comparticipadas</li>
                        <li>Procedimentos perioculares</li>
                        <li>Pacotes pré e pós-operatórios</li>
                    </ul>
                </div>
            </div>

        </div>

        <div class="footer-line"></div>
        <div class="footer">Blink Clinic · Visão 2026</div>

    </div>
    """,
    unsafe_allow_html=True
)
