"""Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""

nome = str(input("Digite seu nome:"))
espaços = len(nome) - nome.count(" ")
Fname1 = nome.find(" ")
nome1 = nome.split(" ")
print(f"Seu nome com todas as letras maiúsculas é {nome.upper()}.")
print(f"Seu nome com todas as letras minúsculas é {nome.lower()}.")
print(f"Seu nome contém {espaços} letras.")
print(f"Seu primeiro nome {nome1[0]} tem {Fname1} letras.")
