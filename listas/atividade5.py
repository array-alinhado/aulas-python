import os
os.system("cls || clear")


"""Crie funções que recebam 2 números e retorne a
soma,subtração, divisão e a multiplicação destes dois números informados."""

segundo_numero = int(input("digite seu 1 numero: "))
primeiro_numero = int(input("digite seu 2 numero: "))
def somar(n1, n2):
    soma = n1 + n2 
    return soma


soma = somar(primeiro_numero, segundo_numero)

print(F"soma: {soma}")

def subtrair(n1, n2):
    subtrai = n1 - n2 
    return subtrai

subtrai = subtrair(primeiro_numero, segundo_numero)

print(F"subtrai: {subtrai}")

def dividir(n1, n2):
    divisao = n1 / n2 
    return divisao

divisao = dividir(primeiro_numero, segundo_numero)

print(F"divisao: {divisao}")

def multiplicar(n1, n2):
    multiplicacao = n1 * n2 
    return multiplicacao

multiplicacao = multiplicar(primeiro_numero, segundo_numero)

print(F"multiplicacao: {multiplicacao}")