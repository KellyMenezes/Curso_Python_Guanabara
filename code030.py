# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input("Digite um numero:"))
par_impar = num % 2
if par_impar == 0:
    print(f"Este número [{num}] é par!!!")
else:
    print(f"Este número [{num}] é impar!!!")
