# Peça o valor do dano.
# Se o dano for par, mostre 'Ataque crítico'. Caso contrário, 'Ataque normal'.

dano = int(input('Digite o dano: '))

if dano % 2 == 0:
    print('Ataque crítico')
else:
    print('Ataque normal')
