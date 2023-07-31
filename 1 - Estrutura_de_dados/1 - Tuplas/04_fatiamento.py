tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])                            # Mostra a partir da posição 2                      ("t", "h", "o", "n")
print(tupla[:2])                            # Mostra ate a posição 2                            ("p", "y")
print(tupla[1:3])                           # Mostra os elementos nas posições de 1 a 3         ("y", "t")
print(tupla[0:3:2])                         # Mostra os elementos de 0 a 3 pulando 2            ("p", "t")
print(tupla[::])                            # Mostra a tupla toda                               ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])                          # Mostra a tupla toda em ordem invertida            ("n", "o", "h", "t", "y", "p")