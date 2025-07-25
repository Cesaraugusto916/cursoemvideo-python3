"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa

Aprimoramentos realizados:
- Permite analisar múltiplos nomes completos.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    nome = input('Digite seu nome completo (ou "fim" para encerrar): ').strip()
    if nome.lower() == 'fim':
        print('Encerrando programa.')
        break
    partes = nome.split()
    if len(partes) < 2:
        print('Digite pelo menos nome e sobrenome.')
        continue
    print(f'Primeiro nome: {partes[0]}')
    print(f'Último nome: {partes[-1]}')
    print('-'*30)
