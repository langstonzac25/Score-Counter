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
    
    
    display1score(score_1)
    display2score(score_2)
    
    determinendgameonewin()
    determinendgametwowin()
    endgame(endgamenow)
    
    
    pygame.display.flip()
    
    
pygame.quit()