import os
os.system("cls || clear")
    
def verificar_par_impar():
    pares = 0
    impares = 0


    for i in range(6):
        numero = int(input("digite seu numero: "))

        if numero % 2 == 0: 
            pares += 1
        else:
            impares += 1

    print(f"quantidade pares: {pares}")
    print(f"quantidade impares: {impares}")

verificar_par_impar()

