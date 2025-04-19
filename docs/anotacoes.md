# Anotações sobre o curso de python

## 01. Tipos em Python

- Os tipos built-in em python são:

    |Nome do Tipo| Em python|
    |---|---|
    |Texto|`str`|
    |Numérico|`int`, `float`, `complex`|
    |Sequência|`list`, `tuple`, `range`|
    |Mapa|`dict`|
    |Coleção|`set`, `frozenset`|
    |Booleano|`bool`|
    |Binário|`bytes`, `bytearray`, `memoryview`|

- Tipos Booleanos são representados por 0 (False) e 1 (True)

## 02. Variáveis e Constantes

- Não exite a definição de uma constante em python, pois não existe uma palavra reservada.
  - Existe uma convenção para indicar que a variável é uma constante, colocando o nome da variável em letras maiúsculas

### Boas Praticas

- Usar snake case:

    ```bash
    tipos_de_produtos, nome_aluno
    ```

- Escolher nomes sugestivos

    ```bash
    tip_p, nome_a # evitar o uso de abreviações e variáveis com apenas uma letra, sempre seja bem descritível
    ```

- Constantes em maiúsculo

## 03. Conversão de tipos

- Para converter tipos em python você pode indicar `tipo_desejado`(`variável`)

    ```bash
    preco_produto = 150.67
    print(type(preco_produto)) # float
    int(preco_produto) # preco_produto = 150
    print(type(preco_produto)) # int
    ```

## 04. Input e Output

- Para dar Input no seu código, use a função input()

    ```bash
    preco_produto = float(input())
    ```

- Para output: print()

    ```bash
    nome = "marina"
    idade = 21
    print(nome,idade, sep=": ", end=" anos\n") # marina: 21 anos
    ```

  - `sep` indicará a separação entre os valores indicados

  - `end` indicará como o output terminará

## 05. Tipos de Operadores

### Aritméticos

- Precedência: `Parêntesis > Expoentes > Multiplicação > Divisão > Soma > Subtração`

- As operações de Multiplicação e Divisão/Soma e Subtração serão lidas da esquerda para a direita

### Comparação

- Utilizados para fazer comparações

- Os operadores de comparação são: `=` (Igual), `!=` (Diferente), `>` (Maior), `>=` (Maior ou Igual), `<` (Menor), `<=` (Menor ou Igual)

    ```bash
    saldo, saque = 500, 400
    print(saldo > saque) # True
    ```

### Atribuição

- Usados para definir o valor inicial ou sobrescrever o valor de uma variável

- Os operadores de atribuição são: `=, +=, -=, *=, /=, //=, %=, **=`

### Lógicos

- São operadores Lógicos: `and` e `or`

- Para indicar negação usa: `not`

- Strings e Listas vazias são consideradas `False`

    ```bash
    idade = 20
    tem_carteira = True

    print(idade >= 18 and tem_carteira)  # True
    print(not tem_carteira)              # False

    print(bool("")) # False

    ```

- Evitar usar uma expressão lógica muito longa em uma linha

    ```bash
    exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

    conta_normal_saldo_suficiente = (saldo >= saque) and (saque <= limite)
    conta_especial_saldo_suficiente = (conta_especial) and (saldo >= saque)
    exp_2 = conta_especial_saldo_suficiente or conta_normal_saldo_suficiente
    ```

### De Identidade

- Utilizado para fazer a comparação entre objetos, para conferir se elas estão no mesmo espaço de sistema

    ```bash
    saldo, limite = 200
    print(saldo is limite) # True, já que tem o mesmo valor
    ```

### De Associação

- Utilizado para verificar se um objeto está dentro de uma sequência

    ```bash
    frutas = ["Pera","Maçã","Limão"]
    print("Abóbora" in frutas) # True
    ```

