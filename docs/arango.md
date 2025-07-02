# ArangoDB - Conceitos iniciais, funcionalidades e comandos básicos

ArangoDB é um banco de dados NoSQL multi-modal, o que significa que pode armazenar e gerenciar dados usando diferentes modelos.

## Características Principais

- **Modelo de Dados Multi-Modelo**: Suporte para documentos, grafos e dados chave-valor em uma única plataforma.
- **Escalabilidade**: Capacidade de escalar horizontalmente para lidar com grandes volumes de dados e altas taxas de transferência. Suporta clusters, sharding e replicação.
- **Consultas AQL**: Linguagem de consulta poderosa e expressiva para interagir com os dados.
- **Transações**: Suporte para transações ACID, garantindo a integridade dos dados.

## Casos de Uso

ArangoDB é ideal para uma variedade de casos de uso, incluindo:

- Aplicações de redes sociais
- Sistemas de recomendação
- Gerenciamento de conteúdo
- Análise de dados em tempo real

## Funcionalidades básicas

- **Coleções**: Estruturas que armazenam documentos. Podem ser do tipo `document`, `edge` (para grafos) ou `key/value`.
- **Documentos**: Unidades de dados armazenadas em coleções, semelhantes a registros em bancos de dados relacionais.
- **AQL (ArangoDB Query Language)**: Linguagem de consulta que permite realizar operações complexas em dados armazenados.
- **Índices**: Estruturas que melhoram a eficiência das consultas, permitindo acesso rápido
  aos dados.
- **Transações**: Permitem realizar múltiplas operações de leitura e escrita de forma atômica, garantindo a consistência dos dados.

## Comandos básicos em Python

```python
from arango import ArangoClient

client = ArangoClient()
db = client.db("nome_do_banco_de_dados")

# Criar Coleção
db.create_collection("nome_da_colecao")

# Inserir Documento
db.collection("nome_da_colecao").insert({"chave": "valor"})

# Consultar Documento
db.collection("nome_da_colecao").get({"chave": "valor"})
```
