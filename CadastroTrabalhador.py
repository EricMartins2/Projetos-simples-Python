from datetime import date

anoA = date.today().year
dici = {
    'nome': input('Nome: '),
    'idade': int(input('Ano de nascimento: ')),
    'cts': int(input('Carteira de trabalho (0 não tem): ')),
}

dici['idade'] = anoA - dici['idade']
if dici['cts'] != 0:
    dici['contratação'] = int(input('Ano de contratação: '))
    dici['salario'] = float(input('Salário: R$ '))
    dici['aposentadoria'] = ((dici['idade'] - (anoA - dici['contratação'])) + 35)

print(dici)

for i, v in dici.items():
    print(f'{i} tem o valor {v}')