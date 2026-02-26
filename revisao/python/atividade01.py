# Peça o nível do jogador.
# Se o nível for maior ou igual a 10, mostre que o modo ranqueado está liberado.
# Caso contrário, informe que ainda está bloqueado.

nivel = int(input('Qual é o seu nivel: '))

if nivel >= 10:
    print('Modo ranqueado liberado')
else:
    print('Modo ranqueado bloqueado')
