def main():
    n = int(input("Quantos itens você deseja pedir? "))

    total = 0

    for i in range(1, n + 1):
        pedido = input("Digite o nome e o valor do item separados por espaço: ").split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    desconto = input("Digite o valor do cupom (10 para 10% ou 20 para 20%): ")

    if desconto == "10%":
        total *= 0.9
    elif desconto == "20%":
        total *= 0.8

    print(f"Valor total: {total:.2f}")

if __name__ == "__main__":
    main()
