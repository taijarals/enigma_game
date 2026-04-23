import streamlit as st

st.set_page_config(
    page_title="Sistema",
    page_icon="🧩",
    layout="centered"
)

# ============================
# 🔁 Controle de navegação
# ============================
if "page" not in st.session_state:
    st.session_state.page = "home"

# ============================
# 🏠 HOME
# ============================
if st.session_state.page == "home":
    st.title("🧩 Sistema Principal")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👤 Usuário"):
            st.session_state.page = "usuario"
            st.rerun()

    with col2:
        if st.button("🧠 Enigma"):
            st.session_state.page = "enigma"
            st.rerun()

# ============================
# 👤 USUÁRIO
# ============================
elif st.session_state.page == "usuario":
    st.title("👤 Tela de Usuário")

    if st.button("⬅️ Voltar"):
        st.session_state.page = "home"
        st.rerun()

    # 👉 importa aqui pra evitar conflito
    import pages.usuario as usuario
    usuario.main() if hasattr(usuario, "main") else None

# ============================
# 🧠 ENIGMA
# ============================
elif st.session_state.page == "enigma":
    st.title("🧠 Tela de Enigma")

    if st.button("⬅️ Voltar"):
        st.session_state.page = "home"
        st.rerun()

    import pages.enigma as enigma
    enigma.main() if hasattr(enigma, "main") else None