from math import radians, cos, sin, tan
cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'ang': '\033[1;33m', 'val': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 018  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse '
      'ângulo.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
an = float(input('Informe o ângulo: '))
ang = radians(an)
co = cos(ang)
se = sin(ang)
ta = tan(ang)
print('O ângulo de {}{}{} tem o Cosseno de {}{:.2f}{}.'.format(cor['ang'], an, cor['reset'],
                                                               cor['val'], co, cor['reset']))
print('O ângulo de {}{}{} tem o Seno de {}{:.2f}{}.'.format(cor['ang'], an, cor['reset'],
                                                            cor['val'], se, cor['reset']))
print('O ângulo de {}{}{} tem a Tangente de {}{:.2f}{}.'.format(cor['ang'], an, cor['reset'],
                                                                cor['val'], ta, cor['reset']))
