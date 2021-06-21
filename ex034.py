cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', '010': '\033[1;33m', '015': '\033[1;32m',
       'sal': '\033[1;31m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 034  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários '
      'superiores a \nR$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
sal = float(input('Qual é o valor do salário do funcionário? R$'))
if sal > 1250:
    print('Quem ganhava {}R${:.2f}{} passa a ganhar agora {}R${:.2f}{}!'.format(cor['sal'], sal, cor['reset'],
                                                                                cor['010'], sal * 1.1, cor['reset']))
else:
    print('Quem ganhava {}R${:.2f}{} passa a ganhar agora {}R${:.2f}{}!'.format(cor['sal'], sal, cor['reset'],
                                                                                cor['015'], sal * 1.15, cor['reset']))
