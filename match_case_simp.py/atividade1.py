import os
os.system("cls || clear")


resultado = 0

primeiro_numero = int(input("digite seu numero1: "))
segundo_numero = int(input("digite seu numero2: "))
opcao = input("digiye uma opcao (+ - * / ): ")

match(opcao):
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("opcao invalida")
    
print(f"resultado: {resultado}")

print("fim")
