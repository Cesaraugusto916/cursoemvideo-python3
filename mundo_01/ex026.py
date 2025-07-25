"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String

Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""

frase = input('Digite uma frase: ').strip().lower()

print(f'A letra a aparece {frase.count('a')} vezes.')
print(f'A primeira posiçao do a: {frase.find('a')+1}')
print(f'A última posição do a: {frase.rfind('a')+1}')
