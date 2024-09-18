import os
os.system("cls || clear")


lista_valores = []

for cont in range(0,5):
    lista_valores.append(int(input("digite seu valor: ")))

for c, v in enumerate(lista_valores):
    print(f"A posição foi {c}ª e o valor foi: {v}")

maximo_valor = max(lista_valores)
minimo_valor = min (lista_valores)


print(f"o maximo valor foi: {maximo_valor}")
print(f"o minimo valor foi: {minimo_valor}")