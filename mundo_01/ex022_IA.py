"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 022: Analisador de Textos

Aprimoramentos realizados:
- Validação do nome.
- Apresentação mais clara dos resultados.
- Permite analisar múltiplos nomes.
"""

while True:
    nome = input('Digite seu nome completo (ou "fim" para encerrar): ').strip()
    if nome.lower() == 'fim':
        print('Encerrando programa.')
        break
    if not nome:
        print('Nome vazio!')
        continue
    print('Todas as letras maiúsculas:', nome.upper())
    print('Todas as letras minúsculas:', nome.lower())
    print('Quantas letras (sem espaços):', len(nome.replace(' ', '')))
    primeiro_nome = nome.split()[0]
    print('Letras do primeiro nome:', len(primeiro_nome))
    print('-'*30)
