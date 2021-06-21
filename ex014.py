cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'cel': '\033[1;33m', 'far': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 014  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Escreva um programa que converta uma temperatura digitando em graus Celsius e convertendo para graus '
      'Fahrenheit.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
cel = float(input('Qual é a temperatura atual °C: '))
far = (cel * 9 / 5) + 32
print('A conversão de {}{}{}°C Celsius para Fahrenheit é {}{}{}°F!'.format(cor['cel'], cel, cor['reset'],
                                                                           cor['far'], far, cor['reset']))
