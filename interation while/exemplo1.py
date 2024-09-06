import os
os.system("cls || clear")

contador  = 0
continua = 's'

while continua  =='s':
  #comando serem repetidos
  print("REPENTINDO....")

  contador += 1
  
  continua = input("tecle 's' se deseja continuar: ").strip().lower()
contador == 0
if contador == 0:
   print("bloco n")
else:
   print(f"foi repetido {contador}vezes")
  