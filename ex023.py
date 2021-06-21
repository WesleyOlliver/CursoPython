cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'num': '\033[1;33m', 'val': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 023  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}{}{} vemos que ele possui: '.format(cor['num'], num, cor['reset']))
print('Unidade: {}{}{}'.format(cor['val'], u, cor['reset']))
print('Dezena: {}{}{}'.format(cor['val'], d, cor['reset']))
print('Centena: {}{}{}'.format(cor['val'], c, cor['reset']))
print('Milhar: {}{}{}'.format(cor['val'], m, cor['reset']))
