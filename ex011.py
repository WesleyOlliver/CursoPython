cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'med': '\033[1;33m', 'res': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 011  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de '
      'tinta necessária \npara pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
comp = float(input('Qual o comprimento da parede (m): '))
alt = float(input('Qual a altura da parede (m): '))
area = comp * alt
print('Em uma parede com dimenssões de {}{}{} x {}{}{} terá uma área de {}{:.2f}{}m².'
      .format(cor['med'], comp, cor['reset'],
              cor['med'], alt, cor['reset'],
              cor['res'], area, cor['reset']))
tinta = area / 2
print('Sendo assim, será preciso {}{:.3f}{} litros de tinta para pintá-la!'.format(cor['res'], tinta, cor['reset']))
