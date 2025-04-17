print("Digite o preço base do cachorro:")
preco = "100"
print(preco)

print("Digite a idade:")
idade = "1"
print(idade)

preco_final = float(preco) * int(idade) / 2.75

print(f"Doberman. idade: {idade} anos || preço final: R$ {preco_final: .2f}")

print(type(preco))
print(type(int(idade)))
