#Calcular a média é uma das operações estatísticas mais básicas e úteis para resumir um conjunto de dados. Dada uma lista de números, você deve calcular a média aritmética desses números.

# Receber a lista do usuário
entrada = input()
# Convertee a string de entrada em uma lista de números
lista = [int(numero) for numero in entrada.split(",")]

# Calcula a soma dos números na lista
soma = sum(lista)
# Calcula a quantidade de elementos na lista
quantidade = len(lista)
# TODO: Calcule a média aritmética:
media = soma/quantidade

# Exibir a média com duas casas decimais
print(f'{media:.1f}')
