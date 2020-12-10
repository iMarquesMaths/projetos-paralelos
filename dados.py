from random import randint
from time import sleep

cores = {'amarelo': '\033[1;33m',
         'azul': '\033[34m',
         'verde': '\033[1;32m',
         'cinza': '\033[37m',
         'reset': '\033[m'}

frase = "DADO VIRTUAL"
print('{}-'.format(cores['amarelo']) * 30)
print(frase.center(30))
print('-' * 30, '{}'.format(cores['reset']))
resp = input('Vamos começar? {}[S/N]{} '.format(cores['verde'], cores['reset'])).strip().upper()

while resp not in 'SN':
    #print('{}-'.format(cores['cinza']) * 20, '{}'.format(cores['reset'])) #Ficou melhor sem essa linha
    resp = input('Não entendi, entre com {}[S/N]{} '.format(cores['verde'], cores['reset'])).strip().upper()

while resp == 'S':
    print('{}Rolando dado...{}'.format(cores['cinza'], cores['reset']))
    sleep(1.25)
    dado = randint(1, 6)
    print('O valor do dado é {}{}{}'.format(cores['azul'], dado, cores['reset']))
    print('{}-'.format(cores['cinza']) * 20, '{}'.format(cores['reset']))
    resp = str(input('Vamos denovo? {}[S/N]{} '.format(cores['verde'], cores['reset']))).strip().upper()[0]
    while resp not in 'SN':
        #print('{}-'.format(cores['cinza']) * 20, '{}'.format(cores['reset'])) #Ficou melhor sem essa linha
        resp = input('Não entendi, entre com {}[S/N]{} '.format(cores['verde'], cores['reset'])).strip().upper()[0]

if resp == 'N':
    print('{}-'.format(cores['cinza']) * 20, '{}'.format(cores['reset']))
    print('Okay, mais tarde jogamos.')
print('\033[7mFim do jogo\033[m')
