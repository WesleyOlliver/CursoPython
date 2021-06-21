cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'din': '\033[1;33m', 'res': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 010  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode '
      'comprar.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
real = float(input('Quanto dinheiro você possui na carteira: R$'))
dolar = real / 5.24
euro = real / 6.39
print('Com R${}{:.2f}{} você pode comprar US${}{:.2f}{} ou EUR€{}{:.2f}{}'.format(cor['din'], real, cor['reset'],
                                                                                  cor['res'], dolar, cor['reset'],
                                                                                  cor['res'], euro, cor['reset']))
