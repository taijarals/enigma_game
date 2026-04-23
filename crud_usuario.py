import pandas as pd
from conexao_api import supabase 

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