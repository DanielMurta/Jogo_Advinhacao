from random import randint
from time import sleep

def Titulo():
    print('=' * 50)
    print(f'               JOGO DA ADVINHAÇÃO')
    print('Vou pensar em um número de 0 à 5, tente advinhar..')
    print('=' * 50)


computador = randint(0, 5)
Titulo()
Chance = 3
while Chance >= 0:
    N1 = int(input('Em que número eu pensei?: '))
    print('PROCESSANDO...')
    sleep(1)
    if N1 == computador:
        print('_'*50)
        print("\033[4;32mAcertou!!\033[m Eu pensei no número {}.".format(computador))
        break
    else:
        print('_'*50)
        if Chance == 0:
            print('\033[4;31mPERDEU !! Você não possuiu mais chances!\033[m')
            break
        else:
            print('\033[33mNão foi dessa vez !! Tente novamente!\033[m')
            print(f'Você possui mais {Chance} chances...')
            Chance -= 1
