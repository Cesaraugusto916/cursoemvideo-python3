"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 007: Média Aritmética

Aprimoramentos realizados:
- Validação das notas (0 a 10).
- Mostra conceito final do aluno.
- Permite calcular média de mais de dois valores.
"""

notas = []
print('Digite as notas do aluno (de 0 a 10). Digite "fim" para encerrar.')
while True:
    entrada = input('Nota: ')
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print('Nota fora do intervalo permitido!')
    except ValueError:
        print('Valor inválido!')
if notas:
    media = sum(notas) / len(notas)
    print(f'Média do aluno: {media:.2f}')
    if media >= 7:
        conceito = 'Aprovado'
    elif media >= 5:
        conceito = 'Recuperação'
    else:
        conceito = 'Reprovado'
    print(f'Conceito: {conceito}')
else:
    print('Nenhuma nota válida foi inserida.')
