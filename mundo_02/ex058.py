"""
EXERCÍCIO 058: Jogo da Adivinhação v2.0

Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""

import random

c = 1
n_pc = random.randint(0,10)
print('Olá, usuário. Eu acabei de pensar em um número de 0 a 10!')

acertou = False
palpites = 0

while not acertou:
    n_us = int(input('Qual número eu pensei?: '))
    palpites += 1
    if n_us == n_pc:
        acertou = True
    else:
        if n_us > n_pc:
            print('Menos')
        else:
            print('Mais')
print(f'Você acertou com {palpites} tentativas!')
