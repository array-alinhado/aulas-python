import os
os.system("cls || clear")

print("""
1 - cadastre usuario
2 - excluir
3 - sair     
  """)


opcao = int(input("digite sua opção: "))

match(opcao):
    case 1:
        print("opção de cadastro.")
    case 2:
        print("opção de excluir.")
    case 3:
        print("opção de sair.")
    case _:
        print("opção invalida.")
        
        print("FIM.")

