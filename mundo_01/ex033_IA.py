"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 033: Maior e Menor Valores

Aprimoramentos realizados:
- Permite analisar múltiplos conjuntos de números.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    entrada = input('Digite três números inteiros separados por espaço (ou "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        print('Encerrando programa.')
        break
    try:
        nums = [int(x) for x in entrada.split()]
        if len(nums) != 3:
            print('Digite exatamente três números.')
            continue
        menor = min(nums)
        maior = max(nums)
        meio = sum(nums) - menor - maior
        print(f'Ordem crescente: {menor}, {meio}, {maior}')
        print('-'*30)
    except ValueError:
        print('Valor inválido!')
