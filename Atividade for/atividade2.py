import os
os.system("cls || clear")
import time


"""Crie um programa que, utilizando um laço `for`, calcule a soma dos números de 1 a 5 e mostre o resultado."""


soma = 0

for i in range(2):
    numero = int(input("digite seu numero: "))
    soma += numero

time.sleep(1)
print(f"soma: {soma}")