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
ekraan.fill(helesinine)
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
                    algus=False
                if event.key==pygame.K_q:
                    pygame.quit
                    quit()
        prindi_ekraanile("Ussimäng", punane, -170, "suur")
        prindi_ekraanile("Selles mängus pead söötma ussi ja seeläbi teda kasvatama.", must, -90, "väike")
        prindi_ekraanile("Mängu alustamiseks vajuta ''s''", must, -65, "väike")
        prindi_ekraanile("Pausiks vajuta ''p''", must, -32, "väike")
        prindi_ekraanile("Mängu lõpetamiseks vajuta ''q''", must, -2, "väike")
        prindi_ekraanile("Mäng saab läbi, kui põrkad ussiga vastu seina või vastu ussisaba", must, 50, "väike")
        prindi_ekraanile("Mängimiseks kasuta nooleklahve", must, 75, "väike")
        pygame.display.update()
        
def muuda_teksti_suurus(tekst, värv, suurus):
    if suurus=="väike":
        teksti_valimus=vaike_font.render(tekst,True,värv)
    elif suurus=="keskmine":
        teksti_valimus=keskmine_font.render(tekst,True,värv)
    elif suurus=="suur":
        teksti_valimus=suur_font.render(tekst,True,värv)
    return teksti_valimus, teksti_valimus.get_rect()    

def prindi_ekraanile(tekst, värv, y_nihe, suurus):
    teksti_valimus,valjastatud_tekst=muuda_teksti_suurus(tekst, värv, suurus)
    valjastatud_tekst.center=(ekraani_laius/2),(ekraani_korgus/2)+y_nihe
    ekraan.blit(teksti_valimus,valjastatud_tekst)



#def segment(x,y):
#    
#
#    return()
#segmendi_laius=10
#segmendi_korgus=10
#ussi_asukoht=[]
#def uss():
#    for i in range(4):
#        ussi_x=400-segmendi_laius*i
#        ussi_y=300
#        ussi_segment=segment(ussi_x,ussi_y)
#        ussi_asukoht.append(ussi_segment)

#def toidu_asukoht():
#    ussi_asukoht=[(x1,y1),(x2,y2)]
#    while True:
#        toidu_asukoht=(random.randint(0,800),random.randint(0,600))
#        if toidu_asukoht not in ussi_asukoht:
#            genereeri_toit(x,y)
#            break

#    toidu_x_koord=random.randint(0,600)
#    toidu_y_koord=random.randint(0,800)
#    return(toidu_x_koord,toidu_y_koord)
