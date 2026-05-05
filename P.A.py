n1 = int(input('Primeiro termo: '))
razao = int(input('Qual a razão: '))
cont = 1
posicao = 0
repeticoes = 10
escolha = 1
while escolha != 0:
    while cont <= repeticoes:
        posicao += 1
        print('{}° Termo -> {}'.format(posicao, n1))
        n1 += razao
        cont += 1
    escolha = int(input('Quantos termos a mais você quer? '))
    repeticoes += escolha
print('Esses são os {} termos da P.A!'.format(repeticoes))