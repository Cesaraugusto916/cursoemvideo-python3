"""
EXERCÍCIO 020: Sorteando uma Ordem na Lista

O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle
n1=input('Digite o nome do primeiro aluno: ')
n2=input('Digito o nome do segundo aluno: ')
n3=input('Digite o nome do terceiro aluno: ')
n4=input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será: {lista}.')
