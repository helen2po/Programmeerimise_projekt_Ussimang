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


ussi_pea=pygame.image.load("nyancat.png")
toit=pygame.image.load("vikerkaar.png")
ussi_saba=pygame.image.load("vikerkaare_saba.png")
#ekraan.blit(ussi_pea,(ussi_x,ussi_y))

segmendi_laius=25
segmendi_korgus=25

ussi_pea=[[400,300]]

mangu_algus()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ussi_pea[0][0]+=segmendi_laius
                print("right")
            if event.key==pygame.K_LEFT:
                ussi_pea[0][0]-=segmendi_laius
                print("left")
            if event.key==pygame.K_UP:
                ussi_pea[0][1]-=segmendi_korgus
                print("up")
            if event.key==pygame.K_DOWN:
                ussi_pea[0][1]+=segmendi_korgus
                print("down")
        ekraan.blit(taust,(0,0))
        
    #joonista uss, blit pea jaoks, draw.rect saba jaoks
        for i in ussi_pea:
            ussi_segment=pygame.Rect(ussi_pea[0][0],ussi_pea[0][1],segmendi_laius,segmendi_korgus) #teeb ristküliku, mille vasak ülemine nurk on x_koord=100, y_koord=0, laius=100, kõrgus=100
            pygame.draw.rect(ekraan,must,ussi_segment)
           
    pygame.display.update()

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
