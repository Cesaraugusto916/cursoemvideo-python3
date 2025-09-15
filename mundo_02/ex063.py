"""
EXERCÍCIO 063: Sequência de Fibonacci v1.0

Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

print('-' * 30)
cont = 1
while cont <= n:
    print(f'{t1}', end=' → ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('-' * 30)
