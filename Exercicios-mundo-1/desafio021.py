#Um programa que reproduz audios em mp3

import pygame

pygame.mixer.init()

pygame.mixer.music.load('perdoar.mp3')
pygame.mixer.music.play('perdoar.mp3')
pygame.mixer.music.set_volume(15)
pygame.event.wait()
