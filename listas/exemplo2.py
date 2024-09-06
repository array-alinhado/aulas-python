import os
os.system("cls || clear")

#função com retorno.

def somar(n1, n2):
    soma =n1 + n2 
    return soma

primeiro_numero = int(input("digite seu numero: "))
segundo_numero = int(input("digite seu 2 numero: "))

soma = somar(primeiro_numero, segundo_numero)

print(F"soma: {soma}")