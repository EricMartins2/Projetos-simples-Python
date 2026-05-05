print('=#' * 20)
print('''

{:^20}

'''.format('SEQUÊNCIA DE FIBONACCI'))
print('=#' * 20)
quantidade = int(input('Quantos números deseja ver? '))
contador = 1
n = 0
n2 = 1
while contador <= quantidade:
    print('{} -> {} -> '.format(n, n2), end='')
    if n == 0:
        n += n2
        n2 += n
    else:
        n += n2
        n2 += n
    contador += 1
print('FIM')