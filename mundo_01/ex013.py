"""
EXERCÍCIO 013: Reajuste Salarial

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

s = float(input('Digite o salário: R$ '))
print(f'O novo salário será de R${s+(s*0.15):.2f}')
