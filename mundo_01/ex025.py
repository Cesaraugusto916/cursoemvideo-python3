"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = input('Digite o nome: ')

if 'SILVA' in nome.upper():
    print('Seu nome contém Silva');
else:
    print('Seu nome não contém silva')