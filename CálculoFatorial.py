num = int(input('Escolha um número: '))
num2 = num - 1
mult = num * num2
print('', num, end='')
while num2 != 1:
    print(' x {}'.format(num2), end='')
    num2 -= 1
    mult = mult * num2
    if num2 == 1:
        print(' x {} = {}'.format(num2, mult))


print('O fatorial de {}! é igual a {}'.format(num, mult))
