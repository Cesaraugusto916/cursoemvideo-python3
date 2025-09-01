"""
EXERCÍCIO 057: Validação de Dados

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

p = input('Insira M para masc e F para fem: ').strip().upper()[0]

while p not in 'MF':
    p = input('Inválido!' \
    '\nInsira M para masc e F para fem: ').strip().upper()[0]
print(f'Gênero [{p}] registrado com sucesso!')