import os
os.system("cls || clear")

soma = 0
media = 0

for i in range (4):
    notas = float(input("digite sua media: "))

    soma = soma + notas
media = media + notas / 4



print(f"media: {media}")