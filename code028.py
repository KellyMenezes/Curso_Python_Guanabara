"""Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""
from random import randint
num = randint(0,5)
print("Vou pensar em um número...(0 até 5)")
jog1 = int(input("Em que número eu pensei?"))
if num == jog1:
    print(f"Você acertou **\__/**!!!Pensei no número {num}!")
    print("Parabéns!!!")
else:
    print(f"Você errou @_@...Pensei no número {num}")
