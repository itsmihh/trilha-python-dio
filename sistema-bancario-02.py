import copy
from datetime import datetime

def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [n] Criar Usuário
    [c] Criar Conta Corrente

    => """

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    usuarios = []
    dados = {
        "nome": None,
        "dt_nascimento": None,
        "cpf": None,
        "endereco": {"logradouro": None, "numero": None, "bairro": None, "cidade": None, "estado": None}
    }

    numero_das_contas = 0

    contas = []
    dados_contas = {
        "numero_conta": numero_das_contas,
        "agencia": "0001",
        "conta_usuario": None
    }

    

    while True:
        opcao = input(menu)

        if opcao == 'd':
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == 's':
            saldo, extrato, limite, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == 'e':
            ver_extrato(extrato, saldo)
        elif opcao == 'n':
            usuarios = criar_usuario(dados, usuarios)
            print("\nLista de usuários:")
            for usuario in usuarios:
                print(usuario)
        elif opcao == 'c':
            contas, numero_das_contas = criar_conta_corrente(contas, dados_contas, usuarios, numero_das_contas)
            print("\nLista de contas:")
            for conta in contas:
                print(conta)
        elif opcao == 'q':
            print("Saindo...\n Obrigada pela preferência :)")
            break
        else: 
            print("Opção inváilida, por favor tente novamente!")

def depositar(saldo, extrato_deposito):
    print("Depósito")
    deposito = float(input("Qual valor deseja depositar? R$ => "))

    data_hora_atual = datetime.now()
    hora_brasil = "%d/%m/%Y às %H:%M"

    if deposito > 0:
        saldo += deposito
        extrato_deposito.append(f"Depósito de R${deposito: .2f} [{data_hora_atual.strftime(hora_brasil)}]\n")
        print("Depósito realizado com sucesso!")
    else:
        print("Não foi possível realizar o depósito! Valor inválido")
    
    return saldo, extrato_deposito


def sacar(saldo, extrato, limite_saque, saques_realizados, LIMITE_SAQUES):
    print("Saque")
    saque = float(input("Qual valor deseja sacar? => R$ "))

    data_hora_atual = datetime.now()
    hora_brasil = "%d/%m/%Y às %H:%M"

    if saque <= 0:
        print("Não foi possível sacar! Valor inválido!")
    elif saque > saldo:
        print("Não foi possível sacar! Saldo insuficiente!")
    elif saque > limite_saque:
        print("Não foi possível sacar! Você excedeu o limite por saque!")
    elif saques_realizados >= LIMITE_SAQUES:
        print("Você excedeu o número de saques diários!")
    else:
        saldo -= saque
        saques_realizados += 1
        extrato.append((f"Saque de R${saque: .2f} [{data_hora_atual.strftime(hora_brasil)}]\n"))
        print("Saque realizado com sucesso!")
    
    return saldo, extrato, limite_saque, saques_realizados

def ver_extrato(extrato, saldo):
    print("Extrato")
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
        print(f"Saldo: R${saldo: .2f}")


def criar_usuario(dados, usuarios):
    print("Cadastrar Novo Usuário \n")

    dados["nome"] = input("Nome do usuário: ")
    dados["dt_nascimento"] = input("Data de nascimento: ")
    dados["cpf"] = input("CPF: ")
    dados["endereco"]["logradouro"] = input("Nome da rua: ")
    dados["endereco"]["numero"] = input("Número: ")
    dados["endereco"]["bairro"] = input("Nome do bairro: ")
    dados["endereco"]["cidade"] = input("Cidade: ")
    dados["endereco"]["estado"] = input("Sigla Estado: ")


    for usuario in usuarios:
        if usuario["cpf"] == dados["cpf"]:
            print("CPF já cadastrado!")
            return usuarios
        
    usuario_novo = copy.deepcopy(dados) 
    usuarios.append(usuario_novo)
    print("Usuário cadastrado com sucesso!")
    return usuarios
    

def criar_conta_corrente(contas, dados_contas, usuarios, numero_das_contas):
    print("Criar Conta Corrente \n")

    cpf = input("Informe o CPF do usuário para vincular a conta: ")

    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            numero_das_contas += 1
            dados_contas["conta_usuario"] = usuario["nome"]
            dados_contas["numero_conta"] = numero_das_contas
            # dados_contas["conta_usuario"] = input("Conta usuário: ")
            
            conta_nova = copy.deepcopy(dados_contas)
            contas.append(conta_nova)
            print(f"Conta corrente do usuário {dados_contas["conta_usuario"]} criada com sucesso!")
            return contas, numero_das_contas
    
    # print("Agência: 0001")
    print("Usuário não encontrado")
    return contas, numero_das_contas
    

main()