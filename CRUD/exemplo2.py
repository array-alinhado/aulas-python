import os
os.system("cls || clear")
from dataclasses import dataclass


# estrutura de dados.
@dataclass
class Aluno: 
    nome: str
    idade: int

QTD = 2

lista_alunos = []

for i in range(QTD):
    aluno = Aluno(
        nome = input("digite seu nome: "),
        idade = int(input("digite sua idade:  "))

    )
    lista_alunos.append(aluno)

print("=== exibindo dados ====")


nome_arquivo = "lista_alunos_SENAI.txt"

with open(nome_arquivo, "a") as arquivo_alunos:
    #percorrendo vetor/lista
    for aluno in lista_alunos:
        #escrevendo no arquivo uma linha de cada vez.
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")
#fechando o arquivo
arquivo_alunos.close()

print("==== dados salves ====")

#lendo dados de um arquivo.

print("acessando arquivos...")
with open(nome_arquivo, "r") as arquivo_origem:
    for linha in arquivo_origem:
        nome,idade = linha.strip().split(",")
        lista_alunos.append(Aluno(nome=nome, idade = int(idade)))

arquivo_alunos.close()
print("=== exibindo... ===")
for aluno in lista_alunos:
    print(f"nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")
