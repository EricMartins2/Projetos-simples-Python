from random import randint
victory = 0
while True:
    jogador = int(input('Digite um valor: '))
    grupo = ' '
    while grupo not in 'PpIi':
        grupo = input('Par ou Ímpar? ')[0]
    computador = randint(1,10)
    soma = jogador + computador
    print('-'*25)
    print(f'Você escolheu {jogador} e o computador {computador}. Total de {soma} deu ', end='')
    if soma % 2 == 0:
        print('PAR')
        print('-'*25)
        if grupo in 'Pp':
            print('Você venceu!')
            victory += 1
        else:
            print('Você perdeu!')
            print('-='*25)
            break
    else:
        print('ÍMPAR')
        print('-'*25)
        if grupo in 'Ii':
            print('Você venceu!')
            victory += 1
        else:
            print('Você perdeu!')
            print('-='*25)
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você venceu {victory} vezes.')