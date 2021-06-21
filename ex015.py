cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'val': '\033[1;33m', 'res': '\033[1;32m',
       'som': '\033[1;31m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 015  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias'
      'pelos quais ele foi \nalugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km'
      'rodado.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
km = float(input('Quantos quilômetros você rodou? '))
dia = int(input('Por quantos dias você o alugou? '))
rod = km * 0.15
aluguel = dia * 60
total = rod + aluguel
print('Se você rodou {}{:.2f}{}km terá que pagar R${}{:.2f}{}!'.format(cor['val'], km, cor['reset'],
                                                                       cor['res'], rod, cor['reset']))
print('Se o usou por {}{:.0f}{} dias o valor ficará R${}{:.2f}{}!'.format(cor['val'], dia, cor['reset'],
                                                                          cor['res'], aluguel, cor['reset']))
print('Sendo assim você terá que pagar o valor final de R${}{:.2f}{}!'.format(cor['som'], total, cor['reset']))
