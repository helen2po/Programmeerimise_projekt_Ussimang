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
mang=True
while mang:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ussi_pea[0]+=segmendi_laius
                print("right")
            if event.key==pygame.K_LEFT:
                ussi_pea[0]-=segmendi_laius
                print("left")
            if event.key==pygame.K_UP:
                ussi_pea[1]-=segmendi_korgus
                print("up")
            if event.key==pygame.K_DOWN:
                ussi_pea[1]+=segmendi_korgus
                print("down")
            if event.key==pygame.K_q:
                print("quit")
                pygame.quit()
            ekraan.blit(taust,(0,0))
            
            print(ussi_saba)
            print(ussi_pea)
            if toidu_asukoht[0]==ussi_pea[0] and toidu_asukoht[1]==ussi_pea[1]:
                toidu_asukoht=genereeri_toidu_asukoht()
                ussi_saba.insert(0,(ussi_pea[0],ussi_pea[1]))
                if toidu_asukoht in ussi_pea or toidu_asukoht in ussi_saba:
                    toidu_asukoht=genereeri_toidu_asukoht()            
                toit=pygame.Rect(toidu_asukoht[0],toidu_asukoht[1],segmendi_laius,segmendi_korgus)
                pygame.draw.rect(ekraan,punane,toit)
            else:
                ussi_saba.pop()
                ussi_saba.insert(0,(ussi_pea[0],ussi_pea[1]))
                toit=pygame.Rect(toidu_asukoht[0],toidu_asukoht[1],segmendi_laius,segmendi_korgus)
                pygame.draw.rect(ekraan,punane,toit)

            for i in ussi_saba:
                saba_segment=pygame.Rect(i[0],i[1],segmendi_laius,segmendi_korgus)
                pygame.draw.rect(ekraan,must,saba_segment)
            
            pea=pygame.Rect(ussi_pea[0],ussi_pea[1],segmendi_laius,segmendi_korgus)
            pygame.draw.rect(ekraan,roheline,pea) 
            
        pygame.display.update()
        if ussi_pea in ussi_saba or ussi_pea[0]>775 or ussi_pea[0]<0 or ussi_pea[1]>575 or ussi_pea[1]<0:  #TODO improve
            prindi_ekraanile("Get rekt, skrub.", must, -90, "keskmine")
            prindi_ekraanile("Pls nerf", must, -55, "väike")
            pygame.display.update()
            mang=False

