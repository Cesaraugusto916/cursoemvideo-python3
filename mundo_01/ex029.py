"""
EXERCÍCIO 029: Radar Eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""

v = int(input('Digite a velocidade do carro em Km/h: '))
if v <= 80:
    print('Que bom, o carro não foi multado')
else:
    print(f'Que pena. O carro foi multado. Ele passou {v-80} Km/h acima da velocidade permitida')
    print(f'Sua multa será de R${(v-80)*7:.2f}')