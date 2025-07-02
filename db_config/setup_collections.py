import os
from arango import ArangoClient
from dotenv import load_dotenv

load_dotenv()
client = ArangoClient(hosts=os.getenv("ARANGO_HOST"))

sys_db = client.db("_system", username=os.getenv("ARANGO_USER"), password=os.getenv("ARANGO_PASS"))
db_name = os.getenv("DB_NAME", "seminario_db")
if not sys_db.has_database(db_name):
    sys_db.create_database(db_name)
db = client.db(db_name, username=os.getenv("ARANGO_USER"), password=os.getenv("ARANGO_PASS"))

for name in ("alunos", "cursos"):
    if not db.has_collection(name):
        db.create_collection(name)
        print(f"Coleção '{name}' criada.")

if not db.has_graph("grafo_academico"):
    graph = db.create_graph("grafo_academico")
else:
    graph = db.graph("grafo_academico")

for vc in ("alunos", "cursos"):
    if not graph.has_vertex_collection(vc):
        graph.create_vertex_collection(vc)

edge = "matriculas"
if not graph.has_edge_definition(edge):
    graph.create_edge_definition(
        edge_collection=edge,
        from_vertex_collections=["alunos"],
        to_vertex_collections=["cursos"],
    )
    print(f"Aresta '{edge}' criada.")

print("Setup concluído!")