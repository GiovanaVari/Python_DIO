conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)               # Os elemento do "a" não estão em "b"?     (True)
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)               # Os elementos do "a" não estão em "c"?     (False)
print(resultado)