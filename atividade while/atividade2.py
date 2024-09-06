import os
os.system("cls || clear")

""" Escreva um programa que use um laço while para encontrar o primeiro número maior que 50 que seja divisível por 7. Exiba esse número."""

numero = 51 

while True:
    if numero % 7 == 0:
        print(f"numero: {numero}")
        break
    numero += 1