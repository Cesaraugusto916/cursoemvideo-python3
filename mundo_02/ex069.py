count = 0
mais_dezoito = 0
masc = 0
fem_vinte_menos = 0

while True:
    idade = int(input('Insira a idade: '))
    if idade > 18:
        mais_dezoito += 1
    sexo = str(input('Insira M para masc ou F para fem: ')).strip().upper()
    if sexo == "M":
        masc += 1
    else:
        if idade < 20:
            fem_vinte_menos += 1
    count += 1
    d = input('Deseja continuar? (S)im ou (N)ão?: ').strip().upper()
    if d == "N":
        break

print(f'{mais_dezoito} pessoas tem mais de 18 anos.')
print(f'{masc} homens foram cadastrados.')
print(f'{fem_vinte_menos} mulheres tem menos de 20 anos.')