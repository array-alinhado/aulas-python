v

# solicitando dados.
nome = input ("digite seu nome: ")
idade = int(input ("digite sua idade: "))
nota1 = float(input("digite sua nota: "))
nota2 = float(input("digite sua nota: "))
nota3 = float(input("digite sua nota: "))
media = (nota1 + nota2 + nota3) /3

# exibindo.
if media >=7:
    resultado = ("reprovado!!!")
else:
    resultado = ("apravado!!!")


print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"nota1: {nota1}")
print(f"nota2: {nota2}")
print(f"nota3: {nota3}")
print(f"resultado: {resultado}")