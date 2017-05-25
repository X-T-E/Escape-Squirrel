x = 400
y = 30
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame, sys, random, time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Squirrel Escape")

FPS = 40
clock = pygame.time.Clock()
timer = 0

player = pygame.image.load("resources/images/squirrel.png")
playerX, playerY = 326, 618
result = 0
nabbedPosX, nabbedPosY = 0, 0
nabbed =  None

hey = pygame.mixer.Sound("resources/audio/hey.wav")
pygame.mixer.music.load("resources/audio/music.wav")

enemyNorth = pygame.image.load("resources/images/enemynorth.png")
enemyEast = pygame.image.load("resources/images/enemyeast.png")
enemySouth = pygame.image.load("resources/images/enemysouth.png")
enemyWest = pygame.image.load("resources/images/enemywest.png")

direction = {
        "1" : "resources/images/enemynorth.png",
        "2" : "resources/images/enemyeast.png",
        "3" : "resources/images/enemysouth.png",
        "4" : "resources/images/enemywest.png"
    }

enemyGround = pygame.image.load("resources/images/ground2.jpg")
safeGround = pygame.image.load("resources/images/ground.jpg")

enemyOne = pygame.image.load("resources/images/enemywest.png")
enemyOneDirection = "4"

enemyTwo = pygame.image.load("resources/images/enemyeast.png")
enemyTwoDirection = "2"

enemyThree = pygame.image.load("resources/images/enemyeast.png")
enemyThreeDirection = "2"

enemyFour = pygame.image.load("resources/images/enemywest.png")
enemyFourDirection = "4"

def changeDirection():
    global enemyOne
    global enemyTwo
    global enemyThree
    global enemyFour

    global enemyOneDirection
    global enemyTwoDirection
    global enemyThreeDirection
    global enemyFourDirection
    
    x = random.randint(1,4)
    enemyOne =  pygame.image.load(direction[str(x)])
    enemyOneDirection = str(x)
    
    x = random.randint(1,4)
    enemyTwo =  pygame.image.load(direction[str(x)])
    enemyTwoDirection = str(x)

    x = random.randint(1,4)
    enemyThree =  pygame.image.load(direction[str(x)])
    enemyThreeDirection = str(x)

    x = random.randint(1,4)
    enemyFour =  pygame.image.load(direction[str(x)])
    enemyFourDirection = str(x)

    

gameIsRunning = 1


screen.fill((0,0,0))
for i in range(0,7):
    for j in range(0,7):
        if i%2 == 1:
            screen.blit(safeGround, (j*100, i*100))
        else:
            screen.blit(enemyGround, (j*100, i*100))
screen.blit(player, (playerX, playerY))
screen.blit(enemyOne, (630, 522))
screen.blit(enemyTwo, (4, 322))
screen.blit(enemyThree, (4, 122))
screen.blit(enemyFour, (630, 122))

fontObj = pygame.font.Font('resources/fonts/Gasalt.ttf', 50)

textSurfaceObj = fontObj.render("Get to the other " ,True,(255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (350, 350)
screen.blit(textSurfaceObj, textRectObj)

textSurfaceObj = fontObj.render("side without being spotted" ,True,(255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (350, 400)
screen.blit(textSurfaceObj, textRectObj)

pygame.display.flip()

time.sleep(3)

pygame.event.clear()
pygame.mixer.music.play(-1)
while gameIsRunning:

    screen.fill((0,0,0))
    
    for i in range(0,7):
        for j in range(0,7):
            if i%2 == 1:
                screen.blit(safeGround, (j*100, i*100))
            else:
                screen.blit(enemyGround, (j*100, i*100))
    screen.blit(player, (playerX, playerY))
     
    screen.blit(enemyOne, (630, 522))
    screen.blit(enemyTwo, (4, 322))
    screen.blit(enemyThree, (4, 122))
    screen.blit(enemyFour, (630, 122))

    if playerY == 518 and enemyOneDirection == "4":
        result = 0
        gameIsRunning = 0
        nabbedPosY = 522 - 50
        nabbedPosX = 580
        nabbed = pygame.image.load("resources/images/nabbedright.png")
        pygame.mixer.music.stop()
        hey.play()
    elif playerY == 318 and enemyTwoDirection == "2":
        result = 0
        gameIsRunning = 0
        nabbedPosY = 322 - 50
        nabbedPosX = 34
        nabbed = pygame.image.load("resources/images/nabbedleft.png")
        pygame.mixer.music.stop()
        hey.play()
    elif playerY == 118 and enemyThreeDirection == "2":
        result = 0
        gameIsRunning = 0
        nabbedPosY = 122 - 50
        nabbedPosX = 34
        nabbed = pygame.image.load("resources/images/nabbedleft.png")
        pygame.mixer.music.stop()
        hey.play()
    elif playerY == 118 and enemyFourDirection == "4":
        result = 0
        gameIsRunning = 0
        nabbedPosY = 122 - 50
        nabbedPosX = 580
        nabbed = pygame.image.load("resources/images/nabbedright.png")
        pygame.mixer.music.stop()
        hey.play()
    elif playerY == 18:
        pygame.mixer.music.stop()
        result = 1
        gameIsRunning = 0

    if timer >= 10:
        timer = 0
        changeDirection()

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYUP:
                if event.key == K_UP:
                    playerY -= 100
                    
    timer += 1
    pygame.display.update()
    clock.tick(FPS)

state = ""
if result == 1:
    state = "YOU WIN !!"
else:
    state = "YOU LOSE !!"
    screen.blit(nabbed, (nabbedPosX, nabbedPosY))
fontObj = pygame.font.Font('resources/fonts/Gasalt.ttf', 90)
textSurfaceObj = fontObj.render(state ,True,(0, 102, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (350, 350)
screen.blit(textSurfaceObj, textRectObj)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    
