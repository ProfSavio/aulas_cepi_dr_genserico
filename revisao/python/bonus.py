# Peça nível e energia.
# Se nível >=15 e energia >50, libere o chefe final.

nivel = int(input('Nível: '))

energia = int(input('Energia: '))
if nivel >= 15 and energia > 50:
    print('Chefe final liberado')
else:
    print('Acesso negado')