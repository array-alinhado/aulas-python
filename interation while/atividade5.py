import os
os.system("cls || clear")

soma = 0
for i in range(3):
        
    while True:
        nota = float(input("digite sua nota: "))
        # nota2 = float(input("digite sua nota2: "))
        # nota3 = float(input("digite sua nota3: "))

        # soma = soma + nota1 + nota2 + nota3

        if nota < 0 or nota > 10:
            print("\na nota deve ser maoir ou igual 0 e maior q 10.")
        # elif nota1 < 0 or nota2 > 10:
        #     print("\na nota deve ser maoir ou igual 0 e maior q 10.")
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