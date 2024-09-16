import os
os.system("cls || clear")
QUANTIDADE_NUMEROS = 5
numeros_vetorizado = []

print("====solicitando dados====")
for i in range(QUANTIDADE_NUMEROS):
    numeros = int(input("digite seu numero: "))
    if numeros < 0:
        numeros = 0
    numeros_vetorizado.append(numeros)

print("====exibindo dados====")
for contador, numero in enumerate(numeros_vetorizado):
    print(f"{contador+1}ª numero: {numero}")


