"""
EXERCÍCIO 052: Números Primos

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

n = int(input('Digite um número inteiro: '))
if n < 2:
    print(f'{n} não é um número primo.')
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{n} é um número primo.')
    else:
        print(f'{n} não é um número primo.')
