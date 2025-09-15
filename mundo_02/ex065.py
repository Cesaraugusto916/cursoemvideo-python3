"""
EXERCÍCIO 065: Maior e Menor Valores

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

s = c = maior = menor = 0

resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número inteiro: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = s / c
print(f'Você digitou {c} números e a média entre eles foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')  
print('Fim do programa!')
