alunos = list()
nivel1 = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    opcao = input('Quer continuar [S/N]? ')[0].lower()
    media = (nota1 + nota2) / 2
    nivel2 = [nota1, nota2]
    nivel1 = [nome, media, nivel2]
    alunos.append(nivel1[:])
    if opcao == 'n':
        break

print('-='*30)
print('N°', end='  ')
print('NOME', end='       ')
print('MÉDIA')
print('-' * 30)
for pos, cont in enumerate(alunos):
    print(pos, end='   ')
    print(f'{cont[0]:<8}', end='    ')
    print(f'{cont[1]}')
print('-'*20)

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    elif opcao <= len(alunos) - 1:
        print(f'Notas de {alunos[opcao][0]} são: {alunos[opcao][2]}')







