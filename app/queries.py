from db_config.connection import db
from tabulate import tabulate

def contar_alunos_por_curso():
    query = """
    FOR c IN cursos
      LET total = LENGTH(
        FOR v IN INBOUND c._id matriculas
          RETURN 1
      )
      RETURN { curso: c.nome_curso, alunos: total }
    """
    cursor = db.aql.execute(query)
    resultados = list(cursor)
    print(tabulate([(r['curso'], r['alunos']) for r in resultados], headers=["Curso", "Qtd. Alunos"]))

def mostrar_cadeia_prerequisitos(curso_key: str, niveis: int = 3):
    start_id = f"cursos/{curso_key}"
    query = f"""
    FOR v, e, p IN 1..{niveis} INBOUND '{start_id}' requisitos
      OPTIONS {{ bfs: true, uniqueVertices: 'global' }}
      RETURN p.vertices[*]._key
    """
    cursor = db.aql.execute(query)
    caminhos = list(cursor)
    if caminhos:
        print("Pré‑requisitos encontrados (por nível):")
        for caminho in caminhos:
            print(" → ".join(caminho))
    else:
        print("Nenhum pré‑requisito encontrado.")


def listar_alunos_sem_matricula():
    query = """
    FOR a IN alunos
      FILTER NOT LENGTH(
        FOR c IN OUTBOUND a._id matriculas
          RETURN 1
      )
      RETURN a
    """
    cursor = db.aql.execute(query)
    alunos = list(cursor)
    if alunos:
        print("Alunos sem matrícula:")
        print(tabulate([[a['_key'], a['nome']] for a in alunos], headers=["KEY", "Nome"]))
    else:
        print("Todos os alunos estão matriculados em algum curso.")
