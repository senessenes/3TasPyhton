import pygame
import os
import math
pygame.init()
sayi=0

BG=pygame.image.load(os.path.join("Assets", "background.jpg"))
BEYAZ_PUL_IMAGE=pygame.image.load(os.path.join("Assets", "png.png"))
SIYAH_PUL_IMAGE=pygame.image.load(os.path.join("Assets", "siyahpul.png"))

text = ''
font = pygame.font.SysFont("calibri.ttf", 48)
img = font.render(text, True, (255,0,0))

rect = img.get_rect()
WIDTH,HEIGHT=700,700
board=[["_","_","_"],
       ["_","_","_"],
        ["_","_","_"]]


sira="b"
kazanan=""
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("3 Tas")

pul_pozisyonlari=[
    [[50,50],[315,50],[550,50]],
    [[50,315],[315,315],[550,315]],
    [[50,580],[315,580],[550,580]]
]
siyah_pullar=[]
beyaz_pullar=[]


START_BEYAZ_X,START_BEYAZ_Y=450,200

START_SIYAH_X,START_SIYAH_Y=450,200
def pul():

    if(sira=="b"):
        return BEYAZ_PUL_IMAGE
    if(sira=="s"):
        return SIYAH_PUL_IMAGE
def possible_moves_once(board):
    moves=[]


    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(move_possible([i+1,j+1],0)==True):
                moves.append([i+1,j+1])
    return moves





beyaz_pul_pozisyonlari=[]
siyah_pul_pozisyonlari=[]
def drawScreen():




    WIN.blit(BG,(0,0))
    for i in range(0, len(beyaz_pullar)):
        WIN.blit(beyaz_pullar[i], tuple(beyaz_pul_pozisyonlari[i]))
    for i in range(0, len(siyah_pullar)):
        WIN.blit(siyah_pullar[i], tuple(siyah_pul_pozisyonlari[i]))
    if (kazanan == "b"):
        text = "Beyaz Kazandı"
        img = font.render(text, True, (255, 0, 0))
        WIN.blit(img, (250, 20))

    elif (kazanan == "s"):

        text = "Siyah Kazandı"
        img = font.render(text, True, (255, 0, 0))
        WIN.blit(img, (250, 20))





    pygame.display.update()


def is_finished(board):
    global kazanan
    columns=[[board[0][0],board[1][0],board[2][0]],[board[0][1],board[1][1],board[2][1]],[board[0][2],board[1][2],board[2][2]]]
    for i in columns:
        if i==["b","b","b"]:
            kazanan="b"
            return True
        elif i==["s","s","s"]:
            kazanan="s"
            return True
    for i in board:
        if i==["b","b","b"]:
            kazanan="b"
            return True
        elif i==["s","s","s"]:
            kazanan="s"
            return True
    return False









def move_possible(yer,tas):
    if(tas==0):
        if (not (icindemi(pul_pozisyonlari[int(yer[0]) - 1][int(yer[1]) - 1], beyaz_pul_pozisyonlari)) and not (icindemi(pul_pozisyonlari[int(yer[0]) - 1][int(yer[1]) - 1], siyah_pul_pozisyonlari))):
            return True
        return False
    else:
        if(abs(int(yer[0])-int(tas[0]))>1 or abs(int(yer[1])-int(tas[1]))>1):
            return False
        elif (abs(int(yer[0]) - int(tas[0])) > 0 and abs(int(yer[1]) - int(tas[1])) > 0):
            return False
        else:
            if (not (icindemi(pul_pozisyonlari[int(yer[0]) - 1][int(yer[1]) - 1], beyaz_pul_pozisyonlari)) and not (icindemi(pul_pozisyonlari[int(yer[0]) - 1][int(yer[1]) - 1], siyah_pul_pozisyonlari))):

                return True

            return False







def icindemi(array1,array2):
    for i in array2:
        for j in i:
            if j==array1:
                return True
    return False
def main():
    secili=False
    yer=[]
    tas=[]
    pygame.init()
    run = True
    global sira
    clock=pygame.time.Clock()
    clock.tick(60)



    while run:




        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                run = False
            if event.type== pygame.MOUSEBUTTONUP:
                if(is_finished(board)==False):
                    enyakin=[0,0]
                    for i in range(0,len(pul_pozisyonlari)):
                        for j in range(0,len(pul_pozisyonlari[i])):
                            if math.dist(pul_pozisyonlari[i][j],list(pygame.mouse.get_pos()))<math.dist(pul_pozisyonlari[enyakin[0]][enyakin[1]],list(pygame.mouse.get_pos())):
                                enyakin=[i,j]
                    if(sira=="b"):
                        if(len(beyaz_pullar)<3):
                            yer=enyakin

                            if(move_possible([yer[0]+1,yer[1]+1],0)):
                                beyaz_pul_pozisyonlari.append([pul_pozisyonlari[int(yer[0])][int(yer[1])]])

                                beyaz_pullar.append(pul())
                                board[int(yer[0])][int(yer[1])] = "b"

                                sira = "s"

                        else:
                            if(secili)==False:
                                tas=enyakin
                                secili=True
                            else:
                                yer=enyakin

                                if (move_possible([yer[0] + 1, yer[1] + 1], [tas[0]+1,tas[1]+1])):
                                    for i in range(0, len(beyaz_pul_pozisyonlari)):
                                        for j in beyaz_pul_pozisyonlari[i]:
                                            if j == pul_pozisyonlari[int(tas[0])][int(tas[1])]:
                                                beyaz_pul_pozisyonlari[i][0] = pul_pozisyonlari[int(yer[0])][
                                                int(yer[1])]
                                                board[int(yer[0])][int(yer[1])], board[int(tas[0])][
                                                    int(tas[1])] = board[int(tas[0])][int(tas[1])], \
                                                                           board[int(yer[0])][int(yer[1])]

                                                sira = "s"
                                    secili=False
                    elif(sira=="s") and is_finished(board)==False:
                        if (len(siyah_pullar) < 3):
                            yer = enyakin

                            if (move_possible([yer[0] + 1, yer[1] + 1], 0)):
                                siyah_pul_pozisyonlari.append([pul_pozisyonlari[int(yer[0])][int(yer[1])]])

                                siyah_pullar.append(pul())
                                board[int(yer[0])][int(yer[1])] = "s"


                                sira = "b"

                        else:
                            if (secili) == False:
                                tas = enyakin
                                secili = True
                            else:
                                yer = enyakin

                                if (move_possible([yer[0] + 1, yer[1] + 1], [tas[0] + 1, tas[1] + 1])):
                                    for i in range(0, len(beyaz_pul_pozisyonlari)):
                                        for j in siyah_pul_pozisyonlari[i]:
                                            if j == pul_pozisyonlari[int(tas[0])][int(tas[1])]:
                                                siyah_pul_pozisyonlari[i][0] = pul_pozisyonlari[int(yer[0])][
                                                    int(yer[1])]
                                                board[int(yer[0])][int(yer[1])], board[int(tas[0])][
                                                    int(tas[1])] = board[int(tas[0])][int(tas[1])], \
                                                                   board[int(yer[0])][int(yer[1])]

                                                sira = "b"
                                    secili = False

                    is_finished(board)
        drawScreen()

















    pygame.quit()














if __name__=="__main__":
    main()

