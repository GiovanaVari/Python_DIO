lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])                                # Mostra a partir da posição 2 (["t", "h", "o", "n"])
print(lista[:2])                                # Mostra até a posição 2 (["p", "y"])
print(lista[1:3])                               # Mostra da posição 1 a 3 (["y", "t"])
print(lista[0:3:2])                             # Mostra da posição 0 a 3 pulando 2 (["p", "t"])
print(lista[::])                                # Mostra tudo e na ordem (["p", "y", "t", "h", "o", "n"])
print(lista[::-1])                              # Mostra tudo em ordem invertida (["n", "o", "h", "t", "y", "p"])