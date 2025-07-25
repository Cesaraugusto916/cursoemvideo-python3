"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 026: Primeira e Última Ocorrência de uma String

Aprimoramentos realizados:
- Permite analisar múltiplas frases.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

while True:
    frase = input('Digite uma frase (ou "fim" para encerrar): ').strip().lower()
    if frase == 'fim':
        print('Encerrando programa.')
        break
    if not frase:
        print('Frase vazia!')
        continue
    print(f'A letra "a" aparece {frase.count("a")} vezes.')
    print(f'A primeira posição do "a": {frase.find("a")+1}')
    print(f'A última posição do "a": {frase.rfind("a")+1}')
    print('-'*30)
