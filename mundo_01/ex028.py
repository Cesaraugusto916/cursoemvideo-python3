"""
EXERCÍCIO 028: Jogo da Adivinhação v1.0

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

import random
n_pc = random.randint(0,5)
print('Olá, usuário. Eu acabei de pensar em um número de 0 a 5!')
n_us = int(input('Qual número eu pensei?: '))
if n_us == n_pc:
    print(f'Parabéns! Você acertou! Eu pensei exatamente no {n_us}')
else:
    print(f'Boa tentativa, mas eu pensei no número {n_pc}!')