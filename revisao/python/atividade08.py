# 1-Guerreiro | 2-Mago | 3-Arqueiro
# Mostre o personagem escolhido ou inválido.

opcao = int(input('Escolha: '))

if opcao == 1:
    print('Guerreiro')
elif opcao == 2:
    print('Mago')
elif opcao == 3:
    print('Arqueiro')
else:
    print('Inválido')