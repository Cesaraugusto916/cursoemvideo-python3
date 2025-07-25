"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 018: Seno, Cosseno e Tangente

Aprimoramentos realizados:
- Validação da entrada do ângulo.
- Permite calcular para múltiplos ângulos.
- Apresentação mais clara dos resultados.
"""

import math
print('Digite os ângulos desejados (em graus). Digite "fim" para encerrar.')
while True:
    entrada = input('Ângulo: ')
    if entrada.lower() == 'fim':
        print('Encerrando programa.')
        break
    try:
        ang = float(entrada)
        angr = math.radians(ang)
        sen = math.sin(angr)
        cos = math.cos(angr)
        tan = math.tan(angr)
        print(f'\nPara o ângulo {ang}°:')
        print(f'- Seno: {sen:.4f}')
        print(f'- Cosseno: {cos:.4f}')
        print(f'- Tangente: {tan:.4f}')
        print('-'*30)
    except ValueError:
        print('Valor inválido!')
