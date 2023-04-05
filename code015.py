# leia km percoridos e a quantidades de dias que foi alugado .Diga o preço sabendo que custa R$60 por dia e R$0,15 por litro
print("Aluguel de carros dia e km")
dia = int(input("Digite a quantidade de dias em que o carro foi alugado:"))
km = float(input("Digite a quantidade de kilometros percorridos:"))
dia = dia * 60.00
km = km * 0.15
pagar = dia + km
print(f"O preço a ser pago é de R${pagar:.2f}")