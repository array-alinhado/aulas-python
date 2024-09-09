import os
os.system("cls || clear")



def calculo_imc(n1, n2):
    resultado = n2 / (n1 * n2)
    return resultado

    
def verificar_classificacao(imc):

    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 24.9:
        return "peso normal"
    elif imc < 34.9:
        return "obsidade grau 1"
    else:
        return "obesidade grau 2"
        
peso = float (input("digite sua altura: "))
altura = float (input("digite seu peso: "))

imc = calculo_imc (peso, altura)
classificacao = verificar_classificacao(imc)


print(f"imc:  {imc}")
print(f"classificao {classificacao}")