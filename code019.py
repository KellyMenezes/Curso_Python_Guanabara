#escrela um programa que leia 3 nomes de alunos e os sortei-os para uma apresentação
from random import choice
print("--"*12,"Aluno a apagar o quadro", "--"*12)
nome1 = input("Digite o nome do aluno:")
nome2 = input("Digite o nome do aluno:")
nome3 = input("Digite o nome do aluno:")
nome4 = input("Digite o nome do aluno:")
lista = choice([nome1,nome2,nome3,nome4])
print(f"O Aluno escolhido foi {choice}.")
print("--"*24)