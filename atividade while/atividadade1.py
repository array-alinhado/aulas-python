import os
os.system("cls || clear")

"""Desenvolva um programa que conte quantos números negativos foram inseridos pelo usuário usando um laço while. O programa deve parar quando o usuário inserir 0 ou um número positivo. Mostre a quantidade de números negativos."""

contador = 0
n = 1
 
while True:
    n =  int(input("digite um valor: "))


    if n <= -1:
        contador += 1

    else:
        print("fim")
        break