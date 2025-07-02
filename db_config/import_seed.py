import json
from db_config.connection import db

data = json.load(open('data/seed_data.json'))
db.collection('alunos').insert_many(data['alunos'])
db.collection('cursos').insert_many(data['cursos'])
print("Dados importados via Python com sucesso!")
