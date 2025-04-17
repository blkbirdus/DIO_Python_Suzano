# Anotações sobre o curso de python

## 01. Tipos em Python

- Os tipos built-in em python são:

    |Nome do Tipo| Em python|
    |---|---|
    |Texto|str|
    |Numérico|int, float, complex|
    |Sequência|list, tuple, range|
    |Mapa|dict|
    |Coleção|set, frozenset|
    |Booleano|bool|
    |Binário|bytes, bytearray, memoryview|

- Tipos Booleanos são representados por 0 (verdadeiro) e 1 (falso) ou por True e False
- Strings e Listas vazias são consideradas false

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
    int(preco_produto)
    ```

## 04. Input e Output

- Para dar Input no seu código, use a função input()

    ```bash
    preco_produto = float(input())
    ```

- Para output: print()

    ```bash
    nome = marina
    idade = 21
    print(nome,idade, sep=": ", end=" anos\n") 
    ```

  - `sep` indicará a separação entre os valores indicados
  - `end` indicará como o output terminará

