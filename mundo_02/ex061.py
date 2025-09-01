"""
EXERCÍCIO 061: Progressão Aritmética v2.0

Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""

print('Gerador de PA')
print('-=-' * 15)
pp = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = pp
cont = 1

while cont <= 10:
    print(f'{termo}', end = ' -> ')
    termo += r
    cont += 1
print('FIM')