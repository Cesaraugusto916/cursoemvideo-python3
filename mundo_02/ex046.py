import time

input('Pressione Enter para iniciar a contagem regressiva...')

print('Contagem regressiva iniciada!')

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print('Kaboom!')
time.sleep(1)
print('Feliz Ano Novo!')
