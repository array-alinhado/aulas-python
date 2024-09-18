import os
os.system("cls || clear")
import time

lista_valores = list()

for cont in range(0, 5):
    lista_valores.append(int(input("digite um valor: ")))




for c, v in enumerate(lista_valores):
    print(f"na posiçao {c} encontrei o numero {v}!")
    time.sleep(0.72)
print("final da lista!!")
time.sleep(1)