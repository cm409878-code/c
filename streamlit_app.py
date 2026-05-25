import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Blink Clinic",
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
        background: linear-gradient(135deg, #f7fbff 0%, #edf4f8 45%, #ffffff 100%);
        color: #1f2d35;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f2533 0%, #23495f 100%);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .block-container {
        padding-top: 2rem;
    }

    .hero {
        background: linear-gradient(135deg, #123243 0%, #3f7d96 60%, #d7edf3 100%);
        padding: 45px;
        border-radius: 28px;
        color: white;
        box-shadow: 0 18px 45px rgba(20, 60, 80, 0.22);
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 52px;
        margin-bottom: 5px;
    }

    .hero p {
        font-size: 19px;
        opacity: 0.95;
    }

    .card {
        background: rgba(255,255,255,0.92);
        padding: 25px;
        border-radius: 24px;
        box-shadow: 0 12px 35px rgba(20, 60, 80, 0.10);
        border: 1px solid rgba(220, 235, 240, 0.8);
        margin-bottom: 18px;
    }

    .service-card {
        background: white;
        padding: 24px;
        border-radius: 22px;
        box-shadow: 0 10px 28px rgba(20, 60, 80, 0.10);
        border-left: 6px solid #3f7d96;
        min-height: 190px;
    }

    .metric-card {
        background: white;
        padding: 25px;
        border-radius: 22px;
        box-shadow: 0 12px 30px rgba(20, 60, 80, 0.09);
        text-align: center;
    }

    .metric-number {
        font-size: 38px;
        font-weight: 800;
        color: #255c72;
    }

    .metric-label {
        font-size: 15px;
        color: #5c6f77;
    }

    .pill {
        display: inline-block;
        background: #d7edf3;
        color: #123243;
        padding: 8px 15px;
        border-radius: 999px;
        font-size: 14px;
        font-weight: 600;
        margin: 4px;
    }

    div.stButton > button:first-child {
        background: linear-gradient(135deg, #255c72 0%, #69a8bd 100%);
        color: white;
        border: none;
        border-radius: 999px;
        padding: 0.75rem 1.4rem;
        font-weight: 700;
        box-shadow: 0 8px 18px rgba(37, 92, 114, 0.25);
    }

    .footer {
        text-align: center;
        color: #6b7d84;
        padding-top: 30px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown("## 👁️ Blink Clinic")
st.sidebar.markdown("Clínica de Oculoplástica")
st.sidebar.divider()

pagina = st.sidebar.radio(
    "Menu principal",
    [
        "Início",
        "Pacientes",
        "Serviços",
        "Consultas",
        "Informação Clínica",
        "Marketing",
        "Tarefas"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Gestão simples para clínica de oculoplástica.")


if pagina == "Início":
    st.markdown(
        """
        <div class="hero">
            <h1>👁️ Blink Clinic</h1>
            <p>Clínica dedicada à oculoplástica, pálpebras, vias lacrimais, órbita e estética periocular.</p>
            <span class="pill">Oculoplástica</span>
            <span class="pill">Pálpebras</span>
            <span class="pill">Vias lacrimais</span>
            <span class="pill">Órbita</span>
            <span class="pill">Estética periocular</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{len(st.session_state.pacientes)}</div>
                <div class="metric-label">Pacientes registados</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{len(st.session_state.consultas)}</div>
                <div class="metric-label">Consultas marcadas</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{len(st.session_state.tarefas)}</div>
                <div class="metric-label">Tarefas internas</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("## Áreas principais")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="service-card">
                <h3>Cirurgia Palpebral</h3>
                <p>Blefaroplastia, ptose palpebral, entrópio, ectrópio e outras alterações das pálpebras.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="service-card">
                <h3>Vias Lacrimais</h3>
                <p>Avaliação e tratamento de lacrimejo, obstruções e alterações do sistema lacrimal.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="service-card">
                <h3>Órbita e Periocular</h3>
                <p>Avaliação da região orbitária, lesões palpebrais e estética médica periocular.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info("Nota: esta app é uma estrutura inicial. Não coloques dados clínicos reais se a aplicação estiver pública.")


elif pagina == "Pacientes":
    st.title("👤 Pacientes")
    st.write("Área simples para registo administrativo de pacientes.")

    with st.form("form_paciente"):
        nome = st.text_input("Nome do paciente")
        contacto = st.text_input("Contacto")
        email = st.text_input("Email")
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


elif pagina == "Serviços":
    st.title("🏥 Serviços de Oculoplástica")
    st.write("Apresentação dos serviços principais da Blink Clinic.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>Blefaroplastia</h3>
                <p>Cirurgia das pálpebras superiores e/ou inferiores, com foco funcional e/ou estético.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Ptose Palpebral</h3>
                <p>Avaliação e tratamento da queda da pálpebra superior.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Entrópio e Ectrópio</h3>
                <p>Correção de alterações da posição das pálpebras.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Lesões Palpebrais</h3>
                <p>Avaliação, acompanhamento e eventual remoção de lesões nas pálpebras.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>Vias Lacrimais</h3>
                <p>Avaliação de lacrimejo, obstrução lacrimal e alterações associadas.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Cirurgia da Órbita</h3>
                <p>Avaliação de alterações orbitárias e perioculares.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Estética Periocular</h3>
                <p>Abordagem estética da região do olhar, de acordo com avaliação médica.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h3>Consulta de Oculoplástica</h3>
                <p>Primeira avaliação, diagnóstico e orientação terapêutica personalizada.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


elif pagina == "Consultas":
    st.title("📅 Consultas")
    st.write("Organização simples de consultas e procedimentos.")

    with st.form("form_consulta"):
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


elif pagina == "Informação Clínica":
    st.title("ℹ️ Informação Clínica")
    st.write("Área informativa para explicar a especialidade de forma simples.")

    with st.expander("O que é Oculoplástica?"):
        st.write(
            "A oculoplástica é uma área da oftalmologia dedicada às pálpebras, "
            "vias lacrimais, órbita e região periocular."
        )

    with st.expander("Quando procurar avaliação?"):
        st.write(
            "Pode ser necessária avaliação quando existem alterações nas pálpebras, "
            "lacrimejo persistente, lesões palpebrais, desconforto ocular associado "
            "à posição das pálpebras ou alterações estéticas/funcionais do olhar."
        )

    with st.expander("Nota importante"):
        st.write(
            "Esta informação é geral e não substitui uma consulta médica individualizada."
        )


elif pagina == "Marketing":
    st.title("📣 Marketing")
    st.write("Ideias de comunicação para uma clínica de oculoplástica.")

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
        "Apresentação da clínica": "A Blink Clinic nasce para cuidar da saúde e estética do olhar, com uma abordagem médica, personalizada e segura.",
        "O que é oculoplástica": "A oculoplástica dedica-se ao tratamento das pálpebras, vias lacrimais, órbita e região periocular.",
        "Blefaroplastia": "A blefaroplastia pode ter objetivos funcionais e/ou estéticos, dependendo da avaliação médica individual.",
        "Ptose palpebral": "A ptose palpebral é a queda da pálpebra superior e pode interferir com o campo visual ou a simetria do olhar.",
        "Vias lacrimais": "O lacrimejo persistente pode estar associado a alterações das vias lacrimais e deve ser avaliado em consulta.",
        "Lesões palpebrais": "Lesões nas pálpebras devem ser observadas para diagnóstico e orientação adequada.",
        "Cuidados no pós-operatório": "O acompanhamento médico e o cumprimento das indicações pós-operatórias são fundamentais para uma boa recuperação."
    }

    if st.button("Gerar texto"):
        st.markdown(
            f"""
            <div class="card">
                <h3>Texto sugerido</h3>
                <p>{ideias[tema]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


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
        Blink Clinic · Oculoplástica · Pálpebras · Vias lacrimais · Órbita
    </div>
    """,
    unsafe_allow_html=True
)
