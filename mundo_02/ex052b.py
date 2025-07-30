"""
EXERCÍCIO 052: Números Primos

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

num = int(input("Digite um número: "))

divisores = []
for i in range(1, num + 1):
    if num % i == 0:
        divisores.append(i)

if len(divisores) == 2:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} tem {len(divisores)} divisores.")
    print(f"São eles: {divisores}")
    print("Portanto ele não é primo.")