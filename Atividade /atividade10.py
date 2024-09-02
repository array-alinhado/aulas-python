import os
os.system("cls || clear")
import time


"""Escreva um programa que calcule a soma dos números ímpares de 1 a 9 utilizando um laço `for`."""
soma = 0
impares = 0

for numero in range (1,10,2):
    print(f"{numero}")
    if numero  % 2 != 0:
            impares = impares + 1
            soma += numero

time.sleep(4)
print(f"soma: {soma}")
