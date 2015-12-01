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
vaike_font=pygame.font.SysFont("calibri",30)
keskmine_font=pygame.font.SysFont("calibri",50)
suur_font=pygame.font.SysFont("calibri",60)

def mangu_algus():
    algus=True
    while algus:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit
                    quit()
        prindi_ekraanile("Tere tulemast mängima ussimängu!", punane, -170, "suur")
        prindi_ekraanile("Selles mängus pead söötma ussi ja seeläbi teda kasvatama.", must, -90, "väike")
        prindi_ekraanile("Mängu alustamiseks vajuta ''s''", must, -65, "väike")
        prindi_ekraanile("Pausiks vajuta ''p''", must, -32, "väike")
        prindi_ekraanile("ning mängu lõpetamiseks vajuta ''q''", must, -2, "väike")
        prindi_ekraanile("Mäng saab läbi, kui põrkad ussiga vastu seina või vastu ussisaba", must, 50, "väike")
        
        pygame.display.update()
