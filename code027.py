"""Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente."""
Nome = str(input("Digite seu nome completo:")).strip().split()
print("Seja bem-vindo")
print("Seu primeiro nome é",Nome[0]+".")
print("E seu ultimo nome é",Nome[len(Nome)-1]+".")
