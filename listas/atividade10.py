import os
os.system("cls || clear")


ano_nascimento = int(input("digite seu ano: "))


def calcular_idade(ano_nascimento):
    idade = 2024 - ano_nascimento
    return idade

idade = calcular_idade (ano_nascimento)
print(f"idade: {idade}")