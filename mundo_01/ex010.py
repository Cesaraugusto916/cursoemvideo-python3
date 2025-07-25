"""
EXERCÍCIO 010: Conversor de Moedas

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.

Considere U$ 1,00 = R$ 3,27
"""

r = float(input('Digite o valor em reais: R$'))
print(f'Com essa quantia, você conseguiria comprar'
      f'\n{r/3.27:.2f} dólares.')