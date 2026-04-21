for person in range(1, 6):
    peso = float(input("Peso da pessoa {}: ".format(person)))
    if person == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('''Maior peso lido: {:.2f} Kg
Menor peso lido: {:.2f} Kg'''.format(maior, menor))