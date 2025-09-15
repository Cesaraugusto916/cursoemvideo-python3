"""
EXERCÍCIO 062: Super Progressão Aritmética v3.0

Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""

print('Gerador de PA')
print('-=-' * 20)
pp = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = pp
cont = 1
total = 0
mais = 10


while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end = ' -> ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print(f'Progressão finalizada com {total} termos mostrados.')