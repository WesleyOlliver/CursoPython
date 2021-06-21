cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'imp': '\033[1;33m', 'par': '\033[1;32m',
       'num': '\033[1;31m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 030  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
num = int(input('Digite um número qualquer: '))
par = num % 2
if par == 0:
    print('O número {}{}{} é {}PAR{}!'.format(cor['num'], num, cor['reset'], cor['par'], cor['reset']))
else:
    print('O número {}{}{} é {}ÍMPAR{}!'.format(cor['num'], num, cor['reset'], cor['imp'], cor['reset']))
