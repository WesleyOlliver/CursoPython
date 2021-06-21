from random import choice
cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'nom': '\033[1;32m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 019  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, '
      'lendo o nome dos \nalunos e escrevendo na tela o nome do escolhido.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
al1 = input('Informe o primeiro aluno: ')
al2 = input('Informe o segundo aluno: ')
al3 = input('Informe o terceiro aluno: ')
al4 = input('Informe o quarto aluno: ')
lista = [al1, al2, al3, al4]
esc = choice(lista)
print('O aluno escolhido foi {}{}{}!'.format(cor['nom'], esc, cor['reset']))
