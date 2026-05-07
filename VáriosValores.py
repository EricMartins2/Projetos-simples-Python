num = int(input('Digite um número inteiro: '))
soma = 0
quant = 0
while num != 999:
    soma += num
    quant += 1
    num = int(input('Digite  inteiro: '))
print('A soma dos números digitados (fora o último) é \033[1;31m{}\033[m'.format(soma))
print('A quantidade de números digitados foi {}'.format(quant))