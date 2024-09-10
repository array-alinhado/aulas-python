import os
os.system("cls || clear")
lista_notas = []

#estradadas

#vetor_notas = [2, 5, 10]

# saida
# for i in range(?):
#============================
#for nota in notas:
#   print(nota)
# ===========================
# por indice
# print(notas[0])

for i in range(2):
    nota = float(input("digite sua nota: "))
    lista_notas.append(nota)

# saida 
for nota in lista_notas:
    print(f"nota: {nota}")