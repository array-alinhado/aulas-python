import os
os.system("cls || clear")
QUANTIDADE_NOTAS = 5
lista_numero = []

for i in range(QUANTIDADE_NOTAS):
    numeros = int(input("digite sua nota: "))
    lista_numero.append(numeros)


# saida 
maior_numero = max(lista_numero)
menor_numero = min(lista_numero)

for contador, nota in enumerate(lista_numero):
    
    print(f"{contador+1}ª nota: {nota}")


print(f"\nMAIOR numero: {maior_numero}")
print(f"\nmenor numero: {menor_numero}")