valor = int(input('Insira o valor a ser sacado: '))

nota_cinquenta = valor // 50
resto_cinquenta = valor % 50
nota_vinte = resto_cinquenta // 20
resto_vinte = resto_cinquenta % 20
nota_dez = resto_vinte // 10
resto_dez = resto_vinte % 10
nota_um = resto_dez

print(f'Seu saque sera de {nota_cinquenta} notas de cinquenta,')
print(f'{nota_vinte} notas de vinte, {nota_dez} notas de dez e')
print(f'{nota_um} notas de um.')

