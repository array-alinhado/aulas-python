import os
os.system("cls || clear")

"""faça um tabela com os produtos do mercado e subtraia o valor total do cliente."""



def subtrair(valor, preco):
   subtracao = valor - preco
   return subtracao

valor = int(input("digite seu valor pra gastar no mercado: "))

print("""
      
1 - batata
2 - couve-flor
3 - banana
4 - bife
5 - camelo
""")
preco = int(input("faça sua escolha: "))

subtracao = subtrair(valor, preco)


match(preco):
    case 1:
       preco = 5.78
       print("batata = R$ 5,78")
    case 2:
       preco = 4.70
       print("couve-flor = R$ 4,70 ")
    case 3:
       preco = 8.60
       print("banana = R$ 8,60")
    case 4:
       preco = 14.70
       print("bife = R$ 14,70")
    case 5:
       preco = 244.70
       print("camelo = R$ 244,70")
    case _:
       print("invalido!!!")

       print("FIM")

if valor < preco:
   print("n tem dinherio suficiente!!!")
   exit()


if valor > 0:
    saldo_restante = subtrair(valor, preco)
    print(f"Você ainda tem R$ {saldo_restante:.2f} restantes.")

print("""
1 - PIX
2 - DINHERO
3 - CARTÃO DE CREDITO
4 - BOLETO
""")

forma_de_pagamento = int(input("digite sua forma de pagamento: "))

match(forma_de_pagamento):
    case 1:
        print("Você escolheu PIX.")
    case 2:
        print("Você escolheu pagar em Dinheiro.")
    case 3:
        print("Você escolheu Cartão de Crédito.")
    case 4:
        print("Você escolheu Boleto.")
    case _:
        print("Forma de pagamento inválida.")
        exit()