total = expensive = cont = cheap = 0
cheapN = ' '
while True:
    produto = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if cont == 1 or preco < cheap:
        cheap = preco
        cheapN = produto
    if preco > 1000:
        expensive += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
    if opcao == 'N':
        break

print(f'O total da compra foi R${total}')
print(f'Temos {expensive} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {cheapN} que custa R${cheap}')