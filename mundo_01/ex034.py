"""
EXERCÍCIO 034: Aumentos Múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""

s = float(input('Qual o salário do funcionário? R$'))
if s > 1250:
    s_aum = s * 1.1
else:
    s_aum = s * 1.15
print(f'O novo salário, com aumento, será de R${s_aum:.2f}')