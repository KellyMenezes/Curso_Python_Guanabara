# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input("Digite um número:"))
b = float(input("Digite um número:"))
c = float(input("Digite um número:"))
if a + b > c and b + c > a and a + c > b:
    print("Você pode formar um triângulo!!!")
else:
    print("Você não pode formar um triângulo @_@.")

