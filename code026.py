"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""
frase = input("Digite uma frase:").strip().upper()
print("Sua frase tem",frase.count("A"),"letras A")
print("Ela aparece a primeira vez na",frase.find("A")+1,"posição")
print("Ela aparece na",frase.rfind("A")+1,"posição")
