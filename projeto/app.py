import os
import time
from arango import ArangoClient
from arango.exceptions import CollectionCreateError, DocumentDeleteError

# --- Configurações da Conexão com o ArangoDB no Docker ---
ARANGO_HOST = "http://localhost:8529"
ARANGO_USER = "root"
ARANGO_PASS = "admin" # A senha que definimos no comando Docker
DB_NAME = "_system" # Banco de dados padrão

def limpar_tela():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def conectar_banco():
    """Conecta ao ArangoDB e retorna a instância do banco."""
    try:
        client = ArangoClient(hosts=ARANGO_HOST)
        db = client.db(DB_NAME, username=ARANGO_USER, password=ARANGO_PASS)
        return db
    except Exception as e:
        print(f"Erro ao conectar ao ArangoDB: {e}")
        print("Verifique se o contêiner Docker 'seminario-arango' está rodando.")
        return None

def preparar_colecoes(db):
    """Cria as coleções 'alunos' e 'cursos' se não existirem."""
    try:
        db.create_collection('alunos')
        print("Coleção 'alunos' criada.")
    except CollectionCreateError:
        pass
    
    try:
        db.create_collection('cursos')
        print("Coleção 'cursos' criada.")
    except CollectionCreateError:
        pass


def adicionar_aluno(db):
    """Adiciona um novo aluno."""
    nome = input("Digite o nome do aluno: ")
    matricula = input(f"Digite a matrícula de {nome}: ")
    db.collection('alunos').insert({'nome': nome, 'matricula': matricula})
    print(f"\nAluno '{nome}' adicionado com sucesso!")

def adicionar_curso(db):
    """Adiciona um novo curso."""
    nome_curso = input("Digite o nome do curso: ")
    codigo_curso = input(f"Digite o código do curso '{nome_curso}': ")
    db.collection('cursos').insert({'nome_curso': nome_curso, 'codigo': codigo_curso})
    print(f"\nCurso '{nome_curso}' adicionado com sucesso!")

# --- NOVA FUNÇÃO ---
def excluir_aluno(db):
    """Exclui um aluno existente pelo seu KEY."""
    key_aluno = input("Digite o KEY do aluno que deseja excluir (ou deixe em branco para cancelar): ")
    if not key_aluno:
        return

    try:
        db.collection('alunos').delete(key_aluno)
        print(f"\nAluno com KEY '{key_aluno}' excluído com sucesso!")
    except DocumentDeleteError:
        print(f"\nErro: Nenhum aluno encontrado com o KEY '{key_aluno}'.")

# --- NOVA FUNÇÃO ---
def excluir_curso(db):
    """Exclui um curso existente pelo seu KEY."""
    key_curso = input("Digite o KEY do curso que deseja excluir (ou deixe em branco para cancelar): ")
    if not key_curso:
        return
        
    try:
        db.collection('cursos').delete(key_curso)
        print(f"\nCurso com KEY '{key_curso}' excluído com sucesso!")
    except DocumentDeleteError:
        print(f"\nErro: Nenhum curso encontrado com o KEY '{key_curso}'.")


def visualizar_tudo(db):
    """Exibe todos os alunos e cursos, incluindo seus IDs (KEYs)."""
    limpar_tela()
    print("--- Alunos Matriculados ---")
    alunos = db.collection('alunos').all()
    for aluno in alunos:
        # --- MODIFICADO para mostrar o _key ---
        print(f"  [KEY: {aluno['_key']}] Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}")
    if not db.collection('alunos').count():
        print("  Nenhum aluno cadastrado.")

    print("\n--- Cursos Disponíveis ---")
    cursos = db.collection('cursos').all()
    for curso in cursos:
        # --- MODIFICADO para mostrar o _key ---
        print(f"  [KEY: {curso['_key']}] Curso: {curso['nome_curso']}, Código: {curso['codigo']}")
    if not db.collection('cursos').count():
        print("  Nenhum curso cadastrado.")
    print("-" * 30)


def main():
    """Função principal."""
    db = conectar_banco()
    if not db:
        return

    preparar_colecoes(db)

    while True:
        visualizar_tudo(db)
        # --- MENU ATUALIZADO ---
        print("\nOpções:")
        print("1. Adicionar Aluno")
        print("2. Adicionar Curso")
        print("3. Excluir Aluno")
        print("4. Excluir Curso")
        print("5. Sair")
        
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            adicionar_aluno(db)
        elif escolha == '2':
            adicionar_curso(db)
        elif escolha == '3':
            excluir_aluno(db)
        elif escolha == '4':
            excluir_curso(db)
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")
        
        time.sleep(2)

if __name__ == "__main__":
    main()