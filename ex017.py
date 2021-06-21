from math import hypot
cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'hip': '\033[1;32m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 017  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.'
      'Calcule e mostre o \ncomprimento da hipotenusa.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(cat1, cat2)
print('O valor da hipotenusa deste triângulo é {}{:.2f}{}!'.format(cor['hip'], hip, cor['reset']))
