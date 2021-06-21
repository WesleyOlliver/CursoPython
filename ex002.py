cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'nom': '\033[1;33m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 002  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
nome = input('Olá, como você se chama? ')
print('Muito prazer em te conhecer, {}{}{}!'.format(cor['nom'], nome, cor['reset']))
