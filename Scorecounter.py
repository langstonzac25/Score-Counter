#load modules
import pygame
from pygame.locals import *



pygame.init()

clock = pygame.time.Clock()
fps = 20

#screen dimmensions
screen_width = 900
screen_height = 579

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Score Counter')



#load images
table = pygame.image.load("Images/pingpongtablefinal.png")
ball = pygame.image.load("Images/pingpongball.png")

#initial picture processing
screen.blit(table,(0, 0))
screen.blit(ball,(225, 289))
pygame.display.flip()


event = pygame.event.wait()
if event.type == KEYDOWN:
    if event.key == K_SPACE:
        screen.blit(ball, (0, 0))


#My varibles
global spawnballleft
spawnballleft = 0
global spawnballright
spawnballright = 0
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

#find the users name
global userName1
userName1 = input("Who is the first competitor?         ")
global userName2
userName2 = input("Who is the second competitor?        ")

print ("")
print ("")
print ("When inputing who got the point please use the numbers 1 and 2.")
print ("")
print ("")


#find who won
def whogotpoint():
    global pointadd
    pointadd = int(input("Who got the point?        "))


#add the players points
def addplayeronepoint(who1):
    if who1 == 1:
        global score_1
        score_1 = score_1 + 1

def addplayertwopoint(who2):
    if who2 == 2:
        global score_2
        score_2 = score_2 + 1


#display the scores    
def display1score(sc1):
    print (userName1)
    print (sc1)  
    
def display2score(sc2):
    print (userName2)
    print (sc2)
    
    
#Determine who shold serve
def whoistheserver(sc1, sc2):
    total = sc1 + sc2
    global spawnballleft
    global spawnballright
    if total == 0:
        spawnballleft = 1
    if total == 1:
        spawnballleft = 1
    if total == 2:
        spawnballright = 1
    if total == 3:
        spawnballright = 1
    if total == 4:
        spawnballleft = 1
    if total == 5:
        spawnballleft = 1
    if total == 6:
        spawnballright = 1
    if total == 7:
        spawnballright = 1
    if total == 8:
        spawnballleft = 1
    if total == 9:
        spawnballleft = 1
    if total == 10:
        spawnballright = 1
    if total == 11:
        spawnballright = 1
    if total == 12:
        spawnballleft = 1
    if total == 13:
        spawnballleft = 1
    if total == 14:
        spawnballright = 1
    if total == 15:
        spawnballright = 1
    if total == 16:
        spawnballleft = 1
    if total == 17:
        spawnballleft = 1
    if total == 18:
        spawnballright = 1
    if total == 19:
        spawnballright = 1
    if total == 20:
        spawnballleft = 1
    if total == 21:
        spawnballleft = 1
    if total == 22:
        spawnballright = 1
    if total == 23:
        spawnballright = 1
    if total == 24:
        spawnballleft = 1
    if total == 25:
        spawnballleft = 1
    if total == 26:
        spawnballright = 1
    if total == 27:
        spawnballleft = 1
    if total == 28:
        spawnballleft = 1
    if total == 29:
        spawnballright = 1
    if total == 30:
        spawnballright = 1


#spawn balls
def spawnballl(spawnl):
    if spawnl == 1:
        screen.blit(table,(0, 0))
        screen.blit(ball,(225, 289))

def spawnballr(spawnr):
    if spawnr == 1:
        screen.blit(table,(0, 0))
        screen.blit(ball,(675, 289))


#Did the game end?
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


#The end of the game
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


#Main Loop
run = 1
while run == 1: 
    
    clock.tick(fps)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    #get keypresses
#    event = pygame.event.wait()
#   if event.type == KEYDOWN:
#       if event.key == K_SPACE:
#           screen.blit(ball, (0, 0))
            
    
    
    whogotpoint()
    
    addplayeronepoint(pointadd)
    addplayertwopoint(pointadd)
    
    whoistheserver(score_1, score_2)
    
    spawnballl(spawnballleft)
    spawnballr(spawnballright)
    spawnballleft = 0
    spawnballright = 0
    
    display1score(score_1)
    display2score(score_2)
    
    determinendgameonewin()
    determinendgametwowin()
    endgame(endgamenow)
    
    
    pygame.display.flip()
    
    
pygame.quit()
