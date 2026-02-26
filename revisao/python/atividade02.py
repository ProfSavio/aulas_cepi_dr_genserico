# Peça a vida do personagem.
# Se a vida for menor ou igual a 0, mostre 'Game Over'.
# Caso contrário, mostre que o personagem está vivo.

vida = int(input('Digite a vida: '))

if vida <= 0:
    print('Game Over')
else:
    print('Personagem vivo')
