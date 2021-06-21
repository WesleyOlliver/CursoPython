cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'num': '\033[1;33m', 'res': '\033[1;32m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 008  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
m = float(input('Informe o comprimento (m): '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('Em {}{}{} metros possue:'.format(cor['num'], m, cor['reset']))
print('{}{:.0f}{} milímetros;'.format(cor['res'], mm, cor['reset']))
print('{}{:.0f}{} centímetros;'.format(cor['res'], cm, cor['reset']))
print('{}{:.0f}{} decímetros;'.format(cor['res'], dm, cor['reset']))
print('{}{:.1f}{} decâmetros;'.format(cor['res'], dam, cor['reset']))
print('{}{:.2f}{} hectômetros;'.format(cor['res'], hm, cor['reset']))
print('{}{:.3f}{} quilômetros;'.format(cor['res'], km, cor['reset']))
