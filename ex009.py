cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'num': '\033[1;33m', 'res': '\033[1;32m',
       'linha': '\033[37m', 'mul': '\033[1;31m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 009  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.{}'.format(cor['título'],
                                                                                                        cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
n = int(input('Digite um número para ver a sua tabuada: '))
print('{}-{}'.format(cor['linha'], cor['reset']) * 45)
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 0, cor['reset'],
                                          cor['res'], n * 0, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 1, cor['reset'],
                                          cor['res'], n * 1, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 2, cor['reset'],
                                          cor['res'], n * 2, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 3, cor['reset'],
                                          cor['res'], n * 3, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 4, cor['reset'],
                                          cor['res'], n * 4, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 5, cor['reset'],
                                          cor['res'], n * 5, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 6, cor['reset'],
                                          cor['res'], n * 6, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 7, cor['reset'],
                                          cor['res'], n * 7, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 8, cor['reset'],
                                          cor['res'], n * 8, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 9, cor['reset'],
                                          cor['res'], n * 9, cor['reset']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cor['num'], n, cor['reset'],
                                          cor['mul'], 10, cor['reset'],
                                          cor['res'], n * 10, cor['reset']))
print('{}-{}'.format(cor['linha'], cor['reset']) * 45)
