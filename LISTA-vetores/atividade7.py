# Variáveis para armazenar os números
import os
os.system("cls || clear")

lista_vetores = []

QUANTIDADE_NUMEROS = 5

quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
soma = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1} número: "))
     
    if numero % 2 == 0:
        quantidade_pares += 1
    else: 
        quantidade_impares += 1
       
    if numero <0:
        quantidade_negativos += 1
    else:
        quantidade_positivos += 1
     
    lista_vetores.append(numero)




# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
