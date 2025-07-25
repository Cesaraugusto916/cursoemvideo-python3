"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 008: Conversor de Medidas

Aprimoramentos realizados:
- Permite converter de metros para várias unidades (cm, mm, km, pol, pés).
- Validação da entrada do usuário.
- Apresentação mais clara dos resultados.
- Comentários explicativos.
"""

# Função para converter metros para outras unidades
def converter_medidas(metros):
    return {
        'Centímetros': metros * 100,
        'Milímetros': metros * 1000,
        'Quilômetros': metros / 1000,
        'Polegadas': metros * 39.3701,
        'Pés': metros * 3.28084
    }

while True:
    try:
        m = float(input('Insira o valor em metros: '))
        if m < 0:
            print('Por favor, insira um valor positivo.')
            continue
        break
    except ValueError:
        print('Valor inválido! Digite um número.')

resultados = converter_medidas(m)
print(f'\nO valor digitado ({m} metros) corresponde a:')
for unidade, valor in resultados.items():
    print(f'- {valor:.4f} {unidade}')
