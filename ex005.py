cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'num': '\033[1;33m', 'res': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 005  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
n = int(input('Por favor digite um número qualquer: '))
print('Analisando o número {}{}{}, seu antecessor é o {}{}{} e seu sucessor é o {}{}{}!'
      .format(cor['num'], n, cor['reset'], cor['res'], (n - 1), cor['reset'], cor['res'], (n + 1), cor['reset']))
