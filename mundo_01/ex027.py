"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

nome = input('Digite seu nome inteiro: ').strip()
pri = nome[:nome.find(' ')]
ult = nome[nome.rfind(' '):]

print(f'Seu primeiro nome é {pri} e seu ultimo nome é{ult}.')
