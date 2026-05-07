num = int(input('Digite um número inteiro: '))
soma = num
cont = 1
maior = num
menor = num
opcao = input('Quer continuar [S/N]? ').strip().lower()[0]
while opcao != 'n':
    num = int(input('Digite outro número inteiro: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    cont += 1
    opcao = input('Quer continuar [S/N]? ').strip().lower()[0]
if maior == menor:
    print('Não há um número MAIOR ou MENOR! Somente {} foi digitado'.format(num))
else:
    print('O \033[1;4;36mMAIOR\033[m número digitado foi {}, enquanto o \033[1;4;36mMENOR\033[m foi {}'.format(maior, menor))
media = soma / cont
print('A MÉDIA dos números digitados é \033[1;31m{}\033[m'.format(media))
