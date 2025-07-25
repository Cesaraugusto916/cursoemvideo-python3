"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 034: Aumentos Múltiplos

Aprimoramentos realizados:
- Permite analisar múltiplos salários.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    entrada = input('Qual o salário do funcionário? R$ (ou "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        print('Encerrando programa.')
        break
    try:
        s = float(entrada)
        if s > 1250:
            s_aum = s * 1.1
        else:
            s_aum = s * 1.15
        print(f'O novo salário, com aumento, será de R${s_aum:.2f}')
        print('-'*30)
    except ValueError:
        print('Valor inválido!')
