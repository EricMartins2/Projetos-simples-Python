num = int(input('Escolha um número: '))
num2 = num - 1
mult = num * num2
while num2 != 1:
    num2 -= 1
    mult = mult * num2


print('O fatorial de {}! é igual a {}'.format(num, mult))
