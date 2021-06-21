cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'nao': '\033[1;31m', 'sim': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 035  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um '
      'triângulo.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print('Com os lados passados {}PODEMOS FORMAR{} um triângulo!'.format(cor['sim'], cor['reset']))
else:
    print('Com os lados passados {}NÃO PODEMOS FORMAR{} um triângulo!'.format(cor['nao'], cor['reset']))
