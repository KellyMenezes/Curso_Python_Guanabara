# Crie um programa que leia o preço de um produto e de um disconto de 5%
produto = float(input("Digite o preço do produto:R$"))
desconto = produto - (produto * 0.05)
print(f"Seu produto custa {desconto:.2f} com 5% de desconto")