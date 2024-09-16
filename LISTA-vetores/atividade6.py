import os
os.system("cls || clear")


QUANTIDADE_NUMEROS = 4
lista_pares_positivos = []

# Entrada.
print("\n=== Solicitando dados ===")


def Verificando_pares(lista_pares_positivos):
    lista_par = []

    for i in range(QUANTIDADE_NUMEROS):
        while True:
            numero = int(input("Digite um número: "))

        # Verificando se o número é par ou positivo.
            if numero % 2 == 0 and numero > 0:
                lista_par.append(numero)
                break
            else:
                print("Número inválido. \nTente novamente.")
    return lista_par

resulatdo = Verificando_pares(lista_pares_positivos)
# Saída.
print("\n=== Exibindo resultados ===")
for i, cada_numero in enumerate(reversed (resulatdo)):
    print(f"{len(resulatdo)} | {i}º - {cada_numero}")