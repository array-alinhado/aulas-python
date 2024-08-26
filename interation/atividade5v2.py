import os
os.system("cls || clear")

soma = 0
media = 0

for i in range (3):
    nota = float(input("digite sua nota: "))
    soma = soma + nota
media = media + soma /3   


if  (media >= 7): 
  print("aprovador")
elif nota < 4:
        print("reporvado!!!")
else:
        print("recuperação!!!")