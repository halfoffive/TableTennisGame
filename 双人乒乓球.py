import pygame,time,win32com.client
pygame.init()
o = False
oa = True
screen = pygame.display.set_mode([800,600])
s = win32com.client.Dispatch("SAPI.SpVoice")
pygame.display.set_caption("双人乒乓球 10.1.2")
keepGoing = True
pic = pygame.image.load("球 - 副本.bmp")
pop = pygame.mixer.Sound("pop - 副本.wav")
an = pygame.image.load("1 - 副本.bmp")
sbt = False
b = True
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
colorkey = an.get_at((0,0))
an.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
timer = pygame.time.Clock()
speedx = 5
speedy = 5
paddlew = 200
paddleh = 25
paddlex = 300
paddley = 550
picw = 46
pich = 46
points = 0
lives = 5
k = True
cs = ""
font = pygame.font.SysFont("simHei", 24)
def djs():
    fonts = pygame.font.SysFont("simHei", 100)
    djsz = ("321")
    for djsx in djsz:
        screen.fill(BLACK)
        djst = fonts.render(djsx, True, WHITE)
        text_rect = djst.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 280
        screen.blit(djst, text_rect)
        pygame.display.update()
        s.Speak(djsx)
        time.sleep(0)
    screen.fill(BLACK)
    djst = fonts.render("开始", True, WHITE)
    text_rect = djst.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 280
    screen.blit(djst, text_rect)
    pygame.display.update()
    s.Speak("开始")
screen.fill(BLACK)
while k:
    screen.fill(BLACK)
    screen.blit(an, (300, 250))
    pygame.display.update()
    c = True
    while c:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False
                k = False
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    if b:
                        BLACK = (255,255,255)
                        WHITE = (0,0,0)
                        screen.fill(BLACK)
                        screen.blit(an, (300, 250))
                        pygame.display.update()
                        b = False
                    elif not b:
                        BLACK = (0,0,0)
                        WHITE = (255,255,255)
                        screen.fill(BLACK)
                        screen.blit(an, (300, 250))
                        pygame.display.update()
                        b = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 300 and x < 500 and y > 250 and y < 350:
                    c = False
                    keepGoing = True
                    o = False
                    oa = True
                    c = False
                    keepGoing = True
                    points = 0
                    lives = 5
                    picx = 0
                    picy = 100
                    speedx = 5
                    speedy = 5
                    djs()
    while keepGoing:
        pax = picx-100
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1 and o:
                    keepGoing = False
                if event.key == pygame.K_F2:
                    if b:
                        BLACK = (255,255,255)
                        WHITE = (0,0,0)
                        b = False
                    elif not b:
                        BLACK = (0,0,0)
                        WHITE = (255,255,255)
                        b = True
        picx += speedx
        picy += speedy
        if picx <= 0 or picx >= 754:
            speedx = -speedx * 1.1
            pop.play()
        if picy <= 75:
            speedy = -speedy + 1
            pop.play()
        if picy >= 554:
            lives -= 1
            speedy = -5
            speedx = 5
            picy = 499
            cs = "Lives -1"
            pop.play()
        screen.fill(BLACK)    
        screen.blit(pic, (picx, picy))
        paddlex = pygame.mouse.get_pos()[0]
        #将下面的“#”去掉，可实现AI互打，但速度过快会出现BUG.
        #paddlex = picx
        paddlex -= paddlew/2
        pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))
        pygame.draw.rect(screen, WHITE, (pax,50,paddlew,paddleh))
        if picy + pich >= paddley and picy + pich <= paddley + paddleh \
           and speedy > 0:
            if picx + picw/2 >= paddlex and picx + picw/2 <= paddlex + \
               paddlew:
                speedy = -speedy
                points += 1
                cs = "Points +1"
                pop.play()
        draw_string = "生命值: " + str(lives) + " 分数: " + str(points)
        if lives < 1:   
            speedx = speedy = 0
            draw_string = "游戏结束。你的得分为：" + str(points)
            draw_string += "。按F1返回主页。"
            o = True
        text = font.render(draw_string, True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 10
        screen.blit(text, text_rect)
        pygame.display.update()
        if o and oa:
            s.Speak(draw_string)
            oa = False
        timer.tick(60)
pygame.quit()
