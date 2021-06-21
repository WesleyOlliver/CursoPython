cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'cid': '\033[1;33m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 24  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
cidade = str(input('Digite a cidade em que você nasceu: ')).strip()
cid = (cidade.upper()).split()
print(cor['cid'], 'SANTO' in cid[0], cor['reset'])
