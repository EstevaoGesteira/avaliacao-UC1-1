class Alunos:
    def __init__(self, nome, idade,cpf, plano):
        self.nome = nome
        self.idade = idade
        self.plano = plano
        self.cpf = cpf

lista_alunos = []

def cadastrarAluno(lista_alunos):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    plano = input("Digite o nome do plano: ")
    while True:
        cpf = input("Digite o cpf do aluno: ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        print("\nCPF inválido, por favor digite um CPF válido com 11 digitos.")

    aluno = Alunos(nome, idade, cpf, plano)

    dados_aluno = {
        "nome": aluno.nome,
        "idade": aluno.idade,
        "cpf": aluno.cpf,
        "plano": aluno.plano
    }

    lista_alunos.append(dados_aluno)
    print("\nAluno cadastrado com sucesso!")

def verificar_plano(lista_alunos):
    cpf_busca = input("Digite o cpf do aluno: ").strip()
    for aluno in lista_alunos:
        if aluno["cpf"] == cpf_busca:
            print(f"\nAluno {aluno["nome"]} está no plano {aluno["plano"]}.")
            return
    print("\nAluno não encontrado!")

def alterar_plano(lista_alunos):
    cpf_busca = input("Digite o cpf do aluno: ").strip()
    for aluno in lista_alunos:
        if aluno["cpf"] == cpf_busca:
            aluno["plano"] = input("Digite o novo plano do aluno: ").strip()
            print("\nPlano alterado com sucesso!")
            return
    print(f"\nAluno não encontrado.")







