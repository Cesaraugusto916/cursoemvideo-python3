"""
EXERCÍCIO 067: Tabuada v3.0

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

n = 0
while True:
    n = int(input('Digite um número para ver sua tabuáda ou um número negativo para encerrar: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} X {c} = {c*n} ")
print('Programa encerrado. Volte sempre!')
