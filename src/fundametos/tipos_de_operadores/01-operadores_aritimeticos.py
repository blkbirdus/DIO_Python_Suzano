# modulo:
print(10 % 3)

# exponenciação:
print(3 ** 3)

# divisão inteira
a = 20 / 10
b = 20 //10
print(type(a))
print(type(b))

"""
precedência:
    Parêntesis > Expoentes > Multiplicação > Divisão > Soma > Subtração
    As operações de Multiplicação e Divisão/Soma e Subtração serão lidas da esquerda para a direita
"""


import math

a, b, c = 4 , -6, 2

print(f"Formula de bhaskara A = ({a}), B = ({b}), C = ({c})")
delta = (b ** 2) - (4 * a * c)
bhaskara_soma = (-b + math.sqrt(delta)) / (2 * a)
bhaskara_subtracao = (-b - math.sqrt(delta)) / (2 * a)

print(f"Valor de X¹ = {bhaskara_soma}")
print(f"Valor de X² = {bhaskara_subtracao}")