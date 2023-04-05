# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input("Digite um numero:"))
b = int(input("Digite um numero:"))
c = int(input("Digite um numero:"))
# Verificar qual número é o maior.
if a > b and a > c:
    print(f"O número {a} é o maior!")
elif b > a and b > c:
    print(f"O número {b} é o maior !")
else:
    print(f"O número {c} é o maior!")
# Verificar qual numero é o menor.
if a < b and a<c:
    print(f"O número {a} é o menor número!")
elif b < a and b < c :
    print(f"O número {b} é o menor numero!")
else:
    print(f"O número {c} é o menor numero")
