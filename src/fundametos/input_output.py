saldo = 1500.50
print(f"Saldo Atual: R$ {saldo}")
print("Digite o valor que deseja sacar:")
valor_saque = float(input())
saldo -= valor_saque
print(f"Novo Saldo: R$ {saldo}")

nome = "Marina"
print(nome, saldo, sep=": ")

nome1, nome2, nome3 = "Marina", "Capella", "Violeta"
print(nome1, nome2, sep=" ama ", end=" ")
print("e Violeta")

idade = 21
print(nome,idade, sep=": ", end=" anos\n")