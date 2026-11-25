class Alunos:
    def __init__(self, nome, idade,cpf, plano, peso):
        self.nome = nome
        self.idade = idade
        self.plano = plano
        self.cpf = cpf
        self.peso = peso

lista_alunos = []

def cadastrar_aluno(lista_alunos):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    plano = input("Digite o nome do plano: ")
    while True:
        cpf = input("Digite o cpf do aluno: ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        print("\nCPF inválido, por favor digite um CPF válido com 11 digitos.")
    peso = (input("Digite o peso do aluno: "))

    aluno = Alunos(nome, idade, cpf, plano, peso)

    dados_aluno = {
        "nome": aluno.nome,
        "idade": aluno.idade,
        "cpf": aluno.cpf,
        "plano": aluno.plano,
        "peso": aluno.peso
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

def dados_aluno(lista_alunos):
    cpf_busca = input("Digite o cpf do aluno: ").strip()
    for aluno in lista_alunos:
        if aluno["cpf"] == cpf_busca:
            print("\nNome do aluno: ", aluno["nome"])
            print("\nIdade do aluno: ", aluno["idade"])
            print("\nCPF: ", aluno["cpf"])
            print("\nPlano do aluno: ", aluno["plano"])
            print("\nPeso do aluno: ", aluno["peso"])

while True:
    print("\n=== MENU ACADEMIA ===")
    print("1 - Cadastrar aluno")
    print("2 - Verificar plano")
    print("3 - Alterar plano")
    print("4 - Mostar dados do aluno")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno(lista_alunos)
    elif opcao == "2":
        verificar_plano(lista_alunos)
    elif opcao == "3":
        alterar_plano(lista_alunos)
    elif opcao == "4":
        dados_aluno(lista_alunos)
    elif opcao == "0":
        print(f"\nSaindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente!")







