#Crie um programa que leia o cateto oposto e adjacente de um trianfulo e mostre o conteudo da hipotenusa 
import math 
cateto_adjacentex = float(input("Digite cateto adjacente: "))
cateto_opostoy = float(input("Digite o cateto oposto: "))
hipotenusa_c = math.hypot(cateto_adjacentex,cateto_opostoy)
print(f"O comprimento da hipotenusa é {hipotenusa_c:.2f}")