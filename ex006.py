cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'num': '\033[1;33m', 'res': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 006  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.{}'.format(cor['título'],
                                                                                                      cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
n = int(input('Por favor, digite um valor: '))
print('Analisando o valor {}{}{}, vemos que: \nSeu dobro é {}{}{};'.format(cor['num'], n, cor['reset'], cor['res'],
                                                                           (n * 2), cor['reset']))
print('Seu triplo é {}{}{}; \nSua raiz quadrada é {}{:.2f}{};'.format(cor['res'], (n * 3), cor['reset'], cor['res'],
                                                                      (n**(1/2)), cor['reset']))
