import os
os.system("cls || clear")


while True: 
    nota = float(input("digite sua nota: "))

    if nota < 0 or nota > 10:
          print("a nota deve ser maior q 0 e menor q 10.")

    else: 
         break #para o laço de repet.
    

print(f"nota: {nota}")