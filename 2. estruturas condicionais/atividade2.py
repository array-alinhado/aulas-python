numero1 = ("digite seu primeiro numero: ")
numero2 = ("digite seu primeiro numero: ")


soma = numero1 + numero2
produto = numero1 * numero2
media = soma /2


if (numero1 > numero2):
    maior = numero1
    menor = numero2
else: 
    maior = numero2
    menor = numero1

    #exibindo dados.
print("\nesxibindo dados: ")
print(f"soma: {soma}")
print(f"media: {media}")
print(f"produto: {produto}")
print(f"maior: {maior}")
print(f"menor: {menor}")