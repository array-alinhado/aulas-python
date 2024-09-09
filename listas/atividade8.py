import os
os.system("cls || clear")
def inflacionar(preco_produto):
    if preco_produto < 100:
        return preco_produto * 1.1
    else:
        return preco_produto * 1.2

preco_produto = float(input("digite seu preço: "))

preco_inflacionado = inflacionar(preco_produto)

print("fimmmmmmmmm")
print(f"preço inflacionado: {preco_inflacionado: .2f}")