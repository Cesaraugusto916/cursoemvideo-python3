"""
EXERCÍCIO 053: Detector de Palíndromo

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

frase = input("Digite uma frase: ").replace(" ", "").lower()
palindromo = frase == frase[::-1]
if palindromo:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")

