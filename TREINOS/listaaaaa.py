import os
os.system("cls || clear")


#lista_lanches = ["pizza", "bolo", "pastel", "maria_mole"]
lista_lanches = [9, 6, 5, 7, 4]
#===========================================================
#lista_lanches.sort() serve para ordenar.
#lista_lanches.sort(reverse = True) serve para reverter.

#===========================================================
#lista_lanches[1] = "passarinho"
#lista_lanches.append("rosca") serve parar acrescentar algo.
#lista_lanches.insert(0, "guaripa")

#===========================================================
#lista_lanches.pop() para apagar algo da lista.
#del lista_lanches[0] tambem.

#============================================================
for contador, lanches in enumerate(lista_lanches):
    print(f"{contador+1}ª {lanches}")

print(f"essa lista tem {len(lista_lanches)} elementos.")