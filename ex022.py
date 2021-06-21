cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'str': '\033[1;32m', 'num': '\033[1;33m',
       'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset']) * 18, '{} Exercício 022  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset']) * 18)
print('{}Crie um programa que leia o nome completo de uma pessoa e mostra:'
      '\n°O nome com todas as letras maiúsculas. '
      '\n°O nome com todas minúsculas. '
      '\n°Quantas letras ao todo (sem considerar espaços). '
      '\n°Quantas letras tem o primeiro nome.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset']) * 42)
nome = str(input('Por favor digite seu nome completo: ')).strip()
print('Analizando seu nome ....')
print('Seu nome com todas as letras maiúsculas: {}{}{}'.format(cor['str'], nome.upper(), cor['reset']))
print('Seu nome com todas as letras minúsculas: {}{}{}'.format(cor['str'], nome.lower(), cor['reset']))
print('Seu nome possui um total de {}{}{} letras.'.format(cor['num'], len(nome) - nome.count(' '), cor['reset']))
div = nome.split()
print('Seu primeiro nome é {}{}{} e ele possui {}{}{} letras.'.format(cor['str'], div[0], cor['reset'],
                                                                      cor['num'], len(div[0]), cor['reset']))
