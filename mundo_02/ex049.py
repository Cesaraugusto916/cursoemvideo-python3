import time
n = int(input('Digite um número para mostrar a tábuada até o 10: '))

for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c}')
    time.sleep(0.5)
print('Fim do programa!')