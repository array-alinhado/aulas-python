import os
os.system("cls || clear")

idade = int(input("digite sua idade: "))

if idade <= 18 or  idade >= 65:
    print("nao pode votar!!!")
else:
    print("pode votar!!!")