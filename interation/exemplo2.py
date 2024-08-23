import os
os.system("cls || clear")


# solicitando dados.
numero = int(input("Digite um número da tabuada: "))

print(f"\ntabuada selcionada: {numero}")
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")