numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)                                          # Mostra o set/conjunto                             {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)                                      # Descarta o elemento informado se existir
numeros.discard(45)                                     # Descarta o elemento informado se existir

print(numeros)                                          # Mostra o set/conjunto                             {2, 3, 4, 5, 6, 7, 8, 9, 0}