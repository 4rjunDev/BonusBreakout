import sys, pygame
pygame.init()
pygame.key.set_repeat(10)
size = width, height = 640, 440
xspeed = 1
yspeed = 1
black = [0, 0, 0]
white = [255, 255, 255]
font = pygame.font.SysFont("Comic Sans", 40)
screen = pygame.display.set_mode(size)

renderedText2 = font.render("Gameover!",1,white)
renderedText3 = font.render("Press r to restart or q to quit",1,white)

paddle1 = pygame.Rect(320,420,70,10)
brick1 = pygame.Rect(0,100,64,20)
brick2 = pygame.Rect(65,100,64,20)
brick3 = pygame.Rect(130,100,64,20)
brick4 = pygame.Rect(195,100,64,20)
brick5 = pygame.Rect(260,100,64,20)
brick6 = pygame.Rect(325,100,64,20)
brick7 = pygame.Rect(390,100,64,20)
brick8 = pygame.Rect(455,100,64,20)
brick9 = pygame.Rect(520,100,64,20)
brick10 = pygame.Rect(585,100,64,20)
brick11 = pygame.Rect(35,77,64,20)
brick12 = pygame.Rect(100,77,64,20)
brick13 = pygame.Rect(165,77,64,20)
brick14 = pygame.Rect(230,77,64,20)
brick15 = pygame.Rect(295,77,64,20)
brick16 = pygame.Rect(360,77,64,20)
brick17 = pygame.Rect(425,77,64,20)
brick18 = pygame.Rect(490,77,64,20)
brick19 = pygame.Rect(555,77,64,20)
brick20 = pygame.Rect(620,77,64,20)

bricks = [brick1,brick2,brick3,brick4,brick5,brick6,brick7,brick8,brick9,brick10,brick11,brick12,brick13,brick14,brick15,brick16,brick17,brick18,brick19]

lives = 3

gameover = False

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ballrect.top = height/2 + 50
ballrect.left = height/2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle1.right = paddle1.right - 5
            elif keys[pygame.K_RIGHT]:
                paddle1.right = paddle1.right + 5

            if gameover:
                if keys[pygame.K_r]:
                    gameover = False
                    xspeed = 1
                    yspeed = 1
                    lives = 3
                if keys[pygame.K_q]:
                    pygame.quit()
                    sys.exit()


            
    ballrect.left = ballrect.left + xspeed
    ballrect.top = ballrect.top + yspeed
    
    if ballrect.colliderect(paddle1):
        yspeed = yspeed * -1.1

    if ballrect.left < 0 or ballrect.right > width:
        xspeed = xspeed * -1.01
        
    if ballrect.top < 0:
        yspeed = yspeed * -1.1

    if ballrect.bottom > 440:
        lives = lives - 1
        xspeed = 1
        yspeed = 1
        ballrect.bottom = height/2
    for b in bricks:
        if ballrect.colliderect(b):
            yspeed = yspeed * -1
            bricks.remove(b)

    if len(bricks)==0:
        gameover = True
        xspeed = 0
        yspeed = 0
        ballrect = ball.get_rect()
        ballrect.top = height/2 + 50
        ballrect.left = height/2
        bricks = [brick1,brick2,brick3,brick4,brick5,brick6,brick7,brick8,brick9,brick10,brick11,brick12,brick13,brick14,brick15,brick16,brick17,brick18,brick19]

    if lives == 0:
        gameover = True
        xspeed = 0
        yspeed = 0
        bricks = [brick1,brick2,brick3,brick4,brick5,brick6,brick7,brick8,brick9,brick10,brick11,brick12,brick13,brick14,brick15,brick16,brick17,brick18,brick19]

    screen.fill(black)
    
    if gameover:
        screen.blit(renderedText2,(220,height/2))
        screen.blit(renderedText3,(220,height/2+50))
    else: 
        screen.blit(ball, ballrect)
        pygame.draw.rect(screen,white,paddle1,0)
        for b in bricks:
            pygame.draw.rect(screen,white,b,0)
        renderedText = font.render("Lives: "+str(lives),1,white)
    
    screen.blit(renderedText, (width/2,4))
    pygame.display.flip()
    pygame.time.wait(10)
