"""
EXERCÍCIO 008: Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

m = float(input('Insira o valor em metros: '))
print(f'O valor que você digitou é igual a:'
      f'\n{m*100:.0f} centímetros'
      f'\n{m*1000:.0f} milímetros')
