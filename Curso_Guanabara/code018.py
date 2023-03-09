#crie um programa que mostre o seno ,coseno tangente de um numero real
import math
Angulo = float(input("Digite um ângulo:"))
seno = math.sin(math.radians(Angulo))
coseno = math.cos(math.radians(Angulo))
tangente = math.tan(math.radians(Angulo))
print(f"O ângulo {Angulo} tem o seno {seno:.2f} ,coseno{coseno:.2f} e a tangente {tangente:.2f}.")