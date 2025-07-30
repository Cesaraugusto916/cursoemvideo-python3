"""
EXERCÍCIO 056: Analisador Completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

from datetime import datetime
total_idade = 0
maior_idade = 0
nome_homem_mais_velho = ""
mulheres_menores_20 = 0

for i in range(1, 5):
    nome = input(f"Digite o nome da {i}ª pessoa: ").strip()
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    sexo = input(f"Digite o sexo da {i}ª pessoa (M/F): ").strip().upper()

    total_idade += idade

    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            nome_homem_mais_velho = nome
    elif sexo == 'F' and idade < 20:
        mulheres_menores_20 += 1

if total_idade > 0:
    media_idade = total_idade / 4
    print(f"A média de idade do grupo é: {media_idade:.1f} anos")
else:
    print("Nenhuma idade válida foi informada.")

if nome_homem_mais_velho:
    print(f"O homem mais velho é: {nome_homem_mais_velho} com {maior_idade} anos")
else:
    print("Não foi informado nenhum homem.")

print(f"Total de mulheres com menos de 20 anos: {mulheres_menores_20}")
