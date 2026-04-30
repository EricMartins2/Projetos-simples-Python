num = int(input('Escolha um número: '))
mult = num
for numero in range(num - 1, 0, -1):
    print('{} x {} = '.format(mult, numero), end='')
    mult = mult * numero
    print('{}'.format(mult))
print('O fatorial de {}! é {}'.format(num, mult))