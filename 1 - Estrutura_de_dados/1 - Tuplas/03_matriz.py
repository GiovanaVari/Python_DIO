matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])                # Mostra elementos da posição L0            ((1, "a", 2))
print(matriz[0][0])             # Mostra elemento da posição L0 C0          (1)
print(matriz[0][-1])            # Mostra elemento da posição L0 C-1         (2)
print(matriz[-1][-1])           # Mostra elemento da posição L-1 C-1        ("c")