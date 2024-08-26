import os
os.system("cls || clear")
import time



pares = 0
impares = 0

for i in range (5):
     numero = int(input("digite um numero: "))
    
     if numero  % 2 == 0:
            pares = pares + 1
     else:
            impares = impares + 1

time.sleep(4)

print(f"pares: {pares}")
print(f"impares: {impares}")
