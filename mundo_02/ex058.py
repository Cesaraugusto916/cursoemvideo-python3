"""
EXERCÍCIO 058: Jogo da Adivinhação v2.0

Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""

from random import randint
n_pc = randint(0, 10)
print('Olá, usuário. Eu acabei de pensar em um número de 0 a 10!')
n_us = int(input('Qual número eu pensei?: '))
tent = 1

while n_us != n_pc:
    tent += 1
    if n_us > n_pc:
        print('Menos...')
    else:
        print('Mais...')
    n_us = int(input('Tente novamente: '))
print(f'Parabéns! Eu estava pensando no {n_pc}.\nVocê demorou {tent} tentativas.')