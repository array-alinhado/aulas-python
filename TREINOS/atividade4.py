import os
os.system("cls || clear")


lista_valores = []
lista_valores.sort()

while True:
    numero = int(input("digite seu nuemro: "))

    if numero in lista_valores:
        print("numero duplicado bocó!!!")
    else:
        lista_valores.append(numero)
        print("numero adicionado com secso.")

    while True:
        continuar = input("Quer continuar? [S/N] ").strip().upper()
        if continuar in ['S', 'N']:
            break
        else:
          print("Entrada inválida! Digite 'S' para Sim ou 'N' para Não.")

        if continuar == 'N':
            break

print("Os números cadastrados foram:", lista_valores)
