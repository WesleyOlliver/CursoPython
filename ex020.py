from random import shuffle
cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'nom': '\033[1;32m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 020  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}O mesmo professor do exercício 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um'
      'programa que leia o \nnome dos quatros alunos e mostre a ordem sorteada.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
al1 = input('Informe o primeiro aluno: ')
al2 = input('Informe o segundo aluno: ')
al3 = input('Informe o terceiro aluno: ')
al4 = input('Informe o quarto aluno: ')
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será a seguinte: ')
print(cor['nom'], lista, cor['reset'])
