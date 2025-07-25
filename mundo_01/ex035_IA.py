"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 035: Analisando Triângulo v1.0

Aprimoramentos realizados:
- Permite analisar múltimos conjuntos de retas.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    entrada = input('Digite três valores de retas separados por espaço (ou "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        print('Encerrando programa.')
        break
    try:
        retas = [float(x) for x in entrada.split()]
        if len(retas) != 3:
            print('Digite exatamente três valores.')
            continue
        menor = min(retas)
        maior = max(retas)
        meio = sum(retas) - menor - maior
        if menor + meio > maior:
            print(f'Os segmentos {menor}, {meio} e {maior} podem formar triângulo!')
        else:
            print(f'Os segmentos {menor}, {meio} e {maior} NÃO podem formar triângulo')
        print('-'*30)
    except ValueError:
        print('Valor inválido!')
