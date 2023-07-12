# Faça um programa em Phyton que abra e reproduza o áudio de um arquivo em MP3.

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
#pygame.event.wait()

