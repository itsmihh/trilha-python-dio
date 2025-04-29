menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print("Depósito")
        deposito = float(input("Qual valor deseja depositar? R$ => "))

        if deposito > 0:
            saldo += deposito
            extrato += (f"Depósito de R${deposito: .2f}\n")
            print("Depósito realizado com sucesso!")

        else:
            print("Não é possível depositar um valor negativo!")


    elif opcao == 's':
        print("Saque")

        saque = float(input("Qual valor deseja sacar? => R$ "))

        if saque <= 0:
            print("Não é possível sacar um valor negativo!")
          
        
        elif saque > saldo:
            print("Você não possui esse valor na conta!")

        elif saque > limite:
            print("Você excedeu o limite por saque!")
        
        elif numero_saques > LIMITE_SAQUES:
            print("Você excedeu o número de saques diários!")

        else:
            saldo -= saque
            numero_saques += 1
            extrato += (f"Saque de R${saque: .2f}\n")
            print("Saque realizado com sucesso!")


    elif opcao == 'e':
        print("Extrato")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R${saldo: .2f}")


    elif opcao == 'q':
        print("Saindo...\n Obrigada pela preferência :)")
        break

    else:
        print("Opção inválida, tente novamente")