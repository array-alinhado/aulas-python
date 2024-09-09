import os
os.system("cls || clear")

def calculo_media(n1, n2):
    soma = n1 + n2
    media = soma /2
    return media

def reprovado_aprovador(media):
    if media < 7:
        print("reprovado")
    else:
        print("aprovado")

nota1 = float(input("digite sua 1 nota: "))
nota2 = float(input("digite sua 2 nota: "))

media_total = calculo_media(nota1, nota2)
print(f"media: {media_total}")

media_final(media_total)
