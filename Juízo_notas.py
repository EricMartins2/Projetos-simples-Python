student = dict()
student['Nome'] = str(input('Nome: '))
student['Média'] = float(input(f'Média de {student['Nome']}: '))

print(f'Nome é igual a {student['Nome']}')
print(f'Média é igual a {student['Média']}')
if student['Média'] < 7:
    print('Situação é igual a Reprovado!')
else:
    print('Situação é igual a Aprovado!')