"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 020: Sorteando uma Ordem na Lista

Aprimoramentos realizados:
- Permite sortear a ordem de qualquer quantidade de alunos.
- Validação dos nomes.
- Apresentação mais clara da ordem sorteada.
"""

from random import shuffle
alunos = []
print('Digite os nomes dos alunos. Digite "fim" para encerrar.')
while True:
    nome = input('Nome: ').strip()
    if nome.lower() == 'fim':
        break
    if nome:
        alunos.append(nome)
if alunos:
    shuffle(alunos)
    print('Ordem de apresentação sorteada:')
    for i, nome in enumerate(alunos, 1):
        print(f'{i}º: {nome}')
else:
    print('Nenhum aluno foi inserido.')
