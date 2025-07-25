"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 025: Procurando uma String Dentro de Outra

Aprimoramentos realizados:
- Permite analisar múltiplos nomes.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    nome = input('Digite o nome (ou "fim" para encerrar): ').strip()
    if nome.lower() == 'fim':
        print('Encerrando programa.')
        break
    if not nome:
        print('Nome vazio!')
        continue
    if 'SILVA' in nome.upper():
        print('Seu nome contém Silva')
    else:
        print('Seu nome não contém Silva')
    print('-'*30)
