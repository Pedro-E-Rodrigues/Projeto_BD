from db_config.connection import db

graph = db.graph("grafo_academico")
reqs = graph.edge_collection("requisitos")

pairs = [
    ("c05", "c01"),
    ("c05", "c02"),
    ("c04", "c01"),
    ("c04", "c03"),
]

for to_key, from_key in pairs:
    edge = {"_from": f"cursos/{to_key}", "_to": f"cursos/{from_key}"}
    try:
        reqs.insert(edge)
        print(f"Requisito inserido: {to_key} → {from_key}")
    except Exception as e:
        print(f"Erro ao inserir requisito: {e}")

print("Seed requisitos executado com sucesso!")
