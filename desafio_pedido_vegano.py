def main():
    num_pedidos = int(input("Quantos pedidos você deseja fazer? "))
    
    for i in range(1, num_pedidos + 1):
        prato = input(f"Digite o nome do prato {i}: ")
        calorias = int(input(f"Digite a quantidade de calorias do prato {i}: "))
        eh_vegano = input(f"O prato {prato} é vegano? (S/N) ")
        
        if eh_vegano.upper() == "S":
            eh_vegano = "(Vegano)"
        else:
            eh_vegano = "(Nao-vegano)"

        print(f"Pedido {i}: {prato} {eh_vegano} - {calorias} calorias")

if __name__ == "__main__":
    main()