"""
EXERCÍCIO 051: Progressão Aritmética

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

pp = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
for c in range(10):
    print(f'{pp:.0f}', end=' -> ')
    pp += r
print('FIM')
