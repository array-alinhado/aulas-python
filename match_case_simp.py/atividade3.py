import os
os.system("cls || clear")


print("""
1 - domingo-feira
2 - segunda-feira
3 - terça-feira
4 - quarta-feira
5 - quinta-feira
6 - sexta-feira
7 - sabado-feira    
 """)


dia = int(input("digite seu dia da semana: "))

match(dia):
    case 1:
        print("domingo")
        print("final de semana!!!") 
    case 2:
        print("segunda-feira")
        print("dia util.")
    case 3:
        print("terça-feira")
        print("dia util.")
    case 4:
        print("quarta-feira")
        print("dia util.")    
    case 5:
        print("quinta-feira")
        print("dia util.")
    case 6:
        print("sexta-feira")
        print("dia util.")
    case 7:
        print("sabado.")
        print("final de semana")
    case _:
        pass
    
        