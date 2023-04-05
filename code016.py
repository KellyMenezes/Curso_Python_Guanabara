# Leia um numero qualquer e mostre somente sua parte inteira(importe uma blioteca) 
from math import trunc
real = float(input("Digite um numero real:"))
real1 = trunc(real)
print(f"O numero real {real} sendo {real1} sua parte só inteira .")