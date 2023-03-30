#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
print("Sua cidade começa com Santo")
city = input("Digite o nome de uma cidade:").split()
city = city[0].upper() == "SANTO"
print(city)
