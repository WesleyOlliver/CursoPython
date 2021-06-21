from random import randint
from time import sleep
cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'num': '\033[1;33m', 'vit': '\033[1;32m',
       'der': '\033[1;31m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 028  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário '
      'tentar descobrir qual \nfoi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário '
      'venceu ou perdeu.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
comp = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente advinhar ...')
player = int(input('Em que número eu pensei? '))
print('Processando ...')
sleep(2)
if player == comp:
    print('{}Parabéns{}! Você me derrotou!'.format(cor['vit'], cor['reset']))
else:
    print('{}Ganhei{}! Eu pensei no número {}{}{} e não no {}{}{}!'.format(cor['der'], cor['reset'],
                                                                           cor['vit'], comp, cor['reset'],
                                                                           cor['num'], player, cor['reset']))
