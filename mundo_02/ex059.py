"""
EXERCÍCIO 059: Criando um Menu de Opções

Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:

[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep
n1 = int(input('Insira um valor inteiro: '))
n2 = int(input('Insira outro valor inteiro: '))
op = 0

while op != 5:
    print("""Selecione uma opção:
    [ 1 ] para somar
    [ 2 ] para multiplicar
    [ 3 ] para mostrar o maior
    [ 4 ] para selecionar novos números
    [ 5 ] para sair do programa""")
    op = int(input('>>>>> Qual a sua opção? '))
    if op == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, {n1} é o maior número.')
        else:
            print(f"Entre {n1} e {n2}, {n2} é o maior número.")
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Insira um valor inteiro: '))
        n2 = int(input('Insira outro valor inteiro: '))
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 15)
    sleep(2)


print('Fim do programa')