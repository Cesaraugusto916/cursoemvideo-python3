"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 004: Dissecando uma Variável

Aprimoramentos realizados:
- Aceita múltiplos inputs em sequência.
- Mostra mais informações sobre o tipo e propriedades do valor.
- Apresentação mais clara dos resultados.
"""

while True:
    valor = input('Digite algo (ou "sair" para encerrar): ')
    if valor.lower() == 'sair':
        print('Encerrando programa.')
        break
    print(f'\nVocê digitou: {valor}')
    print('Tipo primitivo:', type(valor))
    print('Só tem espaços?', valor.isspace())
    print('É numérico?', valor.isnumeric())
    print('É alfabético?', valor.isalpha())
    print('É alfanumérico?', valor.isalnum())
    print('Está em maiúsculas?', valor.isupper())
    print('Está em minúsculas?', valor.islower())
    print('Está capitalizado?', valor.istitle())
    print('-'*30)
