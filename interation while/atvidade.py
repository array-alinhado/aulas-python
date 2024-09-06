import os
os.system("cls || clear")
"""
Escreva um algoritmo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente. 
Calcule e mostre a média aritmética do aluno.
"""
soma = 0

while True:
    nota1 = float(input("digite sua nota1: "))
    nota2 = float(input("digite sua nota2: "))
    soma = soma + nota1 + nota2
    media = soma /2

    if nota1 < 0 or nota2 > 10:
        print("\na nota deve ser maoir ou igual 0 e maior q 10.")
    elif nota1 < 0 or nota2 > 10:
        print("\na nota deve ser maoir ou igual 0 e maior q 10.")
    else:    
        break
print(f"nota: {media}")