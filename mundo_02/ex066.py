s = 0
c = 0
while True:
    n = int(input('Digite um número, ou 999 para encerrar: '))
    if n == 999:
        break
    s += n
    c += 1
    

print(f'Você digitou {c} números e a soma deles é {s}.')