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

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:                                                                       # verifica se o valor é negativo
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"                                        # passa a info pro extrato

        else:
            print("Operação falhou! O valor informado é inválido.")                         # mostra messagem quando o valor é negarivo

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo                                                       # verifica se excedeu o saldo

        excedeu_limite = valor > limite                                                     # verifica se excedeu o limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES                                     # verifica se excedeu o limite de saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")                        # mensagem ao exceder o saldo

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")                     # mensagem ao exceder o limite

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")                     # mensagem ao exceder o limite de saque

        elif valor > 0:                                                                     # verifica se o valor é maior que 0 e efetua o saque
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)            # se extrato estiver vazio, mostra a mensagem
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")