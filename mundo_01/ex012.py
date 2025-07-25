"""
EXERCÍCIO 012: Calculando Descontos

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

v = float(input('Digite o valor do produto: R$'))
print(f'Com 5% de desconto, o produto será R${v-(v*0.05):.2f}.')
