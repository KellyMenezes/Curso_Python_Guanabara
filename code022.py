"""Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""

nome = input("Digite seu nome:").strip()
nome1 = nome.split()
nome2 = len(nome) - nome.count(" ")
print("Seu nome com letras maiúsculas é",nome.upper())
print("Seu nome com letras minúsculas é",nome.lower())
print("Seu nome tem ",nome2,"letras(Sem espaços).")
print("Seu primeiro nome tem ",len(nome1[0]),"letras.")
