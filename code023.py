#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Num = int(input("Digite um número até quatro casas:"))
u = Num // 1 % 10
d = Num // 10 % 10
c = Num // 100 % 10
m = Num // 1000 % 10
print(f"Unidade {u}")
print(f"Dezena  {d}")
print(f"Centena {c}")
print(f"Milhar  {m}")
