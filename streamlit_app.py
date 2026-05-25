import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

if "pacientes" not in st.session_state:
    st.session_state.pacientes = []

if "consultas" not in st.session_state:
    st.session_state.consultas = []

if "tarefas" not in st.session_state:
    st.session_state.tarefas = []


st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(201, 164, 93, 0.18), transparent 28%),
            radial-gradient(circle at top right, rgba(218, 157, 138, 0.20), transparent 30%),
            linear-gradient(135deg, #fbf7ef 0%, #fffdf8 50%, #f6eadc 100%);
        color: #18323a;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #082f3a 0%, #123f49 60%, #8a6a38 100%);
        border-right: 1px solid rgba(218, 184, 112, 0.4);
    }

    [data-testid="stSidebar"] * {
        color: #fff8ea !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        letter-spacing: 0.02em;
    }

    .hero {
        background:
            linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,248,235,0.96));
        border: 1px solid rgba(196, 157, 82, 0.45);
        border-radius: 34px;
        padding: 52px 40px;
        text-align: center;
        box-shadow: 0 22px 60px rgba(79, 55, 26, 0.14);
        margin-bottom: 34px;
        position: relative;
        overflow: hidden;
    }

    .hero::before {
        content: "◜";
        position: absolute;
        left: 30px;
        top: 10px;
        font-size: 140px;
        color: rgba(196, 157, 82, 0.16);
    }

    .hero::after {
        content: "◝";
        position: absolute;
        right: 30px;
        top: 10px;
        font-size: 140px;
        color: rgba(196, 157, 82, 0.16);
    }

    .brand-title {
        font-size: 68px;
        font-weight: 500;
        color: #082f3a;
        letter-spacing: 0.16em;
        margin-bottom: 4px;
    }

    .brand-subtitle {
        font-size: 30px;
        color: #a47a3c;
        font-style: italic;
        margin-bottom: 24px;
    }

    .gold-line {
        width: 72%;
        height: 1px;
        background: linear-gradient(90deg, transparent, #c9a45d, transparent);
        margin: 22px auto;
    }

    .tag {
        display: inline-block;
        background: #f7ead7;
        color: #143c46;
        border: 1px solid rgba(196, 157, 82, 0.45);
        padding: 9px 16px;
        border-radius: 999px;
        font-size: 14px;
        font-weight: 700;
        margin: 6px;
    }

    .panel {
        background: rgba(255,255,255,0.82);
        border: 1px solid rgba(196, 157, 82, 0.42);
        border-radius: 28px;
        overflow: hidden;
        box-shadow: 0 18px 45px rgba(79, 55, 26, 0.12);
        margin-bottom: 26px;
        min-height: 335px;
    }

    .panel-header-navy {
        background: linear-gradient(135deg, #082f3a, #164b56);
        color: white;
        padding: 18px 24px;
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 28px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .panel-header-gold {
        background: linear-gradient(135deg, #b1843f, #d6b36a);
        color: white;
        padding: 18px 24px;
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 28px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .panel-header-rose {
        background: linear-gradient(135deg, #d89178, #e9b09c);
        color: white;
        padding: 18px 24px;
        text-align: center;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 28px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .panel-content {
        padding: 30px 34px;
        font-size: 17px;
        line-height: 1.85;
        color: #253b40;
    }

    .big-icon {
        font-size: 74px;
        text-align: center;
        margin-bottom: 10px;
        color: #b1843f;
    }

    .lux-card {
        background: rgba(255,255,255,0.9);
        border: 1px solid rgba(196, 157, 82, 0.35);
        border-radius: 26px;
        padding: 26px;
        box-shadow: 0 14px 36px rgba(79, 55, 26, 0.10);
        margin-bottom: 20px;
    }

    .lux-card h3 {
        color: #082f3a;
        font-size: 25px;
        margin-bottom: 10px;
    }

    .lux-card p {
        color: #4f5b5d;
        font-size: 16px;
        line-height: 1.6;
    }

    .metric-card {
        background: linear-gradient(180deg, #ffffff, #fff7eb);
        border: 1px solid rgba(196, 157, 82, 0.38);
        border-radius: 24px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 14px 35px rgba(79, 55, 26, 0.10);
    }

    .metric-number {
        font-size: 42px;
        font-weight: 900;
        color: #a47a3c;
    }

    .metric-label {
        color: #143c46;
        font-weight: 700;
    }

    div.stButton > button:first-child {
        background: linear-gradient(135deg, #082f3a 0%, #b1843f 100%);
        color: white;
        border: none;
        border-radius: 999px;
        padding: 0.75rem 1.5rem;
        font-weight: 800;
        box-shadow: 0 10px 22px rgba(79, 55, 26, 0.22);
    }

    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        color: white;
        border: none;
    }

    .footer {
        text-align: center;
        color: #8a6a38;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 22px;
        font-style: italic;
        margin-top: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def panel(titulo, cor, icon, bullets):
    header_class = {
        "navy": "panel-header-navy",
        "gold": "panel-header-gold",
        "rose": "panel-header-rose"
    }[cor]

    items = "".join([f"<li>{b}</li>" for b in bullets])

    st.markdown(
        f"""
        <div class="panel">
            <div class="{header_class}">{titulo}</div>
            <div class="panel-content">
                <div class="big-icon">{icon}</div>
                <ul>{items}</ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_card(numero, texto):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-number">{numero}</div>
            <div class="metric-label">{texto}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.sidebar.markdown("## BLINK CLINIC")
st.sidebar.markdown("### Oculoplástica")
st.sidebar.caption("Planeamento estratégico · Visão 2026")
st.sidebar.divider()

pagina = st.sidebar.radio(
    "Menu",
    [
        "Início",
        "Serviços",
        "Pacientes",
        "Consultas",
        "Informação Clínica",
        "Marketing",
        "Tarefas"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Elegância clínica · Saúde do olhar")


if pagina == "Início":
    st.markdown(
        """
        <div class="hero">
            <div class="brand-title">BLINK CLINIC</div>
            <div class="brand-subtitle">Oculoplástica · Planeamento Estratégico</div>
            <div class="gold-line"></div>
            <span class="tag">Blefaroplastia</span>
            <span class="tag">Ptose Palpebral</span>
            <span class="tag">Vias Lacrimais</span>
            <span class="tag">Órbita</span>
            <span class="tag">Estética Periocular</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(len(st.session_state.pacientes), "Pacientes registados")

    with col2:
        metric_card(len(st.session_state.consultas), "Consultas agendadas")

    with col3:
        metric_card(len(st.session_state.tarefas), "Tarefas internas")

    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        panel(
            "Proposta de Valor",
            "navy",
            "👁️",
            [
                "Blefaroplastia estética e funcional",
                "Ptose, ectrópio e entrópio",
                "Reconstrução lacrimal e orbitária",
                "Abordagem médica personalizada",
                "Resultados naturais e discretos"
            ]
        )

    with c2:
        panel(
            "Clientes",
            "rose",
            "👥",
            [
                "Adultos 40+ com rejuvenescimento periocular",
                "Patologia palpebral e lacrimal",
                "Casos pós-traumáticos e oncológicos",
                "Referenciados por oftalmologistas",
                "Público premium e exigente"
            ]
        )

    c3, c4 = st.columns(2)

    with c3:
        panel(
            "Canais",
            "gold",
            "📱",
            [
                "Website e marcação online",
                "Instagram e LinkedIn",
                "Parcerias médicas multidisciplinares",
                "Seguros de saúde e ADSE",
                "Indicação de pacientes"
            ]
        )

    with c4:
        panel(
            "Receitas",
            "navy",
            "€",
            [
                "Consultas de especialidade",
                "Cirurgias estéticas privadas",
                "Cirurgias funcionais comparticipadas",
                "Procedimentos perioculares",
                "Pacotes pré e pós-operatórios"
            ]
        )

    st.markdown(
        """
        <div class="footer">
            Blink Clinic · Visão 2026
        </div>
        """,
        unsafe_allow_html=True
    )


elif pagina == "Serviços":
    st.title("Serviços de Oculoplástica")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="lux-card">
                <h3>Blefaroplastia</h3>
                <p>Cirurgia das pálpebras superiores e/ou inferiores, com finalidade funcional, estética ou combinada.</p>
            </div>
            <div class="lux-card">
                <h3>Ptose Palpebral</h3>
                <p>Avaliação e tratamento da queda da pálpebra superior, com impacto funcional ou estético.</p>
            </div>
            <div class="lux-card">
                <h3>Entrópio e Ectrópio</h3>
                <p>Correção de alterações da posição das pálpebras que podem causar desconforto ocular.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="lux-card">
                <h3>Vias Lacrimais</h3>
                <p>Avaliação de lacrimejo persistente, obstrução lacrimal e alterações do sistema lacrimal.</p>
            </div>
            <div class="lux-card">
                <h3>Lesões Palpebrais</h3>
                <p>Diagnóstico, acompanhamento e eventual remoção de lesões palpebrais.</p>
            </div>
            <div class="lux-card">
                <h3>Órbita e Estética Periocular</h3>
                <p>Avaliação da região orbitária e abordagem estética médica da área periocular.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


elif pagina == "Pacientes":
    st.title("Pacientes")

    with st.form("form_paciente"):
        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input("Nome do paciente")
            contacto = st.text_input("Contacto")
            email = st.text_input("Email")

        with col2:
            motivo = st.selectbox(
                "Motivo principal",
                [
                    "Consulta de Oculoplástica",
                    "Blefaroplastia",
                    "Ptose palpebral",
                    "Entrópio / Ectrópio",
                    "Vias lacrimais",
                    "Lesão palpebral",
                    "Avaliação da órbita",
                    "Estética periocular",
                    "Outro"
                ]
            )
            notas = st.text_area("Notas administrativas")

        guardar = st.form_submit_button("Guardar paciente")

    if guardar:
        if nome.strip() == "":
            st.warning("Escreve o nome do paciente.")
        else:
            st.session_state.pacientes.append(
                {
                    "Nome": nome,
                    "Contacto": contacto,
                    "Email": email,
                    "Motivo": motivo,
                    "Notas": notas
                }
            )
            st.success(f"Paciente {nome} guardado com sucesso.")

    if len(st.session_state.pacientes) > 0:
        st.table(st.session_state.pacientes)
    else:
        st.info("Ainda não há pacientes registados.")


elif pagina == "Consultas":
    st.title("Consultas")

    with st.form("form_consulta"):
        col1, col2 = st.columns(2)

        with col1:
            paciente = st.text_input("Nome do paciente")
            tipo = st.selectbox(
                "Tipo de consulta/procedimento",
                [
                    "Consulta de Oculoplástica",
                    "Reavaliação",
                    "Blefaroplastia",
                    "Ptose palpebral",
                    "Vias lacrimais",
                    "Lesão palpebral",
                    "Procedimento periocular",
                    "Outro"
                ]
            )

        with col2:
            data_consulta = st.date_input("Data", date.today())
            hora_consulta = st.time_input("Hora")
            observacoes = st.text_area("Observações")

        guardar = st.form_submit_button("Guardar consulta")

    if guardar:
        if paciente.strip() == "":
            st.warning("Escreve o nome do paciente.")
        else:
            st.session_state.consultas.append(
                {
                    "Paciente": paciente,
                    "Tipo": tipo,
                    "Data": str(data_consulta),
                    "Hora": str(hora_consulta),
                    "Observações": observacoes
                }
            )
            st.success("Consulta guardada com sucesso.")

    if len(st.session_state.consultas) > 0:
        st.table(st.session_state.consultas)
    else:
        st.info("Ainda não há consultas guardadas.")


elif pagina == "Informação Clínica":
    st.title("Informação Clínica")

    st.markdown(
        """
        <div class="lux-card">
            <h3>O que é a oculoplástica?</h3>
            <p>
            A oculoplástica é uma área da oftalmologia dedicada às pálpebras,
            vias lacrimais, órbita e região periocular.
            </p>
        </div>

        <div class="lux-card">
            <h3>Quando procurar avaliação?</h3>
            <p>
            Alterações das pálpebras, lacrimejo persistente, lesões palpebrais,
            desconforto ocular, assimetrias ou alterações estéticas do olhar.
            </p>
        </div>

        <div class="lux-card">
            <h3>Abordagem médica</h3>
            <p>
            Cada paciente deve ser avaliado individualmente, considerando saúde ocular,
            função palpebral, segurança e harmonia estética.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


elif pagina == "Marketing":
    st.title("Marketing")

    tema = st.selectbox(
        "Escolhe um tema",
        [
            "Apresentação da clínica",
            "O que é oculoplástica",
            "Blefaroplastia",
            "Ptose palpebral",
            "Vias lacrimais",
            "Lesões palpebrais",
            "Cuidados no pós-operatório"
        ]
    )

    ideias = {
        "Apresentação da clínica": "A Blink Clinic nasce para cuidar da saúde, função e estética do olhar, com uma abordagem médica personalizada e elegante.",
        "O que é oculoplástica": "A oculoplástica dedica-se ao tratamento das pálpebras, vias lacrimais, órbita e região periocular.",
        "Blefaroplastia": "A blefaroplastia pode ter objetivos funcionais e/ou estéticos, dependendo da avaliação médica individual.",
        "Ptose palpebral": "A ptose palpebral é a queda da pálpebra superior e pode interferir com o campo visual ou com a simetria do olhar.",
        "Vias lacrimais": "O lacrimejo persistente pode estar associado a alterações das vias lacrimais e deve ser avaliado em consulta.",
        "Lesões palpebrais": "Lesões nas pálpebras devem ser observadas para diagnóstico e orientação adequada.",
        "Cuidados no pós-operatório": "O acompanhamento médico e o cumprimento das indicações pós-operatórias são fundamentais para uma boa recuperação."
    }

    if st.button("Gerar texto"):
        st.markdown(
            f"""
            <div class="lux-card">
                <h3>Texto sugerido</h3>
                <p>{ideias[tema]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


elif pagina == "Tarefas":
    st.title("Tarefas internas")

    with st.form("form_tarefas"):
        tarefa = st.text_input("Nova tarefa")
        prioridade = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
        prazo = st.date_input("Prazo", date.today())
        guardar = st.form_submit_button("Adicionar tarefa")

    if guardar:
        if tarefa.strip() == "":
            st.warning("Escreve uma tarefa.")
        else:
            st.session_state.tarefas.append(
                {
                    "Tarefa": tarefa,
                    "Prioridade": prioridade,
                    "Prazo": str(prazo)
                }
            )
            st.success("Tarefa adicionada.")

    if len(st.session_state.tarefas) > 0:
        st.table(st.session_state.tarefas)
    else:
        st.info("Ainda não há tarefas.")
