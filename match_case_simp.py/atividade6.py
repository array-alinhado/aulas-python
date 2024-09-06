import os
os.system("cls || clear")

altura = float(input("digite sua altura: "))

sexo = input("digite seu sexo(m ou f): ").upper()#.lower


match sexo:
    case "M":
        peso_ideal = (72.7 * altura) - 58
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
    case _:
        print("opcao invalida")

print(f"peso ideal,: {peso_ideal: .2f}")