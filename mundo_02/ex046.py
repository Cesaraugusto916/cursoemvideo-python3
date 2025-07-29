"""
EXERCÍCIO 046: Contagem Regressiva

Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

import time

input('Pressione Enter para iniciar a contagem regressiva...')

print('Contagem regressiva iniciada!')

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)

print('Kaboom!')
time.sleep(1)
print('Feliz Ano Novo!')
