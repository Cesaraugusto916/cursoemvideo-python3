"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 031: Custo da Viagem

Aprimoramentos realizados:
- Permite analisar múltiplas viagens.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    entrada = input('Qual foi a distância em Km? (ou "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        print('Encerrando programa.')
        break
    try:
        d = float(entrada)
        if d > 200:
            print(f'Passagem: R${d*0.45:.2f}')
        else:
            print(f'Passagem: R${d*0.50:.2f}')
        print('-'*30)
    except ValueError:
        print('Valor inválido!')
