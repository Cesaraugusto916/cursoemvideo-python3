"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 029: Radar Eletrônico

Aprimoramentos realizados:
- Permite analisar múltiplas velocidades.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    entrada = input('Digite a velocidade do carro em Km/h (ou "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        print('Encerrando programa.')
        break
    try:
        v = int(entrada)
        if v <= 80:
            print('Que bom, o carro não foi multado')
        else:
            print(f'Que pena. O carro foi multado. Ele passou {v-80} Km/h acima da velocidade permitida')
            print(f'Sua multa será de R${(v-80)*7:.2f}')
        print('-'*30)
    except ValueError:
        print('Valor inválido!')
