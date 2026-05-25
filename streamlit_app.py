import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Blink Clinic | Oculoplástica",
    page_icon="👁️",
    layout="wide"
)

# -----------------------------
# Dados temporários
# -----------------------------
if "pacientes" not in st.session_state:
    st.session_state.pacientes = []

if "consultas" not in st.session_state:
    st.session_state.consultas = []

if "tarefas" not in st.session_state:
    st.session_state.tarefas = []


# -----------------------------
# Estilo visual premium
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(198, 231, 242, 0.55), transparent 35%),
            radial-gradient(circle at top right, rgba(222, 238, 243, 0.8), transparent 30%),
            linear-gradient(135deg, #f8fbfd 0%, #eef6f9 45%, #ffffff 100%);
        color: #18313f;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #092331 0%, #12384a 45%, #1f6078 100%);
        border-right: 1px solid rgba(255,255,255,0.15);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        font-family: "Segoe UI", sans-serif;
        letter-spacing: -0.03em;
    }

    .hero {
        background:
            linear-gradient(135deg, rgba(7, 34, 47, 0.96), rgba(44, 118, 145, 0.92)),
            url("https://images.unsplash.com/photo-1559757175-0eb30cd8c063?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-position: center;
        padding: 58px;
        border-radius: 34px;
        color: white;
        box-shadow: 0 25px 60px rgba(13, 55, 75, 0.25);
        margin-bottom: 32px;
        position: relative;
        overflow: hidden;
    }

    .hero h1 {
        font-size: 58px;
        margin-bottom: 8px;
        font-weight: 850;
    }

    .hero p {
        font-size: 20px;
        max-width: 760px;
        opacity: 0.96;
        line-height: 1.6;
    }

    .tag {
        display: inline-block;
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.28);
        backdrop-filter: blur(8px);
        padding: 9px 16px;
        border-radius: 999px;
        font-size: 14px;
        font-weight: 700;
        margin: 6px 6px 0 0;
    }

    .glass-card {
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(215,235,242,0.95);
        border-radius: 28px;
        padding: 26px;
        box-shadow: 0 18px 45px rgba(20, 76, 96, 0.10);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    .service-card {
        background: white;
        border-radius: 28px;
        padding: 28px;
        min-height: 240px;
        box-shadow: 0 16px 38px rgba(18, 76, 98, 0.10);
        border: 1px solid #dceef3;
        transition: all 0.25s ease;
        margin-bottom: 18px;
    }

    .service-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 22px 48px rgba(18, 76, 98, 0.16);
    }

    .service-icon {
        font-size: 36px;
        margin-bottom: 12px;
    }

    .service-card h3 {
        color: #12384a;
        margin-bottom: 8px;
    }

    .service-card p {
        color: #516b76;
        font-size: 15px;
        line-height: 1.55;
    }

    .metric-card {
        background: linear-gradient(180deg, #ffffff 0%, #f4fbfd 100%);
        border: 1px solid #d7ecf2;
        border-radius: 26px;
        padding: 28px;
        text-align: center;
        box-shadow: 0 14px 35px rgba(18, 76, 98, 0.10);
    }

    .metric-number {
        font-size: 42px;
        font-weight: 900;
        color: #1f6078;
        margin-bottom: 4px;
    }

    .metric-label {
        font-size: 15px;
        color: #5d737c;
        font-weight: 600;
    }

    .section-title {
        font-size: 30px;
        font-weight: 850;
        color: #12384a;
        margin-top: 18px;
        margin-bottom: 14px;
    }

    .timeline {
        border-left: 4px solid #6bb6ca;
        padding-left: 22px;
        margin-left: 8px;
    }

    .timeline-item {
        background: white;
        border-radius: 20px;
        padding: 18px 22px;
        margin-bottom: 16px;
        box-shadow: 0 12px 28px rgba(18, 76, 98, 0.08);
        border: 1px solid #e0f0f4;
    }

    .notice {
        background: linear-gradient(135deg, #e9f7fb, #ffffff);
        border: 1px solid #cbe8ef;
        padding: 22px;
        border-radius: 24px;
        color: #244756;
        box-shadow: 0 12px 30px rgba(18, 76, 98, 0.08);
    }

    div.stButton > button:first-child {
        background: linear-gradient(135deg, #164b63 0%, #4da4bd 100%);
        color: white;
        border: none;
        border-radius: 999px;
        padding: 0.75rem 1.5rem;
        font-weight: 800;
        box-shadow: 0 10px 22px rgba(31, 96, 120, 0.28);
    }

    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        color: white;
        border: none;
    }

    .footer {
        margin-top: 40px;
        text-align: center;
        color: #6e838b;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Funções visuais
# -----------------------------
def service_card(icon, title, text):
    st.markdown(
        f"""
        <div class="service-card">
            <div class="service-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_card(number, label):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-number">{number}</div>
            <div class="metric-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Menu lateral
# -----------------------------
st.sidebar.markdown("## 👁️ Blink Clinic")
st.sidebar.markdown("### Oculoplástica")
st.sidebar.caption("Pálpebras · Vias lacrimais · Órbita · Estética periocular")
st.sidebar.divider()

pagina = st.sidebar.radio(
    "Menu principal",
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
st.sidebar.caption("Aplicação de gestão e apresentação clínica.")


# -----------------------------
# Página inicial
# -----------------------------
if pagina == "Início":
    st.markdown(
        """
        <div class="hero">
            <h1>👁️ Blink Clinic</h1>
            <p>
            Clínica especializada em oculoplástica, dedicada à saúde, função e estética
            da região periocular, com uma abordagem médica cuidada, moderna e personalizada.
            </p>
            <span class="tag">Oculoplástica</span>
            <span class="tag">Pálpebras</span>
            <span class="tag">Vias lacrimais</span>
            <span class="tag">Órbita</span>
            <span class="tag">Estética periocular</span>
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

    st.markdown('<div class="section-title">Áreas de atuação</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        service_card(
            "👁️",
            "Cirurgia Palpebral",
            "Avaliação e tratamento de alterações das pálpebras, incluindo blefaroplastia, ptose palpebral, entrópio e ectrópio."
        )

    with c2:
        service_card(
            "💧",
            "Vias Lacrimais",
            "Estudo e tratamento de lacrimejo persistente, obstruções lacrimais e alterações do sistema lacrimal."
        )

    with c3:
        service_card(
            "🩺",
            "Órbita e Região Periocular",
            "Avaliação médica de alterações orbitárias, lesões palpebrais e estética periocular."
        )

    st.markdown(
        """
        <div class="glass-card">
            <h3>Experiência pensada para o paciente</h3>
            <p>
            Esta aplicação pode ser usada para apresentar serviços, organizar consultas,
            criar conteúdos de comunicação e estruturar a informação da clínica.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="notice">
            <strong>Nota importante:</strong> não coloques dados clínicos reais se a aplicação estiver pública.
            Esta versão é ideal para apresentação, teste e organização inicial.
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Serviços
# -----------------------------
elif pagina == "Serviços":
    st.title("🏥 Serviços de Oculoplástica")
    st.write("Apresentação visual dos serviços principais da Blink Clinic.")

    col1, col2, col3 = st.columns(3)

    with col1:
        service_card(
            "✨",
            "Blefaroplastia",
            "Cirurgia das pálpebras superiores e/ou inferiores, com finalidade funcional, estética ou combinada, após avaliação médica."
        )

    with col2:
        service_card(
            "👁️",
            "Ptose Palpebral",
            "Avaliação e tratamento da queda da pálpebra superior, que pode interferir com a visão ou com a simetria do olhar."
        )

    with col3:
        service_card(
            "🔄",
            "Entrópio e Ectrópio",
            "Correção de alterações da posição das pálpebras, que podem causar desconforto, irritação ocular ou lacrimejo."
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        service_card(
            "💧",
            "Vias Lacrimais",
            "Avaliação de lacrimejo persistente, obstrução lacrimal e alterações associadas ao sistema de drenagem lacrimal."
        )

    with col5:
        service_card(
            "🔬",
            "Lesões Palpebrais",
            "Observação, diagnóstico, acompanhamento e eventual remoção de lesões localizadas nas pálpebras."
        )

    with col6:
        service_card(
            "🩺",
            "Consulta de Oculoplástica",
            "Primeira avaliação médica, diagnóstico, esclarecimento de dúvidas e orientação terapêutica personalizada."
        )

    st.markdown(
        """
        <div class="notice">
            Os serviços devem ser sempre apresentados como avaliação médica individualizada.
            Evita prometer resultados iguais para todos os pacientes.
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Pacientes
# -----------------------------
elif pagina == "Pacientes":
    st.title("👤 Pacientes")
    st.write("Registo administrativo simples de pacientes.")

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

    st.divider()
    st.subheader("Pacientes registados")

    if len(st.session_state.pacientes) == 0:
        st.info("Ainda não há pacientes registados.")
    else:
        st.table(st.session_state.pacientes)


# -----------------------------
# Consultas
# -----------------------------
elif pagina == "Consultas":
    st.title("📅 Consultas")
    st.write("Organização simples de consultas e procedimentos.")

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

    st.divider()
    st.subheader("Consultas guardadas")

    if len(st.session_state.consultas) == 0:
        st.info("Ainda não há consultas guardadas.")
    else:
        st.table(st.session_state.consultas)


# -----------------------------
# Informação Clínica
# -----------------------------
elif pagina == "Informação Clínica":
    st.title("ℹ️ Informação Clínica")
    st.write("Área informativa para explicar a especialidade de forma simples e elegante.")

    st.markdown(
        """
        <div class="timeline">
            <div class="timeline-item">
                <h3>1. O que é a oculoplástica?</h3>
                <p>
                É uma área da oftalmologia dedicada às pálpebras, vias lacrimais,
                órbita e região periocular.
                </p>
            </div>

            <div class="timeline-item">
                <h3>2. Quando procurar avaliação?</h3>
                <p>
                Quando existem alterações das pálpebras, lacrimejo persistente,
                lesões palpebrais, assimetrias, desconforto ocular ou alterações estéticas do olhar.
                </p>
            </div>

            <div class="timeline-item">
                <h3>3. Como é a abordagem?</h3>
                <p>
                Cada caso deve ser avaliado individualmente, considerando a saúde ocular,
                a função das pálpebras e os objetivos do paciente.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="notice">
            Esta informação é geral e não substitui uma consulta médica individualizada.
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Marketing
# -----------------------------
elif pagina == "Marketing":
    st.title("📣 Marketing")
    st.write("Criação de ideias de comunicação para a Blink Clinic.")

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
        "Apresentação da clínica": "A Blink Clinic nasce para cuidar da saúde, função e estética do olhar, com uma abordagem médica personalizada.",
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
            <div class="glass-card">
                <h3>Texto sugerido</h3>
                <p>{ideias[tema]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("Criar legenda personalizada")

    objetivo = st.text_input("Objetivo da publicação", placeholder="Ex: explicar um serviço")
    tom = st.selectbox("Tom da comunicação", ["Profissional", "Informativo", "Elegante", "Acolhedor"])

    if st.button("Criar legenda"):
        if objetivo.strip() == "":
            st.warning("Escreve o objetivo da publicação.")
        else:
            st.success(
                f"Legenda em tom {tom.lower()}: Na Blink Clinic, cada olhar é avaliado com atenção médica, "
                f"cuidado e detalhe. Hoje falamos sobre {objetivo.lower()}, sempre com foco na segurança, "
                f"na função e na harmonia da região periocular."
            )


# -----------------------------
# Tarefas
# -----------------------------
elif pagina == "Tarefas":
    st.title("✅ Tarefas internas")
    st.write("Organização de tarefas da clínica.")

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

    st.divider()

    if len(st.session_state.tarefas) == 0:
        st.info("Ainda não há tarefas.")
    else:
        st.table(st.session_state.tarefas)


st.markdown(
    """
    <div class="footer">
        Blink Clinic · Oculoplástica · Pálpebras · Vias lacrimais · Órbita · Estética periocular
    </div>
    """,
    unsafe_allow_html=True
)
