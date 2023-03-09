# Crie um programa que leia 4 alunos e os sotei para limpar o quadro
from random import shuffle,choice
print("-"*14,"Alunos a Apresentar","-"*14)
alu1 = input("Digite o nome do aluno:")
alu2 = input("Digite o nome do aluno:")
alu3 = input("Digite o nome do aluno:")
alu4 = input("Digite o nome do aluno:")
list = [alu1,alu2,alu3,alu4]
shuffle(list)
print("Alunos a apresentar em sequencia ")
print(list)
print("-"*50)