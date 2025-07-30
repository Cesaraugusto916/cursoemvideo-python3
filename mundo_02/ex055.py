"""
EXERCÍCIO 055: Maior e Menor da Sequência

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

qtd = int(input("Quantas pessoas vão informar o peso? "))
pesos = [float(input(f"Digite o peso da {i+1}ª pessoa (kg): ")) for i in range(qtd)]
print(f"O maior peso lido foi: {max(pesos):.1f} kg")
print(f"O menor peso lido foi: {min(pesos):.1f} kg")
