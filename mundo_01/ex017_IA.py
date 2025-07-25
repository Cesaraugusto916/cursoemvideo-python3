"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 017: Catetos e Hipotenusa

Aprimoramentos realizados:
- Validação da entrada dos catetos.
- Mostra todos os lados do triângulo.
- Apresentação mais clara dos resultados.
"""

while True:
    try:
        c1 = float(input('Digite o valor do cateto oposto: '))
        c2 = float(input('Digite o valor do cateto adjacente: '))
        if c1 <= 0 or c2 <= 0:
            print('Os catetos devem ser positivos.')
            continue
        break
    except ValueError:
        print('Valor inválido!')
from math import hypot
hip = hypot(c1, c2)
print(f'\nTriângulo retângulo:')
print(f'- Cateto oposto: {c1:.2f}')
print(f'- Cateto adjacente: {c2:.2f}')
print(f'- Hipotenusa: {hip:.2f}')
