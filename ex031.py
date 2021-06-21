cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'val': '\033[1;33m', 'desc': '\033[1;32m',
       'via': '\033[1;31m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 031  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando '
      'R$0,50 por Km para \nviagens de até 200Km e R$0,45 para viagens mais longas.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
viagem = float(input('Qual é a distância da sua viagem (Km)? '))
print('Você está prestes a começar uma viagem de {}{:.1f}Km{}'.format(cor['via'], viagem, cor['reset']))
if viagem <= 200:
    print('O preço da sua viagem será de {}R${:.2f}{}!'.format(cor['val'], viagem * 0.5, cor['reset']))
else:
    print('O preço da sua viagem será de {}R${:.2f}{}'.format(cor['desc'], viagem * 0.45, cor['reset']))
