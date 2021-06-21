cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'num': '\033[1;33m', 'soma': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 003  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Crie um programa que leia dois números e mostre a soma entre eles.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
n1 = int(input('Por favor, digite um valor: '))
n2 = int(input('Agora digite mais um valor: '))
s = n1 + n2
print('A soma de {}{}{} e {}{}{} é igual à {}{}{}!'.format(cor['num'], n1, cor['reset'], cor['num'], n2, cor['reset'],
                                                           cor['soma'], s, cor['reset']))
