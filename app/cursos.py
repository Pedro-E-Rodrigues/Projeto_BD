from db_config.connection import db
from tabulate import tabulate

cursos_col = db.collection("cursos")

def listar_cursos(db=None):
    cursos = cursos_col.all()
    rows = [[c["_key"], c.get("nome_curso", "")] for c in cursos]
    print("\n--- Cursos ---")
    if rows:
        print(tabulate(rows, headers=["KEY", "Nome"]))
    else:
        print("Nenhum curso cadastrado.")

def adicionar_curso(db=None):
    nome = input("Nome do curso: ").strip()
    if not nome:
        print("Nome não pode ficar em branco.")
        return
    codigo = input("Código do curso: ").strip()
    doc = {"nome_curso": nome, "codigo": codigo}
    curso = cursos_col.insert(doc)
    print(f"Curso criado com KEY = {curso['_key']}")

def excluir_curso(db=None):
    key = input("KEY do curso a excluir: ").strip()
    if not key:
        print("Cancelado.")
        return
    try:
        cursos_col.delete(key)
        print(f"Curso {key} removido.")
    except Exception:
        print("Falha ao remover (verifique o KEY).")
