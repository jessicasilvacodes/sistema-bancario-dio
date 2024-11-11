
menu = """

[d] Depositar
[s] Sacar
[e] Visualizar o extrato
[q] Sair do sistema

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3      #variavel constante


while True:

    opcao = input(menu)

    if opcao == "d":      #depositar
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:      #evitar depósitos de valores negativos
            saldo = saldo + valor
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":      #sacar
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo      #verificar se excedeu o saldo

        excedeu_limite = valor > limite      #verificar se excedeu o limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES      #verificar se o usuário já fez os 3 saques diários

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o valor o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")

        elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + f"Saque: R$ {valor:.2f}\n"
            numero_saques = numero_saques + 1      #para registrar que já fez saques anteriormente 

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":      #visualizar o extrato
        print("\nEXTRATO: ")
        print("Não foram realizadas movimentações." if not extrato else extrato)      #se não foram feitas operações
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":      #sair do sistema
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
