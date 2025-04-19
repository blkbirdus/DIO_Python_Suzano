saldo, saque, limite = 1000, 200, 100

print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)
print(not saldo >= saque or saque <= limite)
print()

saldo, limite, saque = 1000, 200, 250
conta_especial = True
exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp)

conta_especial = False
print(exp)

conta_normal_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_saldo_suficiente = conta_especial and saldo >= saque
exp_2 = conta_especial_saldo_suficiente or conta_normal_saldo_suficiente
print(exp_2)
    
"""
    Strings e Listas vazias são consideradas false
"""

print(bool(""))