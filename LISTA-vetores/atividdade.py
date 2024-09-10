import os
os.system("cls || clear")

vetor_notas = []

for i in range(3):
    nota = float(input("digite sua nota: "))
    vetor_notas.append(nota)

# saida 
for i, nota in enumerate(vetor_notas):
    print(f"{i+1}ª nota: {nota}")