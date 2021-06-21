cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'res': '\033[1;31m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 007  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.{}'.format(cor['título'],
                                                                                                         cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
n1 = float(input('Por favor digite a nota do 1º Bimestre: '))
n2 = float(input('Por favor, digite a nota do 2º Bimestre: '))
m = (n1 + n2) / 2
print('Sua média neste semestre foi: {}{:.1f}{}'.format(cor['res'], m, cor['reset']))
