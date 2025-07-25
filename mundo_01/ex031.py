"""
EXERCÍCIO 031: Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""

d = float(input('Qual foi a distancia em Km? '))
if d > 200:
    print(f'Passagem: R${d*0.45:.2f}')
else:
    print(f'Passagem: R${d*0.50:.2f}')