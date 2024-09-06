import os
os.system("cls || clear")


primeiro_numero = int(input("Digite o numero: "))

def verificar_par_impar(primeiro_numero):
    if primeiro_numero % 2 == 0:
        print(f"O numero {primeiro_numero} é par")
    else:
        print(f"O nuumero {primeiro_numero} é impar")

resposta = verificar_par_impar(primeiro_numero)        
