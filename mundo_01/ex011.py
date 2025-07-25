"""
EXERCÍCIO 011: Pintando Parede

Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
print(f'A área dessa parede é igual a {a*l}m2.'
      f'\nPara pintar essa parede, você precisará'
      f'\nde {(a*l)/2} litros de tinta.')
