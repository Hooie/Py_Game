import pygame
import sys
from time import sleep
import random

padWidth = 480
padHeight = 640
enemyImage = ['images/enemy1.png', 'images/enemy2.png', 'images/enemy3.png']
explosionSound = ['sounds/boom1.wav', 'sounds/boom2.wav','sounds/boom3.wav']

rock1Width = 10
rock1Height = 35
rock2Width = 20
rock2Height = 20 

def textObj(text, font):
    textSurface = font.render(text, True, (255,0,0))
    return textSurface, textSurface.get_rect()

def dispMessage(text):
    global gamePad, gameOverSound

    largeText = pygame.font.Font('freesansbold.ttf', 75)
    TextSurf, TextRect = textObj(text, largeText)
    TextRect.center = ((padWidth/2),(padHeight/2))
    gamePad.blit(TextSurf, TextRect)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameOverSound.play()
    sleep(3)
    pygame.mixer.music.play(-1)
    runGame()

def crash():
    global gamePad
    dispMessage('Crashed!')


def gameOver():
    global gamePad
    dispMessage('GAME OVER!')

#적 처치 수
def writeScore(count):
    global gamePad
    font = pygame.font.SysFont(None, 25)
    text = font.render('Enemy Defeated:' + str(count), True, (255, 255, 255))
    gamePad.blit(text,(10,0))

#통과한 적 수
def writePassed(count):
    global gamePad
    font = pygame.font.SysFont(None, 25)
    text = font.render('Enemy Passed:' + str(count), True, (255,0,0))
    gamePad.blit(text,(335,0))

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x,y))

def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound, rocks

    rocks = []
    
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Space War')
    background = pygame.image.load('image/background.png')
    fighter = pygame.image.load('image/ship.png')
    missile = pygame.image.load('image/missile1.png')
    explosion = pygame.image.load('image/boom.png')
    pygame.mixer.music.load('sounds/bgm.wav')
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('sounds/missile.wav')
    gameOverSound = pygame.mixer.Sound('sounds/gameover.wav')
    rocks.append((0, pygame.image.load('image/rock1.png')))
    rocks.append((1, pygame.image.load('image/rock2.png')))

    for i in range(3):
        rocks.append((i+2, None))
    
    clock = pygame.time.Clock()                           

def runGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound
    global enemy, rocks

    isShot = False
    shotCount = 0
    enemyPassed = 0

    
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0] + 5
    fighterHeight = fighterSize[1] + 5

    x = padWidth * 0.45
    y = padHeight * 0.85
    fighterX = 0

    rockX = random.randrange(0, padWidth)
    rockY = 0
    random.shuffle(rocks)
    rock = rocks[0]

    missileXY = []



    #적 랜덤 생성
    enemy = pygame.image.load(random.choice(enemyImage))
    enemySize = enemy.get_rect().size
    enemyWidth = enemySize[0]
    enemyHeight = enemySize[1]
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))
    
    #적 초기 위치 설정
    enemyX = random.randrange(0, padWidth - enemyWidth)
    enemyY = 0
    enemySpeed = 2

    rockSpeed = 7
    
    onGame = False

    #키 이벤트 설정
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT:
                    fighterX += 5

                elif event.key == pygame.K_SPACE:
                    missileSound.play()
                    missileX = x + fighterWidth /2
                    missileY = y - fighterHeight
                    missileXY.append([missileX,missileY])

                elif event.key == pygame.K_LCTRL:
                    sleep(3)
                    
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0
                    
        #배경 그리기
        drawObject(background, 0, 0)

        #우주선 위치 제한
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        #전투기가 적과 충돌하는지 확인
        if y < enemyY + enemyHeight:
            if(enemyX > x and enemyX < x + fighterWidth) or (enemyX + enemyWidth > x and enemyX + enemyWidth < x + fighterWidth):
                crash()

        #전투기가 운석과 충돌하는지 확인
        if rock[1] != None:
            if rock[0] == 0:
                rockWidth = 25
                rockHeight = 20
            else:
                rockWidth = 25
                rockHeight = 20

            if y < rockY + rockHeight:
                if(rockX > x and rockX < x + fighterWidth) or (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
                    crash()

        
            
        #우주선 그리기
        drawObject(fighter, x, y)

        #미사일 추가하기
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                if bxy[1] < enemyY:
                    if bxy[0] > enemyX and bxy[0] < enemyX + enemyWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
                    
        #미사일 그리기
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        writeScore(shotCount)
        
        #운석 위치
        if rock[1] == None:
            rockY += 7
        else:
            rockY += 3

        if rockY > padHeight:
            rockY = 0
            rockX = random.randrange(0, padWidth)
            random.shuffle(rocks)
            rock = rocks[0]

        #적 아래로
        enemyY += enemySpeed

        if enemyY > padHeight:
            enemy = pygame.image.load(random.choice(enemyImage))
            enemySize = enemy.get_rect().size
            enemyWIdth = enemySize[0]
            enemyHeight = enemySize[1]
            enemyX = random.randrange(0, padWidth - enemyWidth)
            enemyY = 0
            enemyPassed += 1

        if enemyPassed == 5:
            gameOver()
        
        writePassed(enemyPassed)

        #적이 미사일을 맞았다면
        if isShot:
            drawObject(explosion, enemyX, enemyY)
            destroySound.play()

            enemy = pygame.image.load(random.choice(enemyImage))
            enemySize = enemy.get_rect().size
            enemyWidth = enemySize[0]
            enemyHeight = enemySize[1]
            enemyX = random.randrange(0, padWidth - enemyWidth)
            enemyY = 0
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))
            isShot = False

            enemySpeed += 0.1
            if enemySpeed >= 10:
                enemySpeed = 10

        drawObject(enemy, enemyX, enemyY)
        

        if rock[1] != None:
            drawObject(rock[1], rockX, rockY)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

    
initGame()
runGame()
