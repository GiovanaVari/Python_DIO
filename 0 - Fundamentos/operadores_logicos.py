                    # ***** TABELA AND *****
print(True and True and True)                       # V V V = V
print(True and False and True)                      # V F V = F
print(False and False and False)                    # F F F = F

                    # ***** TABELA OR *****
print(True or True or True)                         # V V V = V
print(True or False or False)                       # V F V = V
print(False or False or False)                      # F F F = F

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)