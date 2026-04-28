sexo = input('Sexo [M/F]: ').strip().upper()[0]
while sexo != "M" and sexo != "F":
    print('\033[1;31mTente novamente"\033[m')
    sexo = input('Sexo [M/F]: ').strip().upper()[0]

print('Obrigado por colaborar!')