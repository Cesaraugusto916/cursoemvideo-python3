"""
EXERCÍCIO 023: Separando Dígitos de um Número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""

n = int(input('Digite um número de 0 a 9999: '))

uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10

print('Unidades: ', uni)
print('Dezenas: ', dez)
print('Centenas: ', cen)
print('Milhares: ', mil)
