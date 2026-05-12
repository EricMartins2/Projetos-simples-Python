valor = 0
multiplicador = 0
print('-'*20)
print('\033[1;34mTABUADA\033[m')
print('-'*20)
while True:
    if multiplicador == 0 or multiplicador == 10:
        valor = int(input('Quer ver a tabuada de qual valor? '))
        print('-'*20)
        multiplicador = 0
        if valor < 0:
            break
    multiplicador += 1
    print(f'{valor} x {multiplicador} = {valor*multiplicador}')
    if multiplicador == 10:
        print('-'*20)

print('O PROGRAMA TABUADA FOI ENCERRADO! Volte sempre!')

