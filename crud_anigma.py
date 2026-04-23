import conexao_api
from conexao_api import supabase

# =============================
# 📌 Funções CRUD
# =============================


def listar_enigmas():
    response = supabase.table("enigma").select("*").execute()
    return pd.DataFrame(response.data)


def inserir_enigma(data):
    supabase.table("enigma").insert(data).execute()


def atualizar_enigma(id_enigma, data):
    supabase.table("enigma").update(data).eq("id_enigma", id_enigma).execute()


def deletar_enigma(id_enigma):
    supabase.table("enigma").delete().eq("id_enigma", id_enigma).execute()
