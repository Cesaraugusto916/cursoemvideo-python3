p = input('Insira M para masc e F para fem: ').strip().upper()[0]

while p not in 'MF':
    p = input('Inválido!' \
    '\nInsira M para masc e F para fem: ').strip().upper()[0]
print(f'Gênero [{p}] registrado com sucesso!')