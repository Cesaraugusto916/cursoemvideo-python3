n = 0
while True:
    n = int(input('Digite um número para ver sua tabuáda ou um número negativo para encerrar: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{c} X {n} = {c*n} ")
print('Programa encerrado. Volte sempre!')
