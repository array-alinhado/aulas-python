import os
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Checagem:
    nome: str
    idade: int

QTD = 1

lista_festa = []

for i in range(QTD):
    checagem = Checagem(
        nome = input("fale seu nome: "),
        idade = int(input("fale sua idade: "))
    )
    lista_festa.append(checagem)

nome_arquivo = "festa_now!!!.txt"

with open(nome_arquivo,"a") as festa_login:
    for checagem in lista_festa:
        festa_login.write(f"nome:{checagem.nome}, idade:{checagem.idade}\n")
festa_login.close()

with open(nome_arquivo, "r") as arquivo_origins:
    for linha in arquivo_origins:
        nome,idade = linha.strip().split(",")
        lista_festa.append(Checagem(nome=nome, idade = int(idade)))
festa_login.close()

print("DADOS SALVOS!!!!")

print("EXIBINDO!!!")

for checagem in lista_festa:
    print(f"nome: {checagem.nome}")
    print(f"idade: {checagem.idade}")
