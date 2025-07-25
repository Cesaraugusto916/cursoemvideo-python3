"""
EXERCÍCIO 042: Analisando Triângulos v2.0

Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
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

if menor == meio and meio == maior:
    print('Seu triângulo será EQUILÁTERO!')
elif menor == meio or menor == maior or meio == maior:
    print('Seu triângulo será ISÓCELER!')
else:
    print('Seu triângulo será ESCALENO!')