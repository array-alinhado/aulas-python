import os
os.system("cls || clear")

tabuada = 0

def tabuada_dos_n(n1, n2):
    tabuada_dos_n = n1 * n2
    return tabuada
    



numero = int(input("digite seu numero para a tabuada: "))

 
for i in range(1,11):
   tabuada = print(f"{numero} x {i} = {numero * i}")
