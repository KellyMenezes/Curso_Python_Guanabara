#Faça um programa que leia em metros e os converta em outra medidas de distância
metros = float(input("Digite os metros que são precisos: "))
km = metros / 1000
h  = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros *100
mm = metros * 1000
print("Sua tabela de medidas")
print(f"{km:.3f}Km")
print(f"{h:.2f}h")
print(f"{dam:.1f}dam")
print(f"{metros:.0f}m")
print(f"{dm:.0f}dm")
print(f"{cm:.0f}cm")
print(f"{mm:.0f}mm")
