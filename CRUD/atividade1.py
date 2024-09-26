import os
os.system("cls || clear")
from  dataclasses import dataclass


#estrutura de dados.
@dataclass

class Client:
    nome: str 
    sobrenome: str
    idade: int
    altura: float
    peso: float

QTD = 4
for i in range(QTD):
    cliente = Client( 
    nome = input("digite seu nome: "),
    sobrenome = input ("digite seu sobrenome: "),
    idade = int(input("digite sua idade: ")),
    altura = float(input("digite sua altura: ")),
    peso =  float(input("digite sua altura: ")),
    )
    lista_clientes.append(Client)


# salvar um arquivo chamado: carteira_cliente.txt.
nome_arquivo = "carteira_cliente.txt"
# fazer leitura de dados do arquivo carteira_cliente.txt e mostre no terminal.  