"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 019: Sorteando um Item na Lista

Aprimoramentos realizados:
- Permite sortear entre qualquer quantidade de alunos.
- Validação dos nomes.
- Apresentação mais clara do resultado.
"""

from random import choice
alunos = []
print('Digite os nomes dos alunos. Digite "fim" para encerrar.')
while True:
    nome = input('Nome: ').strip()
    if nome.lower() == 'fim':
        break
    if nome:
        alunos.append(nome)
if alunos:
    sorteado = choice(alunos)
    print(f'O aluno sorteado foi: {sorteado}')
else:
    print('Nenhum aluno foi inserido.')
