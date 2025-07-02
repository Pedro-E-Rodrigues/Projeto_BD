from db_config.connection import db
from tabulate import tabulate

graph = db.graph("grafo_academico")
matriculas = graph.edge_collection("matriculas")

def matricular_aluno(aluno_key: str, curso_key: str):
    edge = {
        '_from': f'alunos/{aluno_key}',
        '_to': f'cursos/{curso_key}'
    }
    matriculas.insert(edge)
    print(f"Aluno {aluno_key} matriculado no curso {curso_key}.")

def listar_matriculas_aluno(aluno_key: str):
    query = """
    FOR curso IN OUTBOUND @from_vertex GRAF 'grafo_academico'
      RETURN curso
    """
    cursor = db.aql.execute(query, bind_vars={'from_vertex': f'alunos/{aluno_key}'})
    cursos = [c for c in cursor]
    if cursos:
        print("Cursos do aluno:")
        print(tabulate([[c['_key'], c['nome_curso']] for c in cursos], headers=["KEY", "Nome"]))
    else:
        print("Nenhuma matrícula encontrada.")

def deletar_matricula(aluno_key: str, curso_key: str):
    matching = list(matriculas.find(
        {'_from': f'alunos/{aluno_key}', '_to': f'cursos/{curso_key}'}
    ))
    if not matching:
        print("Matrícula não encontrada.")
        return
    for edge in matching:
        matriculas.delete(edge['_key'])
    print("Matrícula removida com sucesso.")
