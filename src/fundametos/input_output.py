saldo = 1500.50
print(f"Saldo Atual: R$ {saldo}")
print("Digite o valor que deseja sacar:")
valor_saque = float(input())
saldo -= valor_saque
print(f"Novo Saldo: R$ {saldo}")

nome = "Marina"
print(nome, saldo, sep=": ")

nome1, nome2 = "Marina", "Capella"
print(nome1, nome2, sep=" ama ", end="...")