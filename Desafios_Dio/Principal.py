Menu = ('''
[d] Depositar    
[s] Sacar
[e] Extrato
[q] Sair

Opção: ''')

Saldo = 0
Limite = 500
Extrato = ""
Numero_Saques = 0
Limite_Saques = 3

while True:

    opcao = input(Menu)

    if opcao == "d":

        Valor = float(input("Digite o valor do deposito: "))
        if Valor > 0:
            Saldo += Valor
            Extrato += f"Deposito de R$ {Valor:.2f}\n"

        else:
            print("O valor Digitado e menor que Zero! Operação falhou")

    elif opcao == "s":

        Valor = float(input("Qual o valor da retirada: "))

        Ultrapassou_L = Valor > Saldo
        Ultrapassou_L_S = Valor > Limite
        Ultrapassou_S = Numero_Saques >= Limite_Saques

        if Ultrapassou_L:
            print("Você não tem saldo o suficiente")

        elif Ultrapassou_L_S:
            print("O limite de saque por dia e de R$ 500,00")

        elif Ultrapassou_S:
            print("Você alcançou o numero maximo de saques por dia")

        elif Valor > 0:
            Saldo -= Valor
            Extrato += f"Valor retirado de R$ {Valor:.2f}\n"
            Numero_Saques += 1

        else:
            print("operação falhou!")

    elif opcao == "e":
        print("Extrato".center(10,'='))
        if not Extrato:
            print("Nenhuma movimetação foi efetuada")

        else:
            print(Extrato)

        print(f"Saldo: {Saldo:.2f}")

        print("="*10)

    elif opcao == "q":
        break

    else:
        print("Falha?!")


