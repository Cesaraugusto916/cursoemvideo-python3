"""
EXERCÍCIO 004: Dissecando uma Variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""

t = input('Digite algo: ')
print(f'Você digitou {t}. O tipo primitivo do que você digitou é:', type(t))
print('É somente alfabético?', t.isalpha())
print('É somente numérico?', t.isnumeric())
print('É composto de letras e números?', t.isalnum())
print('Está todo maiúsculo?', t.isupper())
print('Está com a primeira letra maiúscula?', t.istitle())
