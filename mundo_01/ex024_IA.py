"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto

Aprimoramentos realizados:
- Permite analisar múltiplos nomes de cidades.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    cid = input('Digite o nome de uma cidade (ou "fim" para encerrar): ').strip()
    if cid.lower() == 'fim':
        print('Encerrando programa.')
        break
    if not cid:
        print('Nome vazio!')
        continue
    if cid[:5].upper() == 'SANTO':
        print('Sua cidade começa com a palavra Santo')
    else:
        print('Sua cidade não começa com a palavra Santo')
    print('-'*30)
