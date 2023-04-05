"""Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""
vel = int(input("Qual a velocidade do seu carro em km/h:"))
multa = 80 - vel
if vel > 80 :
    print("Você foi multado @_@!!!")
    print("A multa vai custar R$7,00 por cada Km/h acima do limite.")
    print(f"Você deve pagar R${multa *(-7.00):.2f}!")
print("Tenha um bom dia :-),dirija com segurança!!!")
