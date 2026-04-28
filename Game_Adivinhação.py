from random import randint
print(20 * '=')

print('''

\033[1;34m{:^20}\033[m

'''.format('DESCUBRA O ALGARISMO'))

print(20 * '=')
print('Sou seu computador e vou escolher um número entre 0 e 10.\nSua tarefa é descobrir o número que eu escolher!')

computador = randint(0, 10)
escolha = int(input('Tente adivinhar o número escolhido entre 0 e 10: '))
tentativas = 1

while escolha != computador:
    tentativas += 1
    print('\033[1;31mTente novamente!\033[m')
    escolha = int(input('Escolha de novo: '))

print('''\033[4;32mPARABÉNS!\033[m Você acertou!
Foram necessárias {} tentativas'''.format(tentativas))
