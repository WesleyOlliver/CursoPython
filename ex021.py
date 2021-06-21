import pygame
cor = {'traço': '\033[35m', 'ex': '\033[4;31m', 'título': '\033[1;34m', 'reset': '\033[m'}
print('{}-=-{}'.format(cor['traço'], cor['reset'])*18, '{} Exercício 021  {}'.format(cor['ex'], cor['reset']),
      '{}-=-{}'.format(cor['traço'], cor['reset'])*18)
print('{}Faça um programa em Python que abra e reproduza aúdio de um arquivo MP3.{}'
      .format(cor['título'], cor['reset']))
print('{}-=-{}'.format(cor['traço'], cor['reset'])*42)
pygame.init()
pygame.mixer.music.load('king.mp3')
pygame.mixer.music.play()
pygame.event.wait()
