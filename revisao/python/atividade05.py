# Peça a energia (0 a 100).
# Energia >= 70: alta
# Entre 30 e 69: média
# Abaixo de 30: baixa

energia = int(input('Energia: '))

if energia >= 70:
    print('Energia alta')
elif energia >= 30:
    print('Energia média')
else:
    print('Energia baixa')