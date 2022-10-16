from random import randint
from time import sleep
computador = randint(0, 5)
print('_' *50)
print('Vou pensar em um número de 0 à 5 tente advinhar...')
print('_' *50)
N1 = int(input('Em que número eu pensei?: '))
print('PROCESSANDO...')
sleep(2)
if N1 == computador:
    print("Acertou!! Eu pensei no número {}".format(computador))
else:
    print('Você Perdeu!! Eu pensei no número {}'.format(computador))