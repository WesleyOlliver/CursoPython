from datetime import date
cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'nao': '\033[1;33m', 'sim': '\033[1;32m',
       'ano': '\033[1;31m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 032  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa que leia um ano qualquer e mostre se ele é bissexto.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
ano = int(input('Que ano você gostaria de analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {}{}{} é {}BISSEXTO{}!'.format(cor['ano'], ano, cor['reset'], cor['sim'], cor['reset']))
else:
    print('O ano de {}{}{} {}NÃO{} é {}BISSEXTO{}!'.format(cor['ano'], ano, cor['reset'], cor['nao'], cor['reset'],
                                                           cor['nao'], cor['reset']))
