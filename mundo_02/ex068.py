import random
import time

r = 0
user_choice = 0
user_number = 0
pc_number = random.randint(0, 10)
wins = 0

while True:
    print('Vamos jogar par ou ímpar?')
    user_choice = int(input('Escolha (1) para ÍMPAR e (2) para PAR: '))
    time.sleep(1)
    if user_choice == 1:
        print("Você selecionou ÍMPAR. Então eu serei PAR.")
    elif user_choice == 2:
        print("Você selecionou PAR. Então eu serei ÍMPAR.")
    else:
        print("Opção inválida! O jogo será encerrado.")
        exit()

    time.sleep(1)
    pc_number = random.randint(0, 10)
    print('Eu já escolhi meu número...')
    time.sleep(1)
    user_number = int(input("Agora, insira o seu número: "))

    time.sleep(1)

    soma = pc_number + user_number
    print(f'\nEu escolhi {pc_number} e você escolheu {user_number}.\nA soma deu {soma}.')

    time.sleep(2)

    if soma % 2 == 1:  # Se for ímpar
        r = 1
    else:  # Se for par
        r = 2

    if r == user_choice:
        print('Parabéns! Você GANHOU!')
        wins += 1
    else:
        break
print('Que pena! Você PERDEU...')
print(f'Você ganhou {wins} vezes.')

