"""
EXERCÍCIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""

nome = str(input("Digite seu nome: ")).strip()

print("Todas as letras maúsculas: ", nome.upper())
print('Todas as letras minúsculas: ', nome.lower())
print('Quantas letras: ', len(nome.replace(" ","")))
primeironome = nome[:nome.find(' ')]
print('Letras do primeiro nome: ', len(primeironome))

