from db_config.connection import db

from app.alunos import listar_alunos, adicionar_aluno, excluir_aluno
from app.cursos import listar_cursos, adicionar_curso, excluir_curso
from app.matriculas import matricular_aluno, listar_matriculas_aluno, deletar_matricula
from app.queries import contar_alunos_por_curso, mostrar_cadeia_prerequisitos, listar_alunos_sem_matricula
from app.utils import limpar_tela, pausar

def main():
    while True:
        limpar_tela()
        print("Sistema Acadêmico - Menu Principal")
        print("""
Opções:
1. Adicionar Aluno
2. Excluir Aluno
3. Adicionar Curso
4. Excluir Curso
5. Matricular Aluno em Curso
6. Listar Cursos de um Aluno
7. Desfazer Matrícula
8. Relatório: Qtd. de Alunos por Curso
9. Relatório: Pré-requisitos por Curso
10. Relatório: Alunos sem Matrícula
11. Sair
""")
        escolha = input("Escolha: ").strip()

        if escolha == '1':
            adicionar_aluno()
        elif escolha == '2':
            excluir_aluno()
        elif escolha == '3':
            adicionar_curso()
        elif escolha == '4':
            excluir_curso()
        elif escolha == '5':
            ak = input("KEY do aluno: ").strip()
            ck = input("KEY do curso: ").strip()
            matricular_aluno(ak, ck)
        elif escolha == '6':
            ak = input("KEY do aluno: ").strip()
            listar_matriculas_aluno(ak)
        elif escolha == '7':
            ak = input("KEY do aluno: ").strip()
            ck = input("KEY do curso: ").strip()
            deletar_matricula(ak, ck)
        elif escolha == '8':
            contar_alunos_por_curso()
        elif escolha == '9':
            ck = input("KEY do curso: ").strip()
            mostrar_cadeia_prerequisitos(ck)
        elif escolha == '10':
            listar_alunos_sem_matricula()
        elif escolha == '11':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

        pausar()

if __name__ == "__main__":
    main()
