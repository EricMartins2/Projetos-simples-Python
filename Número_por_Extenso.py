contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {contagem[numero]}')
    opcao = input('Você quer continuar? [S/N] ')
    if opcao in 'Nn':
        break
    while opcao not in 'SsNn':
        opcao = input('Tente novamente. Você quer continuar? [S/N] ')





