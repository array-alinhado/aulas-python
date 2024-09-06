import os
os.system("cls || clear")


""""Crie um programa que ajude um usuário a controlar seus gastos mensais. O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido. O programa deve exibir o total gasto e o valor  excedente."""
gasto_total = 0
orcamento = float(input("DIGITE SEU ORÇAMENTO: "))

while True:
     gastos = float(input("digite seu gasto do mês: "))
     if gastos == 0:
        break
     gasto_total += gastos

     if gasto_total > orcamento:
      exedente = gasto_total - orcamento
      print(f"vc gastou R$ {gasto_total:.2f}. excedeu seu orçamento em R${exedente}: ")
     else:
      print(f"voce gastou R${gasto_total:.2f}. valor dentro do seu orcamenta.")
