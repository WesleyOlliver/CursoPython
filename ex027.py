cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'pri': '\033[1;33m', 'ult': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 027  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome '
      'separadamente.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
div = nome.split()
print('Seu primeiro nome é {}{}{}.'.format(cor['pri'], div[0], cor['reset']))
print('Seu último nome é {}{}{}.'.format(cor['ult'], div[len(div) - 1], cor['reset']))
