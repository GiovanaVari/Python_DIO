def informar_tempo_de_entrega():
    nome_restaurante = input("Digite o nome do restaurante: ")
    tempo_espera = input("Digite o tempo de espera em minutos: ")

    mensagem = f"O restaurante {nome_restaurante} entrega em {tempo_espera} minutos."
    print(mensagem)

informar_tempo_de_entrega()
