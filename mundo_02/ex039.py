"""
EXERCÍCIO 039: Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

ano = int(input('Digite seu ano de nascimento: '))

if (2025 - ano) > 18:
    print(f'Você passou {(2025-ano)-18} ano(s) do tempo de se alistar!')
elif (2025 - ano) == 18:
    print('Você está na idade de se alistar!')
else:
    print(f"Ainda falta {18-(2025-ano)} ano(s) para o seu alistamento!")