from math import trunc
cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'val': '\033[1;33m', 'int': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 016  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
num = float(input('Por favor digite um valor: '))
print('O valor digitado foi {}{}{} e sua porção inteira é {}{}{}!'.format(cor['val'], num, cor['reset'],
                                                                          cor['int'], trunc(num), cor['reset']))
