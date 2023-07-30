saldo = 1000
limite = 500

print(saldo is limite)              # Oculpa a msm região de memoria?
print(saldo is not limite)          # Não oculpa a msm região de memoria?

saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)