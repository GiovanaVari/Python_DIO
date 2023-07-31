lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)                                # Mostra toda a lista                       ([1, "Python", [40, 30, 20]])

print(id(l2), id(lista))                    # Mostra o ID das duas listas

l2[0] = 14                                  # Adiciona o 14 na posição 0 da lista l2

print(l2)                                   # Mostra a l2
print(lista)                                # Mostra a lista 