import os
os.system("cls || clear")
contador = 0
numero = 10

"""Escreva um programa que multiplique um número inicial por um fator dado pelo usuário até que o produto exceda 100. Exiba o produto final e o número de multiplicações realizadas."""

while True:
    for i in range(1):
       fator = float(input("digite seu fator: "))
       multiplicacao = numero * fator
       contador += 1

    if multiplicacao > 100:
        break

print(f"Produto final: {multiplicacao}")
print(f"Contador: {contador}")