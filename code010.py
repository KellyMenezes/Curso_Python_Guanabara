#Faça um programa que leia quanto dinhero uma pessoa tem e mostra quantos dolas ela pode comprar
carteira_dinheiro = float(input("Digite quanto dinheiro você tem na carteira(Digite com ponto):R$"))
dolar = 5.09
comprar = carteira_dinheiro/dolar
print(f"Parabéns você pode comprar US$ {comprar:.2f} .")

