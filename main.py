import streamlit as st

st.set_page_config(
    page_title="Sistema Principal",
    page_icon="🧩",
    layout="centered"
)

# Título principal
st.title("🧩 Sistema de Navegação")
st.markdown("Escolha uma das opções abaixo para continuar:")

# Espaçamento
st.write("")

# Botões de navegação
col1, col2 = st.columns(2)

with col1:
    if st.button("👤 Usuário", use_container_width=True):
        st.switch_page("usuario.py")

with col2:
    if st.button("🧠 Enigma", use_container_width=True):
        st.switch_page("enigma.py")

# Rodapé opcional
st.write("---")
st.caption("Selecione uma funcionalidade para iniciar.")