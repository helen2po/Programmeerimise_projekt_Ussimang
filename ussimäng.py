# Programmeerimise_projekt_Ussimang
# Kood programeerimise projekti jaoks nimega "Ussimäng".

import pygame, random, sys
from pygame.locals import *

#Värvid
valge=(255,255,255)
must=(0,0,0)
punane=(255,0,0)
roheline=(0,155,0)
helesinine=(240,248,255)

#Ekraani mõõtmed
ekraani_laius=800
ekraani_korgus=600

pygame.init()
ekraan=pygame.display.set_mode((ekraani_laius,ekraani_korgus))
ekraan.fill(valge)
pygame.display.update()
pygame.display.set_caption("Ussimäng")

#Fondid
vaikefont=pygame.font.SysFont("calibri",30)
keskminefont=pygame.font.SysFont("calibri",50)
suurfont=pygame.font.SysFont("calibri",60)
