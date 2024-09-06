import os
os.system("cls || clear")
import time


"""Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 4 linhas por 6  colunas de asteriscos (`*`)."""
largura = "* * * * * * * * * * * * * * * * * "
altura = "*****"

print (f"{largura}")
for letra in altura:
    print(f"{letra}                               {letra}")
print(f"{largura}")