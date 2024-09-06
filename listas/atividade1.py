import os
os.system("cls || clear")


def media(n1, n2):
    soma = n1 + n2
    media = soma /2
    return media 

nota1 = float(input("digite seu primeiro numero: "))
nota2 = float(input("digite seu segundo numero: "))



media = media (nota1, nota2)

print(f"media {media}")