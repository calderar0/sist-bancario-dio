menu = """
    Bem Vindo ao Banco DIO
    Escolha uma operação:
    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [q] - Sair
"""

print(menu)

saldo = 0
limite = 500
saques = 0
extrato = ""
LIMITESAQUES = 3

while True:
    opcao = input("Escolha uma opção: ")
    if opcao == 'd':
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    elif opcao == 's':
        if saques < LIMITESAQUES:
            valor = float(input("Digite o valor do saque: "))
            if saldo - valor >= 0 and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                saques += 1
            elif valor > limite:
                print("Limite de valor para sacar excedido")
            else:
                print("Saldo insuficiente")
        else:
            print("Limite de saques atingido")
    elif opcao == 'e':
        print("\nExtrato bancário:")
        print(extrato + f"Saldo: R$ {saldo:.2f}")
    elif opcao == 'q':
        break
    else:
        print("Operação inválida, selecione novamente a operação desejada")


