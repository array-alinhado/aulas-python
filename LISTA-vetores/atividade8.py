# Variáveis para armazenar os números
import os
os.system("cls || clear")

lista_vetores = []

QUANTIDADE_NUMEROS = 5

positivos_pares = 0
quantidade_impares = 0
quantidade_negativos = 0
soma = 0
contador = 0
while True: 
        numero = int(input("Digite o número: "))
        contador += 1
        if numero % 2 == 0 and numero > 0:
            positivos_pares += 1
        else: 
            quantidade_impares += 1
        if numero <0:
            quantidade_negativos += 1




        if numero == 0:
            contador -= 1
            break
     

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {positivos_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Quantidade de numer+os inseridos: {contador}")
