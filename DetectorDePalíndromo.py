frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
tamanho = len(junto)
invert = ''
for usuario in junto:
    tamanho = tamanho - 1
    invert += junto[tamanho]

print('Frase inversa: {}'.format(invert))
if invert == junto:
    print('Essa frase é palíndromo')
else:
    print('Essa palavra NÃO é palíndromo!')

