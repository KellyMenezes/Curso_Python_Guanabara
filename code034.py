# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual o seu sálario?"))
if salario <= 1250.00 :
    print(f"Seu sálario de {salario:.2f} com aumento de 15% vai ser R${salario + salario * 15 / 100:.2f} ")
else :
    print(f"Seu sálario de {salario:.2f} com aumento de 10% vai ser R${salario + salario * 10 / 100:.2f} ")


#  Segundo jeito de fazer.
if salario <= 1250.00 :
    print(f"Seu sálario de {salario:.2f} com aumento de 15% vai ser R${salario + salario * 15 / 100:.2f} ")
elif salario > 1250.00 :
    print(f"Seu sálario de {salario:.2f} com aumento de 10% vai ser R${salario + salario * 10 / 100:.2f} ")
