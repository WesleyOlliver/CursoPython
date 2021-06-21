cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'nom': '\033[1;33m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 025  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}{}{}'.format(cor['nom'], 'SILVA' in nome.upper(), cor['reset']))
