"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 030: Par ou Ímpar?

Aprimoramentos realizados:
- Permite analisar múltiplos números.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    entrada = input('Digite um número inteiro (ou "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        print('Encerrando programa.')
        break
    try:
        n = int(entrada)
        if n % 2 == 0:
            print('Seu número é PAR!')
        else:
            print('Seu número é ÍMPAR!')
        print('-'*30)
    except ValueError:
        print('Valor inválido!')
