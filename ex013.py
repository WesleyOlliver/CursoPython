cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'sal': '\033[1;33m', 'res': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 013  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
sal = float(input('Qual é o valor do seu salário atual? R$'))
aum = sal + (sal * 0.15)
print('Seu salário de R${}{:.2f}{} terá um reajuste de 15% e você receberá a partir deste momento R${}{:.2f}{}!'
      .format(cor['sal'], sal, cor['reset'], cor['res'], aum, cor['reset']))
