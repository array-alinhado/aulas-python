import os
os.system("cls || clear")

login = "marta"
senha = 1234
contador = 0
  
while True:
    contador += 1
    login = input("digite seu login: ")
    senha = str(input("digite sua senha: "))
    if login == "marta" and senha == 1234:
         print("acesso permitido!!!")
         break
    if contador >= 3:
        print("acabo!!!")
        break
    else:
        print("acesso negado!!!")

