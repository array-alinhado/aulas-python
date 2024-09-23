import os
os.system("cls || clear")


pessoa = list()
dados = list()
totmaior = totmenor = 0


for c in range(0,3):
    dados.append(str(input("digite seu nome: ")))
    dados.append(int(input("digite sua idade: ")))
    pessoa.append(dados[:])
    dados.clear()


for p in pessoa:
    if p[1] >= 21:
        print(f"{p[0]} e maior de idade.")
        totmaior += 1
    else: 
        print(f"{p[0]} e menor de idade.")
        totmenor += 1
print(pessoa)