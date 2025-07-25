"""
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

cid = input('Digite o nome de uma cidade: ').strip()

if cid[:5].upper() == 'SANTO':
    print('Sua cidade começa com a palavra Santo')
else:
    print('Sua cidade não começa com a palavra Santo')
