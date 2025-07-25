"""
EXERCÍCIO 036: Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
t = int(input('Em quantos anos você irá pagar? '))
prest = casa / (t * 12)

print(f'Sua prestação será de R${prest:.2f}')

if prest > (sal * 0.3):
    print('Seu empréstimo foi NEGADO.')
else:
    print('Seu empréstimo foi APROVADO!')



