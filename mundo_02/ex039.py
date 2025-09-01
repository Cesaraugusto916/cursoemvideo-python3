"""
EXERCÍCIO 039: Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import datetime

ano_atual = datetime.now().year
ano = int(input('Digite seu ano de nascimento: '))

if (ano_atual - ano) > 18:
    print(f'Você passou {(ano_atual-ano)-18} ano(s) do tempo de se alistar!')
elif (ano_atual - ano) == 18:
    print('Você está na idade de se alistar!')
else:
    print(f"Ainda falta {18-(ano_atual-ano)} ano(s) para o seu alistamento!")