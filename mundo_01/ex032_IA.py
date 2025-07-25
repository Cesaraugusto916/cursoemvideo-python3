"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 032: Ano Bissexto

Aprimoramentos realizados:
- Permite analisar múltiplos anos.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    entrada = input('Digite um ano qualquer (ou "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        print('Encerrando programa.')
        break
    try:
        ano = int(entrada)
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f'O ano {ano} é BISSEXTO.')
        else:
            print(f'O ano {ano} não é BISSEXTO.')
        print('-'*30)
    except ValueError:
        print('Valor inválido!')
