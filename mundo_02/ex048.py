"""
EXERCÍCIO 048: Soma Ímpares Múltiplos de Três

Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

import time

s = 0

for c in range(1, 501):
    if c % 3 == 0:
        s += c

print(f'A soma de todos os valores de 1 a 500 que são múltiplos de 3 é {s}.')
