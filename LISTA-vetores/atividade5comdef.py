import os
os.system("cls || clear")
QUANTIDADE_NUMEROS = 5
lista_numeros = []

def verificando_numeros(lista_numeros):
    lista_atualizada = []

    for numero in lista_numeros:
        if numero < 0:
            numero = 0
        lista_atualizada.append(numero)
    return lista_atualizada

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"digite o {i+1}ª numero: "))
    lista_numeros.append(numero)

resultado = verificando_numeros(lista_numeros)


for cada_numero in resultado:
    print(cada_numero)

