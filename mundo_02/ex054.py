"""
EXERCÍCIO 054: Grupo de Maioridade

Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import datetime
maioridade = 0
menoridade = 0
for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = datetime.now().year - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f"Total de maiores de idade: {maioridade}")
print(f"Total de menores de idade: {menoridade}")
