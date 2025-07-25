"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 023: Separando Dígitos de um Número

Aprimoramentos realizados:
- Validação do número (0 a 9999).
- Permite analisar múltiplos números.
- Apresentação mais clara dos resultados.
"""

while True:
    entrada = input('Digite um número de 0 a 9999 (ou "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        print('Encerrando programa.')
        break
    try:
        n = int(entrada)
        if 0 <= n <= 9999:
            uni = n // 1 % 10
            dez = n // 10 % 10
            cen = n // 100 % 10
            mil = n // 1000 % 10
            print(f'Unidade: {uni}')
            print(f'Dezena: {dez}')
            print(f'Centena: {cen}')
            print(f'Milhar: {mil}')
            print('-'*30)
        else:
            print('Número fora do intervalo permitido!')
    except ValueError:
        print('Valor inválido!')
