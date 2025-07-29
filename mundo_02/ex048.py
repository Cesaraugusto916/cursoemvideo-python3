"""
EXERCÍCIO 048: Soma Ímpares Múltiplos de Três

Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

s = 0

for c in range(1, 501, 2):  # Começa em 1, incrementa de 2 para pegar apenas ímpares
    if c % 3 == 0:
        s += c

print(f'A soma de todos os valores de 1 a 500 que são múltiplos de 3 e ímpares é {s}.')
