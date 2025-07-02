# Seminário da disciplina de PABD

- **Tema**: Gerenciando Relacionamentos Complexos em Ambientes Acadêmicos;

- **Equipe**: [Matheus Quirino](https://github.com/quirinof), [Pedro Emanuel](https://github.com/Pedro-E-Rodrigues), [Isayan Deivid](https://github.com/kolitero)

- **SGBD**: [ArangoDB - Apresentação e Conceitos](https://github.com/Pedro-E-Rodrigues/Projeto_BD/blob/main/docs/arango.md)

- **Tecnologias**: [Python](https://docs.python.org/pt-br/3/), [ArangoDB](https://docs.arangodb.com/3.11/concepts/data-structure/documents/), [Docker](https://docs.docker.com/)

## Projeto - Pré-requisitos

- Docker & Docker Compose instalados
- Python 3.9+ e `venv`

- Passos para executar o projeto:

```bash
# Clonar o repositório
git clone https://github.com/Pedro-E-Rodrigues/Projeto_BD.git
cd Projeto_BD

# Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Instalar as dependências
pip install -r requirements.txt

# Iniciar o Docker com o ArangoDB
docker-compose up -d
```
