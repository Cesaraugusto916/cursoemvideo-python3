"""
EXERCÍCIO 017: Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

from math import hypot
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(c1, c2)
print(f'A hipotenusa desse triangulo retangulo é {hip:.2f}')