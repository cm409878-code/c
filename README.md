import streamlit as st

st.set_page_config(
    page_title="Blink Clinic",
    page_icon="👁️",
    layout="wide"
)

st.title("👁️ Blink Clinic")

st.write("Bem-vinda à aplicação da Blink Clinic.")

st.header("Menu principal")

opcao = st.selectbox(
    "Escolhe uma opção:",
    ["Início", "Clientes", "Serviços", "Marketing", "Tarefas"]
)

if opcao == "Início":
    st.subheader("Início")
    st.write("Esta é a página inicial da aplicação.")

elif opcao == "Clientes":
    st.subheader("Clientes")
    nome = st.text_input("Nome do cliente")
    telefone = st.text_input("Telefone")
    
    if st.button("Guardar cliente"):
        st.success(f"Cliente {nome} guardado com sucesso!")

elif opcao == "Serviços":
    st.subheader("Serviços")
    st.write("- Extensão de pestanas")
    st.write("- Lifting de pestanas")
    st.write("- Design de sobrancelhas")

elif opcao == "Marketing":
    st.subheader("Marketing")
    st.write("Aqui podes escrever ideias para publicações, campanhas e promoções.")
    
    ideia = st.text_area("Escreve uma ideia de marketing")
    
    if st.button("Guardar ideia"):
        st.success("Ideia guardada!")

elif opcao == "Tarefas":
    st.subheader("Tarefas")
    tarefa = st.text_input("Nova tarefa")
    
    if st.button("Adicionar tarefa"):
        st.success(f"Tarefa adicionada: {tarefa}")
