"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 014: Conversor de Temperaturas

Aprimoramentos realizados:
- Permite converter entre Celsius, Fahrenheit e Kelvin.
- Validação da entrada.
- Apresentação mais clara dos resultados.
"""

def converter_temperatura(valor, escala):
    if escala == 'C':
        return {
            'Celsius': valor,
            'Fahrenheit': valor * 9/5 + 32,
            'Kelvin': valor + 273.15
        }
    elif escala == 'F':
        c = (valor - 32) * 5/9
        return {
            'Celsius': c,
            'Fahrenheit': valor,
            'Kelvin': c + 273.15
        }
    elif escala == 'K':
        c = valor - 273.15
        return {
            'Celsius': c,
            'Fahrenheit': c * 9/5 + 32,
            'Kelvin': valor
        }
    else:
        return None

while True:
    escala = input('Digite a escala de origem (C/F/K): ').upper()
    if escala in ['C', 'F', 'K']:
        break
    print('Escala inválida!')
while True:
    try:
        valor = float(input(f'Digite o valor da temperatura em {escala}: '))
        break
    except ValueError:
        print('Valor inválido!')
res = converter_temperatura(valor, escala)
print('\nTemperaturas convertidas:')
for k, v in res.items():
    print(f'- {v:.2f} {k}')
