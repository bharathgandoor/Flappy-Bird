##import pygame
##pygame.init()
##screen=pygame.display.set_mode((1900,1060))
##pygame.display.set_caption("[name]")
##while True:
##    pygame.display.update()
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            exit()

import pygame, random
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Flappy Bird")
pillar_x = 750
pillar_1_height = random.randint(150,650)
pillar_2_y = pillar_1_height + 150
pillar_2_height = 800 - pillar_2_y
birby = 395
score = 0
def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj,(x,y))
while True:
    pillar1 = pygame.draw.rect(screen,(255,0,0),(pillar_x,0,25,pillar_1_height))
    pillar2 = pygame.draw.rect(screen,(255,0,0),(pillar_x,pillar_2_y,25,pillar_2_height))
    birb = pygame.draw.circle(screen,(0,255,0),(50,birby),10)
    pygame.display.update()
    screen.fill((0,0,0))
    pillar_x -= 3
    birby += 2
    if pillar_x <= 49:
        pillar_x = 800
        pillar_1_height = random.randint(150,650)
        pillar_2_y = pillar_1_height + 150
        pillar_2_height = 800 - pillar_2_y
        score += 1
    show_text("Score: " + str(score), 650, 10, (0,255,0))
    if birb.colliderect(pillar1) or birb.colliderect(pillar2):
        show_text("Game Over, your score is: " + str(score), 370, 384, (255,0,0))
        pygame.display.update()
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birby -= 40
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
