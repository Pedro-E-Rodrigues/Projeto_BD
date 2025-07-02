# Seminário da disciplina de PABD

- **Tema**: Gerenciando Relacionamentos Complexos em Ambientes Acadêmicos;

- **Equipe**: [Matheus Quirino](https://github.com/quirinof), [Pedro Emanuel](https://github.com/Pedro-E-Rodrigues), [Isayan Deivid](https://github.com/kolitero)

- **SGBD**: [ArangoDB - Apresentação e Conceitos](https://github.com/Pedro-E-Rodrigues/Projeto_BD/blob/main/docs/arango.md)

- **Tecnologias**: [Python](https://docs.python.org/pt-br/3/), [ArangoDB](https://docs.arangodb.com/3.11/concepts/data-structure/documents/), [Docker](https://docs.docker.com/)

## Tecnologias e execução

- Docker & Docker Compose instalados
- Python 3.9+ e `venv`

### Setup inicial

```bash
# 1. Clone o repositório
git clone https://github.com/Pedro-E-Rodrigues/Projeto_BD.git
cd Projeto_BD

# 2. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Inicie o ArangoDB via Docker
docker-compose up -d

# 5. Execute os scripts do banco de dados
python db_config/connection.py
python db_config/setup_collections.py
python db_config/setup_graph.py

# 6. Insira os dados simulados
python db_config/import_seed.py
python db_config/seed_matriculas.py
python db_config/seed_requisitos.py

# Para testar a aplicação, execute a CLI
python -m app.main

# Para gerar o grafo no Jupyter:

## - Instale as dependências
pip install networkx plotly nx-arangodb python-dotenv

## - Abra o Jupyter Notebook
jupyter notebook notebooks/analise_grafo.ipynb
```
