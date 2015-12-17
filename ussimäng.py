#taustamuusika võetud: https://www.youtube.com/watch?v=MD6oDnm43HA
#nyancat ja saba võetud: https://www.youtube.com/watch?v=QH2-TGUlwu4

import pygame, random, sys, time, winsound
from pygame.locals import *

pygame.init()

#Akna mõõtmed
ekraani_laius=800
ekraani_korgus=600

#Värvid
valge=(255,255,255)
must=(0,0,0)
punane=(255,0,0)
roheline=(0,155,0)
helesinine=(240,248,255)

#Akna suvandid
ekraan=pygame.display.set_mode((ekraani_laius,ekraani_korgus))
taust=pygame.Surface(ekraan.get_size()).convert()
pygame.display.set_caption("Ussimäng")
taust.fill(helesinine)
ekraan.fill(helesinine)

#Fondid
vaike_font=pygame.font.SysFont("calibri",30)
keskmine_font=pygame.font.SysFont("calibri",50)
suur_font=pygame.font.SysFont("calibri",60)

#Tekstuurid
pea_pilt=pygame.image.load("nyankatze.png")
pea_pilt=pygame.transform.scale(pea_pilt, (25, 25))
toidu_pilt=pygame.image.load("vikerkaar.png")
toidu_pilt=pygame.transform.scale(toidu_pilt,(25,25))
saba_pilt=pygame.image.load("vikerkaare_saba.png")
saba_pilt=pygame.transform.scale(saba_pilt,(25,25))

#Segmendi suurus
segmendi_laius=25
segmendi_korgus=25

#Taimer
clock=pygame.time.Clock()

#Ussi esialgne asukoht
pea_x=375
pea_y=300


#Abimeetodid
def joonista_tutvustus():
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
        prindi_ekraanile("Mängu lõpetamiseks vajuta ''q''", must, -32, "väike")
        prindi_ekraanile("Mäng saab läbi, kui põrkad ussiga vastu seina või vastu ussisaba", must, 20, "väike")
        prindi_ekraanile("Mängimiseks kasuta nooleklahve", must, 45, "väike")
        pygame.display.update()
        clock.tick(5)
        
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

def loo_uus_toit():
    global toidu_asukoht
    toidu_asukoht=[random.randrange(0,775,25), random.randrange(0,575,25)]

def joonista_elemendid():
    ekraan.blit(taust,(0,0))
    toit=pygame.Rect(toidu_asukoht[0],toidu_asukoht[1],segmendi_laius,segmendi_korgus)
    pygame.draw.rect(ekraan,punane,toit)
    ekraan.blit(toidu_pilt,toit)
    
    for i in ussi_saba:
        saba_segment=pygame.Rect(i[0],i[1],segmendi_laius,segmendi_korgus)
        pygame.draw.rect(ekraan,must,saba_segment)
        ekraan.blit(saba_pilt,saba_segment)
    pea=pygame.Rect(ussi_pea[0],ussi_pea[1],segmendi_laius,segmendi_korgus)
    pygame.draw.rect(ekraan,roheline,pea)

    ekraan.blit(pea_pilt, pea)
    pygame.display.update()

def mangu_tsukkel():
    suund="left"
    start=time.time()
    while True:
        lopp = time.time()
        vahe = lopp-start
        if vahe < 0.2:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and (event.key==pygame.K_DOWN or event.key==pygame.K_UP or event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_q):
                    ussi_saba.insert(0,[ussi_pea[0],ussi_pea[1]])

                    #Vastavalt nupule liiguta ussi pead
                    if event.key==pygame.K_RIGHT:
                        ussi_pea[0]+=segmendi_laius
                        suund="right"
                    if event.key==pygame.K_LEFT:
                        ussi_pea[0]-=segmendi_laius
                        suund="left"
                    if event.key==pygame.K_UP:
                        ussi_pea[1]-=segmendi_korgus
                        suund="up"
                    if event.key==pygame.K_DOWN:
                        ussi_pea[1]+=segmendi_korgus
                        suund="down"
                    if event.key==pygame.K_q:
                        pygame.quit()

                    #Kas uss sai toitu või mitte?
                    if toidu_asukoht[0]==ussi_pea[0] and toidu_asukoht[1]==ussi_pea[1]:
                        loo_uus_toit()
                    else:
                        ussi_saba.pop()

                    joonista_elemendid()
                    start=time.time()

                    #Kontrolli surma
                    if ussi_pea in ussi_saba or ussi_pea[0]>775 or ussi_pea[0]<0 or ussi_pea[1]>575 or ussi_pea[1]<0:  #TODO improve
                        prindi_ekraanile("Get rekt, skrub.", must, -90, "keskmine")
                        prindi_ekraanile("Pls nerf", must, -55, "väike")
                        prindi_ekraanile("RIP in peace, autist", must, -15, "väike")
                        
                        pygame.display.update()
                        winsound.Beep(10000,1200)
                        pygame.time.delay(2400)
                        pygame.quit()

        else:
            ussi_saba.insert(0,[ussi_pea[0],ussi_pea[1]])
            if suund=="left":
                ussi_pea[0]-=segmendi_laius
            if suund=="right":
                ussi_pea[0]+=segmendi_laius
            if suund=="up":
                ussi_pea[1]-=segmendi_korgus
            if suund=="down":
                ussi_pea[1]+=segmendi_korgus
            if toidu_asukoht[0]==ussi_pea[0] and toidu_asukoht[1]==ussi_pea[1]:
                loo_uus_toit()
            else:
                ussi_saba.pop()
                
            #Kontrolli surma
            joonista_elemendid()
            if ussi_pea in ussi_saba or ussi_pea[0]>775 or ussi_pea[0]<0 or ussi_pea[1]>575 or ussi_pea[1]<0:  #TODO improve
                prindi_ekraanile("Get rekt, skrub.", must, -90, "keskmine")
                prindi_ekraanile("Pls nerf", must, -55, "väike")
                prindi_ekraanile("RIP in peace, autist", must, -15, "väike")
                pygame.display.update()
                winsound.Beep(10000,1200)
                pygame.time.delay(2400)
                pygame.quit()
            start=time.time()
            
            
        clock.tick(10)
        
            

#Taustamuss
pygame.mixer.music.load('HorstWesselLied.mp3')
pygame.mixer.music.play(-1, 0.0)


joonista_tutvustus()

ussi_pea=[pea_x,pea_y]
ussi_saba=[[pea_x+segmendi_laius,pea_y],[pea_x+2*segmendi_laius,pea_y],[pea_x+3*segmendi_laius,pea_y],[pea_x+4*segmendi_laius,pea_y]]
loo_uus_toit()
joonista_elemendid()

mangu_tsukkel()
