import pygame
from pygame.locals import *



pygame.init()

clock = pygame.time.Clock()
fps = 20


screen_width = 900
screen_height = 579

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Score Counter')

surface = pygame.display.set_mode((screen_width, screen_height))
#blue = (0, 0, 255)


#load images
table = pygame.image.load("Images\pingpongtablefinal.png")
ball = pygame.image.load("Images/pingpongball.png")


screen.blit(table,(0, 0))
screen.blit(ball,(0, 0))
pygame.display.flip()


#My varibles
global endgamenow
endgamenow = 0
global pointadd
pointadd = 0
global endgame
endgame = 0
global score_1
score_1 = 0
global score_2
score_2 = 0
global server
server = 1

global userName1
userName1 = input("Who is the first competitor?         ")
global userName2
userName2 = input("Who is the second competitor?        ")

print ("")
print ("")
print ("When inputing who got the point please use the numbers 1 and 2.")
print ("")
print ("")



def whogotpoint():
    global pointadd
    pointadd = int(input("Who got the point?        "))
    
def addplayeronepoint(who1):
    if who1 == 1:
        global score_1
        score_1 = score_1 + 1

def addplayertwopoint(who2):
    if who2 == 2:
        global score_2
        score_2 = score_2 + 1
                        
    
def display1score(sc1):
    print (userName1)
    print (sc1)


def display2score(sc2):
    print (userName2)
    print (sc2)

#Determine who shold serve
def whoistheserver(sc1, sc2):
    total = sc1 + sc2
    print(sc1 + sc2)
    if total == 1:
        print("odd")
    if total == 2:
        print("even")
    if total == 3:
        print("odd")
    if total == 4:
        print("even")
    if total == 5:
        print("odd")
    if total == 6:
        print("even")
    if total == 7:
        print("odd")
    if total == 8:
        print("even")
    if total == 9:
        print("odd")
    if total == 10:
        print("even")
    if total == 11:
        print("odd")
    if total == 12:
        print("even")
    if total == 13:
        print("odd")
    if total == 14:
        print("even")
    if total == 15:
        print("odd")
    if total == 16:
        print("even")
    if total == 17:
        print("odd")
    if total == 18:
        print("even")
    if total == 19:
        print("odd")
    if total == 20:
        print("even")
    if total == 21:
        print("odd")
    if total == 22:
        print("even")
    if total == 23:
        print("odd")
    if total == 24:
        print("even")
    if total == 25:
        print("odd")
    if total == 26:
        print("even")
    if total == 27:
        print("odd")
    if total == 28:
        print("even")
    if total == 29:
        print("odd")
    if total == 30:
        print("even")

    
def determinendgameonewin():
    global endgamenow
    if score_1 >= 11:
        if score_1 - score_2 >= 2:
            endgamenow = 1

def determinendgametwowin():
    global endgamenow
    if score_2 >= 11:
        if score_2 - score_1 >= 2:
            endgamenow = 1
    
def endgame(endgamenowfun):
    if endgamenowfun == 1:
        global run
        run = int(input("To play again type 1. To quit type any other number:   "))
        global score_1
        score_1 = 0
        global score_2
        score_2 = 0
        global endgamenow
        endgamenow = 0

run = 1
while run == 1: 
    
    clock.tick(fps)
    
    screen.blit(ball, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_1]:
        print ("key 1 pressed.")
    if key[pygame.K_2]:
        print ("hello")
    
    
    
    whogotpoint()
    
    addplayeronepoint(pointadd)
    addplayertwopoint(pointadd)
    
    whoistheserver(score_1, score_2)
    
    display1score(score_1)
    display2score(score_2)
    
    determinendgameonewin()
    determinendgametwowin()
    endgame(endgamenow)
    
    
    pygame.display.flip()
    
    
pygame.quit()