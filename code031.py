# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input("Qual a distancia de sua viagem em Km/h?"))
if km <= 200 :
    print(f"Sua viagem custa R${km*0.50:.2f}")
else:
    print(f"Sua viagem custa R${km*0.45:.2f}")

