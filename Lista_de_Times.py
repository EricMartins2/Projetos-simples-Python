tabela = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino', 'Coritiba',
 'São Paulo', 'Bahia', 'Cruzeiro', 'Botafogo', 'Vitória', 'Atlético-MG', 'Internacional', 'Grêmio',
 'Corinthians', 'Vasco', 'Santos', 'Mirassol', 'Remo', 'Chapecoense')

print(f'Lista de times do brasileirão: {tabela}')
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print(f'Os 4 últimos são: {tabela[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(f'O Chapecoense está na {tabela.index('Chapecoense')+1}° posição')

