cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'msg': '\033[7;38;43m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 001  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Nesse vídeo, mostraremos como criar um projeto Python no PyCharm e deixar tudo preparado para receber os '
      'exercícios da série, \nque vão utilizar o mesmo projeto.{}'.format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
print('{}Olá, Mundo!{}'.format(cor['msg'], cor['reset']))
msg = 'Olá, Mundo!'
print(msg)
