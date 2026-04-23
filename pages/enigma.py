import streamlit as st
import pandas as pd
import conexao_api
from conexao_api import supabase
from crud_anigma import listar_enigmas



# =============================
# 🎯 Interface Streamlit
# =============================

st.title("🧩 CRUD de Enigmas")

menu = st.sidebar.selectbox(
    "Escolha a ação",
    ["Listar", "Inserir", "Atualizar", "Deletar"]
)

# =============================
# 📄 LISTAR
# =============================
if menu == "Listar":
    st.subheader("📋 Lista de Enigmas")

    df = listar_enigmas()

    if not df.empty:
        st.dataframe(df)
    else:
        st.info("Nenhum enigma cadastrado.")


# =============================
# ➕ INSERIR
# =============================
elif menu == "Inserir":
    st.subheader("➕ Novo Enigma")

    with st.form("form_insert"):
        titulo = st.text_input("Título")
        descricao = st.text_area("Descrição")
        nivel = st.number_input("Nível", min_value=1)
        resposta = st.text_input("Resposta")

        dica1 = st.text_input("Dica 1")
        dica2 = st.text_input("Dica 2")
        dica3 = st.text_input("Dica 3")

        fk_usuario = st.text_input("ID Usuário (UUID - opcional)")

        submitted = st.form_submit_button("Salvar")

        if submitted:
            data = {
                "titulo_enigma": titulo,
                "descricao_enigma": descricao,
                "nivel_enigma": nivel,
                "resposta_enigma": resposta,
                "dica_1_enigma": dica1 or None,
                "dica_2_enigma": dica2 or None,
                "dica_3_enigma": dica3 or None,
                "fk_usuario": fk_usuario or None
            }

            inserir_enigma(data)
            st.success("Enigma inserido com sucesso!")


# =============================
# ✏️ ATUALIZAR
# =============================
elif menu == "Atualizar":
    st.subheader("✏️ Atualizar Enigma")

    df = listar_enigmas()

    if df.empty:
        st.warning("Nenhum enigma para atualizar.")
    else:
        selected_id = st.selectbox(
            "Selecione o enigma",
            df["id_enigma"]
        )

        enigma = df[df["id_enigma"] == selected_id].iloc[0]

        with st.form("form_update"):
            titulo = st.text_input("Título", enigma["titulo_enigma"])
            descricao = st.text_area("Descrição", enigma["descricao_enigma"])
            nivel = st.number_input("Nível", value=int(enigma["nivel_enigma"]))
            resposta = st.text_input("Resposta", enigma["resposta_enigma"])

            dica1 = st.text_input("Dica 1", enigma["dica_1_enigma"])
            dica2 = st.text_input("Dica 2", enigma["dica_2_enigma"])
            dica3 = st.text_input("Dica 3", enigma["dica_3_enigma"])

            fk_usuario = st.text_input("ID Usuário", enigma["fk_usuario"])

            submitted = st.form_submit_button("Atualizar")

            if submitted:
                data = {
                    "titulo_enigma": titulo,
                    "descricao_enigma": descricao,
                    "nivel_enigma": nivel,
                    "resposta_enigma": resposta,
                    "dica_1_enigma": dica1,
                    "dica_2_enigma": dica2,
                    "dica_3_enigma": dica3,
                    "fk_usuario": fk_usuario or None
                }

                atualizar_enigma(selected_id, data)
                st.success("Enigma atualizado!")


# =============================
# ❌ DELETAR
# =============================
elif menu == "Deletar":
    st.subheader("❌ Deletar Enigma")

    df = listar_enigmas()

    if df.empty:
        st.warning("Nenhum enigma para deletar.")
    else:
        selected_id = st.selectbox(
            "Selecione o enigma",
            df["id_enigma"]
        )

        if st.button("Deletar"):
            deletar_enigma(selected_id)
            st.success("Enigma deletado com sucesso!")