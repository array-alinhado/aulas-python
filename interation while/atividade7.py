import os
os.system("cls || clear")

r = "S"
soma = 0 
contador = 0

for i in range(3):
     while r == "S":
      print("""
          
            """)
      
      opcao = int(input("digite sua opção: "))

        match(opcao):
                case 1:
                    print("inserir mais uma nota")
                case 2:
                    print("ver quantas foram informadas")
                case 3:
                    print("calcular a media.")
                case _:
                    print("opção invalida.")
                    
                    print("FIM.")

                nota = float(input("digite sua nota: "))
      
                contador += 1
                        
                r = (input("quer colocar mais uma nota? [S/N]")).upper()
                if nota < 0 or nota > 10:
                    print("\na nota deve ser maoir ou igual 0 e maior q 10.")            
                else:
                   soma = soma + nota
                    break

                        media = soma /3

                        if media >= 7:
                            print("aprovado")
                            
                        elif media < 5: 
                            print("reprovado!!!")
                            
                        else: 
                            print("recuperação") 


                        print(f"nota: {media}")

