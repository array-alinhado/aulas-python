import os
os.system("cls || clear")


print("""
1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11 - 12.          
 """)


mes = int(input("escolha um numero para o mes desejado: "))

match(mes):
    case 1:
        print("JANEIRO")
        
    case 2:
        print("FEVEIRO")

    case 3:
        print("MARÇO")

    case 4:
        print("ABRIL")

    case 5:
        print("MAIO")

    case 6:
        print("JUNHO")

    case 7:
         print("JULHO")

    case 8:
        print("AGOSTO")

    case 9:
        print("SETEMBRO")
    
    case 10:
         print("OUTUBRO")
    
    case 11:
         print("NOVEMBRO")
    
    case 12:
         print("DEZEMBRO")
        