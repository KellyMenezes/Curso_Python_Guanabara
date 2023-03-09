# Crie um programa que leia um salario e de um aumento de 15%
salario = float(input("Digite seu salario(com ponto):"))
aumento = salario + (salario * 15 /100)
print(f"Seu salario de R${salario:.2f} aumentou para R${aumento:.2f}.Parabéns!!!")