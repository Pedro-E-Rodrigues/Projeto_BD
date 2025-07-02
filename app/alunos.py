from db_config.connection import db
from tabulate import tabulate

alunos_col = db.collection("alunos")

def listar_alunos():
    alunos = alunos_col.all()
    rows = [[a["_key"], a.get("nome", "")] for a in alunos]
    print("\n--- Alunos ---")
    if rows:
        print(tabulate(rows, headers=["KEY", "Nome"]))
    else:
        print("Nenhum aluno cadastrado.")

def adicionar_aluno():
    nome = input("Nome do aluno: ").strip()
    if not nome:
        print("Nome não pode ficar em branco.")
        return
    matricula = input("Matrícula: ").strip()
    doc = {"nome": nome, "matricula": matricula}
    aluno = alunos_col.insert(doc)
    print(f"Aluno criado com KEY = {aluno['_key']}")

def excluir_aluno():
    key = input("KEY do aluno a excluir: ").strip()
    if not key:
        print("Cancelado.")
        return
    try:
        alunos_col.delete(key)
        print(f"Aluno {key} removido.")
    except Exception:
        print("Falha ao remover (verifique o KEY).")
