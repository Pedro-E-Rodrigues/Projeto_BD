from db_config.connection import db

graph = db.graph("grafo_academico")
matriculas = graph.edge_collection("matriculas")

inscricoes = [
    ("a01", "c01"),
    ("a01", "c05"),
    ("a02", "c01"),
    ("a02", "c03"),
    ("a03", "c02"),
    ("a04", "c04"),
    ("a05", "c05"),
    ("a05", "c03"),
    ("a06", "c01"),
    ("a07", "c02"),
    ("a08", "c04"),
    ("a09", "c05"),
    ("a10", "c01"),
    ("a11", "c02"),
    ("a12", "c03"),
    ("a13", "c04"),
    ("a14", "c05"),
    ("a15", "c01"),
    ("a16", "c02"),
    ("a17", "c03"),
    ("a18", "c04"),
    ("a19", "c05"),
    ("a20", "c01")
]

for ak, ck in inscricoes:
    edge = {
        "_from": f"alunos/{ak}",
        "_to": f"cursos/{ck}"
    }
    try:
        matr = matriculas.insert(edge)
        print(f"Matrícula criada: {matr['_key']} — {ak} → {ck}")
    except Exception as e:
        print(f"Falha ao matricular {ak} em {ck}: {e}")

print("Seed de matrículas finalizado com sucesso!")
