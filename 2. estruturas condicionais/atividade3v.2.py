import os
os.system("cls || clear")

login = input("digite seu nome: ")
senha = float (input("digite sua senha: "))

login_correto = login == "carlos"
senha_correto = senha == "6969"


if login != "itau" and senha != 6969:
    print("login ou senha incorreta!!!")
else:
    print("bem-vindo!!!")
