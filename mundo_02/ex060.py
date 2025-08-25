"""
EXERCÍCIO 060: Cálculo do Fatorial

Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

from time import sleep
n = int(input('Digite um número inteiro: '))
c = n
f = 1

print(f'Calculando {n}!')
sleep(2)
while c > 0:
    print(f'{c}', end = '')
    print(' x ' if c > 1 else ' = ', end = '') 
    f *= c
    c -= 1
print(f'{f}')
sleep(5)