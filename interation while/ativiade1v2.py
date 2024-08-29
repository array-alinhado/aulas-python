import os
os.system("cls || clear")
"""
Escreva um algoritmo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente. 
Calcule e mostre a média aritmética do aluno.
"""
soma = 0
QUANTIDADE_NOTAS = 2 

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input("digite{i + 1}º nota:  "))

        if nota >= 0 or nota <= 10:
            break
    media += nota
media = soma / QUANTIDADE_NOTAS

