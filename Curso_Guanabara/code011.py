# Faça um programa que leia altura,metros e diga a quantidade necessaria para pintar as pareces 
altura = float(input("digite a altura em metros (com ponto)"))
largura = float(input("Digite sua largura em metros (com ponto)"))
area = altura*largura
tinta = area / 2
print(f"Sua área pintada é {area}m^2 e a quantidade de litros necessaria é {tinta}l.")