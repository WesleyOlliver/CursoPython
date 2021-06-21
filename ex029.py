cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'vel': '\033[1;32m', 'mul': '\033[1;31m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 029  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem que ele '
      'foi multado. A \nmulta vai custar R$7,00 por cada Km acima do limite.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
km = float(input('Qual a velocidade atual do carro (Km)? '))
if km > 80:
    print('{}VOCÊ FOI MULTADO!{} Você ultrapassou o limite permitido que é de {}80Km/h{}.'
          .format(cor['mul'], cor['reset'], cor['vel'], cor['reset']))
    print('Sua multa ficará no valor de {}R${:.2f}{}!'.format(cor['mul'], (km - 80) * 7, cor['reset']))
print('Tenha um bom dia! Dirija com segurança!')
