cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'res': '\033[1;32m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 012  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
valor = float(input('Informe o valor do produto: R$'))
desc = valor - (valor * 0.05)
print('Se você comprar ele com 5% de desconto ele sairá apenas por R${}{:.2f}{}!'
      .format(cor['res'], desc, cor['reset']))
