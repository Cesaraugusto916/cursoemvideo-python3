"""
EXERCÍCIO 035: Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de outra reta: '))
r3 = float(input('Digite o valor da última reta: '))

if (r1 <= r2) and (r1 <= r3):
    menor = r1
elif (r2 <= r1) and (r2 <= r3):
    menor = r2
else:
    menor = r3

if (r1 >= r2) and (r1 >= r3):
    maior = r1
elif (r2 >= r1) and (r2 >= r3):
    maior = r2
else:
    maior = r3

meio = (r1 + r2 + r3) - maior - menor

if menor + meio > maior:
    print(f'Os seguimentos {menor}, {meio} e {maior} podem formar triangulo!')
else:
    print(f'Os seguimentos {menor:}, {meio:} e {maior} NÃO podem formar triangulo')