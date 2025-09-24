tot = 0
tot_mais_mil = 0
lower = 9999999999999999999999999999999999999999999999999999.0
lower_nome = 0

while True:
    p_nome = str(input('Digite o nome do produto: '))
    p_preco = float(input('Digite o valor do protudo R$ '))
    tot = tot + p_preco

    if p_preco > 1000:
        tot_mais_mil += 1

    if p_preco < lower:
        lower_nome = p_nome

    c = input('Deseja continuar? (S)im ou (N)ão: ').strip().upper()
    if c == "N":
        break

print(f'O total gasto na compra foi R${tot}')
print(f'{tot_mais_mil} produto(s) custam mais de R$1000.00')
print(f'O produto mais barato chama-se {lower_nome}')