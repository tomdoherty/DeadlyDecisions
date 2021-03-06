# import modules
import pygame
import pygame.freetype

pygame.init()

# Variables

Map1 = '''231CCC2331
WWWCCCWWWW
WWWCCCWWWW
CCCCCCCSCC
CCCCCCCCCC
CCCCCCCCCCC
FFFFFFFFFFF
BBBBBBBBBB'''


Map2 = '''333333333B
WWWWWWWWWB
WWWWWWWWWB
CCCCCCCCCB
CCCCCCCCCB
CCCCCCCCCB 
FFFFFFFFFB
BBBBBBBBBB'''


# W = wall F = floor
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
Map1 = Map1.splitlines()
Map2 = Map2.splitlines()
Map = Map1
GameTitle = pygame.image.load('Sprites/Menu/GameTitle.png')
Z = pygame.image.load("Sprites/Menu/Press _z_ to continue.png")
Skull = pygame.image.load('Sprites/Menu/Skull.png')
PlayerFront = pygame.image.load('Sprites/Player/Bill.png')
PlayerBack = pygame.image.load('Sprites/Player/Bill back.png')
PlayerRight = pygame.image.load('Sprites/Player/Bill right.png')
PlayerLeft = pygame.image.load('Sprites/Player/Bill left.png')
SlideOne = pygame.image.load('Sprites/Story/Slide1.png')
SlideTwo = pygame.image.load('Sprites/Story/Slide2.png')
SlideThree = pygame.image.load('Sprites/Story/Slide3.png')
SlideFour = pygame.image.load('Sprites/Story/Slide4.png')
SlideFive = pygame.image.load('Sprites/Story/Slide5.png')
Slay1 = pygame.mixer.Sound('SFX/Enemy slay.wav')
Walk1 = pygame.mixer.Sound('SFX/Walk.wav')
SlideOneAudio = pygame.mixer.Sound('SFX/STORY1.wav')
SlideTwoAudio = pygame.mixer.Sound('SFX/STORY2.wav')
SlideThreeAudio = pygame.mixer.Sound('SFX/STORY3.wav')
SlideFourAudio = pygame.mixer.Sound('SFX/STORY4.wav')
SlideFiveAudio = pygame.mixer.Sound('SFX/STORY5.wav')
Welcome = pygame.mixer.Sound('SFX/Welcome to my game.wav')
Menu = pygame.mixer.Sound('SFX/Deadly Decison.wav')
Font1 = pygame.freetype.Font("Fonts/Font1.ttf", 40)
Font2 = pygame.freetype.Font("Fonts/Bad Signal.otf", 40)
clock = pygame.time.Clock()
pressed = pygame.key.get_pressed()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Scene = "Story"
playerX = 236
playerY = 186
x = WINDOW_WIDTH
y = WINDOW_HEIGHT

# Title, Icon and Display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# The first one is X the second is Y
pygame.display.set_caption('Deadly decision')
icon = pygame.image.load('Sprites/Tiles/Brick.png')
pygame.display.set_icon(icon)
Scene = "Menu"


def intro():
    pygame.mixer.music.load('Music/Story OST 1.wav')
    pygame.mixer.music.play(-1)
    screen.blit(pygame.transform.scale(SlideOne, (412, 296)), (94, 50))
    text1, _ = Font1.render('People get lost in this game,', (255, 255, 255))
    text2, _ = Font1.render('       and never leave.', (255, 255, 255))
    screen.blit(text1, (100, 380))
    screen.blit(text2, (100, 430))
    pygame.display.update()
    SlideOneAudio.play()
    pygame.time.delay(5 * 1000)  # Time in milliseconds
    screen.fill([0, 0, 0])
    screen.blit(pygame.transform.scale(SlideTwo, (412, 296)), (94, 50))
    text1, _ = Font1.render('They never find a way out.', (255, 255, 255))
    screen.blit(text1, (120, 380))
    pygame.display.update()
    SlideTwoAudio.play()
    pygame.time.delay(5 * 1000)
    screen.fill([0, 0, 0])
    screen.blit(pygame.transform.scale(SlideThree, (412, 296)), (94, 50))
    text1, _ = Font1.render('At some point they die, as early', (255, 255, 255))
    text2, _ = Font1.render('          as a day or two.', (255, 255, 255))
    screen.blit(text1, (90, 380))
    screen.blit(text2, (90, 430))
    pygame.display.update()
    SlideThreeAudio.play()
    pygame.time.delay(5 * 1000)
    screen.fill([0, 0, 0])
    screen.blit(pygame.transform.scale(SlideFour, (412, 296)), (94, 50))
    text1, _ = Font1.render('the reason why is unknown.', (255, 255, 255))
    screen.blit(text1, (120, 380))
    pygame.display.update()
    SlideFourAudio.play()
    pygame.time.delay(5 * 1000)
    screen.fill([0, 0, 0])
    screen.blit(pygame.transform.scale(SlideFive, (412, 296)), (94, 50))
    text1, _ = Font1.render('But i think we are close to', (255, 255, 255))
    text2, _ = Font1.render('           finding out.', (255, 255, 255))
    screen.blit(text1, (100, 380))
    screen.blit(text2, (100, 430))
    pygame.display.update()
    SlideFiveAudio.play()
    pygame.time.delay(5 * 1000)
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Music/Menu OST 2.wav')
    pygame.mixer.music.play(-1)
    Menu.play()


def tiles(input_map):
    global Wall
    global Water
    global Floor
    global Floor2
    global One
    global Two
    global Three
    global Blank
    global Sign
    for y, line in enumerate(input_map):
        for x, character in enumerate(line):
            if character == 'W':
                screen.blit(pygame.transform.scale(Wall, (64, 64)), (x * 64, y * 64))
            if character == 'F':
                screen.blit(pygame.transform.scale(Floor, (64, 64)), (x * 64, y * 64))
            if character == 'C':
                screen.blit(pygame.transform.scale(Floor2, (64, 64)), (x * 64, y * 64))
            if character == 'A':
                screen.blit(pygame.transform.scale(Water, (64, 64)), (x * 64, y * 64))
            if character == '1':
                screen.blit(pygame.transform.scale(One, (64, 64)), (x * 64, y * 64))
            if character == '2':
                screen.blit(pygame.transform.scale(Two, (64, 64)), (x * 64, y * 64))
            if character == '3':
                screen.blit(pygame.transform.scale(Three, (64, 64)), (x * 64, y * 64))
            if character == 'B':
                screen.blit(pygame.transform.scale(Blank, (64, 64)), (x * 64, y * 64))
            if character == 'S':
                screen.blit(pygame.transform.scale(Sign, (64, 64)), (x * 64, y * 64))


def init_display():
    global screen, Wall
    global screen, Water
    global screen, Floor
    global screen, Floor2
    global screen, One
    global screen, Two
    global screen, Three
    global screen, Blank
    global screen, Sign
    Wall = pygame.image.load('Sprites/Tiles/Brick.png')
    Water = pygame.image.load('Sprites/Tiles/Water.png')
    Floor = pygame.image.load('Sprites/Tiles/Floor.png')
    Floor2 = pygame.image.load('Sprites/Tiles/Floor2.png')
    One = pygame.image.load('Sprites/Tiles/Tile1.png')
    Two = pygame.image.load('Sprites/Tiles/Tile2.png')
    Three = pygame.image.load('Sprites/Tiles/Tile3.png')
    Blank = pygame.image.load('Sprites/Tiles/Tile4.png')
    Sign = pygame.image.load('Sprites/Tiles/Sign.png')


# loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if Scene == "Menu":
        intro()
        screen.fill([0, 0, 0])
        screen.blit(pygame.transform.scale(GameTitle, (590, 30)), (5, 15))
        screen.blit(pygame.transform.scale(Z, (262, 20)), (169, 430))
        pygame.display.update()

        if pressed[pygame.K_z]:
            Welcome.play()
            pygame.time.delay(2 * 1000)
            screen.fill([0, 0, 0])
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.time.delay(3 * 1000)
            Scene = "Game"
            init_display()
            Slay1.play()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Music/HallowHalls OST 3.wav')
            pygame.mixer.music.play(-1)
            screen.fill([0, 0, 0])
            tiles(Map1)
            screen.blit(pygame.transform.scale(PlayerFront, (64, 64)), (playerX, playerY))
            pygame.display.update()

    if Scene == "Game":
        if pressed[pygame.K_w]:
            if Map == Map2 and playerY <= 145:
                playerY += 4
            if Map == Map1:
                if playerX <= 180 and playerY <= 145:
                    playerY += 4
                if playerX >= 332 and playerY <= 145:
                    playerY += 4
            screen.fill([0, 0, 0])
            playerY -= 4
            tiles(Map)
            screen.blit(pygame.transform.scale(PlayerBack, (64, 64)), (playerX, playerY))
            pygame.display.update()
        if pressed[pygame.K_s]:
            if Map == Map1 or Map2:
                if playerY >= 355:
                    playerY -= 4
            screen.fill([0, 0, 0])
            playerY += 4
            tiles(Map)
            screen.blit(pygame.transform.scale(PlayerFront, (64, 64)), (playerX, playerY))
            pygame.display.update()
        if pressed[pygame.K_d]:
            if Map == Map1:
                if playerX >= 600:
                    Map = Map2
                    tiles(Map)
                    playerX = 4
                    pygame.display.update()
                if playerX >= 332 and playerY <= 145:
                    playerX -= 4
            screen.fill([0, 0, 0])
            playerX += 4
            tiles(Map)
            screen.blit(pygame.transform.scale(PlayerRight, (64, 64)), (playerX, playerY))
            pygame.display.update()
        if pressed[pygame.K_a]:
            if Map == Map2:
                if playerX <= 0:
                    Map = Map1
                    tiles(Map)
                    playerX = 595
                    pygame.display.update()
            if Map == Map1:
                if playerX <= 180 and playerY <= 145:
                    playerX += 4
            screen.fill([0, 0, 0])
            playerX -= 4
            tiles(Map)
            screen.blit(pygame.transform.scale(PlayerLeft, (64, 64)), (playerX, playerY))
            pygame.display.update()