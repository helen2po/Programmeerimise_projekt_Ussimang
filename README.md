# Programmeerimise_projekt_Ussimang
#Kood programeerimise projekti jaoks nimega "Ussimäng".

# Programmeerimise_projekt_Ussimang
# Kood programeerimise projekti jaoks nimega "Ussimäng".

import pygame, random, sys
from pygame.locals import *

#Värvid
valge=(255,255,255)
must=(0,0,0)
punane=(255,0,0)
roheline=(0,155,0)

#Ekraani mõõtmed
ekraani_laius=800
ekraani_korgus=600

pygame.init()
ekraan=pygame.display.set_mode((ekraani_laius,ekraani_korgus))
ekraan.fill(valge)
pygame.display.update()
pygame.display.set_caption("Ussimäng")

#Fondid
vaikefont=pygame.font.SysFont("comicsans",30)
keskminefont=pygame.font.SysFont("comicsans",50)
suurfont=pygame.font.SysFont("comicsans",60)


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
        tekst_ekraanil("Tere tulemast mängima ussimängu!", punane, -170, "suur")
        tekst_ekraanil("Selles mängus pead söötma ussi ja seeläbi teda kasvatama.", must, -90, "väike")
        tekst_ekraanil("Mängu alustamiseks vajuta ''s''", must, -65, "väike")
        tekst_ekraanil("Pausiks vajuta ''p''", must, -32, "väike")
        tekst_ekraanil("ning mängu lõpetamiseks vajuta ''q''", must, -2, "väike")
        tekst_ekraanil("Mäng saab läbi, kui põrkad ussiga vastu seina või vastu ussisaba", must, 50, "väike")
        
        pygame.display.update()

def teksti_kuju(tekst, värv, suurus):
    if suurus=="väike":
        teksti_valimus=vaikefont.render(tekst,True,värv)
    elif suurus=="keskmine":
        teksti_valimus=keskminefont.render(tekst,True,värv)
    elif suurus=="suur":
        teksti_valimus=suurfont.render(tekst,True,värv)

    return teksti_valimus, teksti_valimus.get_rect()    

def tekst_ekraanil(tekst, värv, paiknemine, suurus):
    teksti_valimus,valjastatud_tekst=teksti_kuju(tekst, värv, suurus)
    valjastatud_tekst.center=(ekraani_laius/2),(ekraani_korgus/2)+paiknemine
    ekraan.blit(teksti_valimus,valjastatud_tekst)
    

mangu_algus()
                    





pygame.quit




















