matriz = [[], [], []]
n = 0

for c in range(0, 3):
    for c2 in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {c2}]: '))
        matriz[c].append(n)

for c in range(0, 3):
    for c2 in range(0, 3):
        print(f'[{matriz[c][c2]:^5}]', end='')
    print()

somaP = 0
for c in range(0, 3):
    for c2 in range(0, 3):
        if matriz[c][c2] % 2 == 0:
            somaP += matriz[c][c2]

somaC = 0

for c in range(0, 3):
    somaC += matriz[c][2]

maior = 0
for c in range(0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
    elif c == 0:
        maior = matriz[1][c]

print(f'O soma dos valores pares é: {somaP}')
print(f'A soma dos valores da terceira coluna é: {somaC}')
print(f'O maior valor da segunda linha é: {maior}')

