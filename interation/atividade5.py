import os
os.system("cls || clear")

soma = 0
QUANTIDADE_NOTAS = 2

for i in range (QUANTIDADE_NOTAS):
    nota = float(input("digite sua nota: "))
    soma = soma + nota
media = soma / QUANTIDADE_NOTAS   


if  (media >= 7): 
  print("aprovador")
else:
    if media < 4:
        print("reporvado!!!")
    else:
        print("recuperação!!!")