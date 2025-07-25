"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 009: Tabuada

Aprimoramentos realizados:
- Permite escolher o intervalo da tabuada.
- Validação da entrada.
- Apresentação mais clara e interativa.
"""

while True:
    try:
        n = int(input('Digite um número para ver a tabuada: '))
        break
    except ValueError:
        print('Valor inválido! Digite um número inteiro.')
while True:
    try:
        inicio = int(input('Tabuada começa em: '))
        fim = int(input('Tabuada termina em: '))
        if inicio > fim:
            print('O início deve ser menor ou igual ao fim.')
            continue
        break
    except ValueError:
        print('Digite valores inteiros.')
print(f'\nTabuada de {n} de {inicio} até {fim}:')
for i in range(inicio, fim+1):
    print(f'{n} x {i} = {n*i}')
