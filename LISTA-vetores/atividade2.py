import os
os.system("cls || clear")
QUANTIDADE_NOTAS = 3
vetor_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("digite sua nota: "))
    vetor_notas.append(nota)

soma = sum(vetor_notas)
media = soma / QUANTIDADE_NOTAS

# saida 
for contador, nota in enumerate(vetor_notas):
    
    print(f"{contador+1}ª nota: {nota}")
print(f"media: {media}")
    