conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)            # Elementos do "b" estão todos dentro do "a"?          (False)
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)            # Elementos do "a" estão todos dentro do "b"?          (True)
print(resultado)