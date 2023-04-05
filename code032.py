# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input("Digite um ano qualquer:"))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto!!!;-)")
else:
    print(f"Seu ano {ano} não é bissexto @__@!")
