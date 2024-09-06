import os
os.system("cls || clear")

tentativas = 3
contador = 0
desconto = 0

while True:
    desconto = input("Digite o codigo de desconto: ")

    if desconto == "PROMO2024":
        print("Desconto Aplicado")
    else:
        input("tente novamente")
    contador += 1
    if contador == tentativas:
        break    
