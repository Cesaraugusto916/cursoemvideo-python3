import random

c = 1
n_pc = random.randint(0,5)
print('Olá, usuário. Eu acabei de pensar em um número de 0 a 5!')
n_us = int(input('Qual número eu pensei?: '))

while n_us != n_pc:
    print('Tente novamente!')
    n_us = int(input('Qual número eu pensei?: '))
    c += 1
else:
    print(f'Parabéns! Você acertou! Eu pensei exatamente no {n_us}')
    print(f'Você precisou de {c} tentativas!')