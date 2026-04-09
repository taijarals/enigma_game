import streamlit as st
import pandas as pd
from supabase import create_client, Client

# =========================
# CONFIG SUPABASE
# =========================

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# =========================
# FUNÇÕES CRUD
# =========================

def get_usuarios():
    response = supabase.table("usuario").select("*").order("created_at", desc=True).execute()
    return pd.DataFrame(response.data)


def inserir_usuario(dados):
    supabase.table("usuario").insert(dados).execute()


def atualizar_usuario(id_usuario, dados):
    supabase.table("usuario").update(dados).eq("id_usuario", id_usuario).execute()


def deletar_usuario(id_usuario):
    supabase.table("usuario").delete().eq("id_usuario", id_usuario).execute()


# =========================
# UI STREAMLIT
# =========================

st.title("👤 CRUD de Usuários (Supabase API)")

menu = st.sidebar.selectbox("Menu", ["Listar", "Cadastrar", "Editar", "Deletar"])

# =========================
# LISTAR
# =========================
if menu == "Listar":
    df = get_usuarios()
    st.dataframe(df)

# =========================
# CADASTRAR
# =========================
elif menu == "Cadastrar":
    st.subheader("Novo Usuário")

    with st.form("form_cadastro"):
        tipo = st.text_input("Tipo Usuário")
        senha = st.text_input("Senha", type="password")
        email = st.text_input("Email")
        nivel = st.number_input("Nível", value=1)
        nick = st.text_input("Nick")
        pontuacao = st.number_input("Pontuação", value=0)
        rank = st.number_input("Rank", value=0)

        submit = st.form_submit_button("Salvar")

        if submit:
            inserir_usuario({
                "tipo_usuario": tipo,
                "senha_usuario": senha,
                "email_usuario": email,
                "nivel_usuario": nivel,
                "nick_usuario": nick,
                "pontuacao_usuario": pontuacao,
                "rank_usuario": rank
            })
            st.success("Usuário cadastrado!")

# =========================
# EDITAR
# =========================
elif menu == "Editar":
    df = get_usuarios()

    if not df.empty:
        usuario_id = st.selectbox("Selecione o usuário", df["id_usuario"])

        usuario = df[df["id_usuario"] == usuario_id].iloc[0]

        with st.form("form_editar"):
            tipo = st.text_input("Tipo Usuário", usuario["tipo_usuario"])
            senha = st.text_input("Senha", usuario["senha_usuario"])
            email = st.text_input("Email", usuario["email_usuario"])
            nivel = st.number_input("Nível", value=int(usuario["nivel_usuario"]))
            nick = st.text_input("Nick", usuario["nick_usuario"])
            pontuacao = st.number_input("Pontuação", value=int(usuario["pontuacao_usuario"]))
            rank = st.number_input("Rank", value=int(usuario["rank_usuario"]))

            submit = st.form_submit_button("Atualizar")

            if submit:
                atualizar_usuario(usuario_id, {
                    "tipo_usuario": tipo,
                    "senha_usuario": senha,
                    "email_usuario": email,
                    "nivel_usuario": nivel,
                    "nick_usuario": nick,
                    "pontuacao_usuario": pontuacao,
                    "rank_usuario": rank
                })
                st.success("Atualizado com sucesso!")

# =========================
# DELETAR
# =========================
elif menu == "Deletar":
    df = get_usuarios()

    if not df.empty:
        usuario_id = st.selectbox("Selecione o usuário para deletar", df["id_usuario"])

        if st.button("Deletar"):
            deletar_usuario(usuario_id)
            st.success("Usuário deletado!")