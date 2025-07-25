"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 028: Jogo da Adivinhação v1.0

Aprimoramentos realizados:
- Permite escolher o intervalo do jogo.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

import random
while True:
    try:
        inicio = int(input('Número mínimo: '))
        fim = int(input('Número máximo: '))
        if inicio >= fim:
            print('O mínimo deve ser menor que o máximo.')
            continue
        break
    except ValueError:
        print('Digite valores inteiros.')
n_pc = random.randint(inicio, fim)
print(f'Pensei em um número entre {inicio} e {fim}!')
while True:
    try:
        n_us = int(input('Qual número eu pensei?: '))
        if n_us == n_pc:
            print(f'Parabéns! Você acertou! Eu pensei exatamente no {n_us}')
            break
        else:
            print(f'Boa tentativa, mas eu pensei no número {n_pc}!')
            break
    except ValueError:
        print('Digite um número inteiro.')
