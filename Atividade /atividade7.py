import os
os.system("cls || clear")
import time

"""Crie um programa que use um laço `for` para gerar e exibir os quadrados dos números de 1 a 5 (ou seja, 1², 2², 3², etc.)."""


for i in range(7):
    print(F"{i}² = {i * i}")
    time.sleep(1)