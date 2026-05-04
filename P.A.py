n1 = int(input('Primeiro termo: '))
razao = int(input('Qual a razão: '))
n10 = n1 + (razao * 10)
posicao = 0
while n1 != n10:
    posicao += 1
    print('{}° Termo -> {}'.format(posicao, n1))
    n1 += razao
print('Esses são os 10 primeiros termos!')