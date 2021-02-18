import pygame
import random
import math

pygame.mixer.init()

class game:

    class round:

        def __init__(self):
            self.level = 0
            self.starsCollected = 0
            self.messagesAmount = 0
            self.ypos = 20
            self.speech = [['I like you)!', 'I like your hair!)', 'You\'re so cute', 'I like what you are doing',
                            'I never met such a good person', 'I hope you live longer', 'This is actually cool!',
                            ')))', 'DONT COLLECT RED'],
                           ['This is weird', 'I feel something', 'I can understand you', 'I feel it',
                            'Have you hear this?', 'DONT COLLECT RED'],
                           ['He is behind me', 'He is GsdiauU', 'RED RED RED', 'HEEEEEEELP', 'DO SOMETHING',
                            'HE WILL KILL ME', 'DONT COLLECT RED'],
                           ['YOU LEFT ME THERE', 'LEFT ME IN HERE', 'BETRAYAL', 'HE KILLED ME', 'YOUR FAULT']]
            self.moneys = 0

        def saySomething(self, level):
            return self.speech[level][random.randint(0, len(self.speech[level])-1)]

        def dialog(self, display):
            self.ypos = 20
            turn = 1
            if self.level < 4:
                for message in range(10):
                    if turn == 1:
                        message = game.round.saySomething(self, self.level)
                        font1 = pygame.font.SysFont('chalkduster.ttf', 72)
                        img1 = font1.render(message, True, (255, 255, 255))
                        display.blit(img1, (5, self.ypos))
                        turn = 0
                    else:
                        pygame.draw.rect(display, (255, 255, 255), (random.randint(1700, 1940), self.ypos, 800, 20))
                        turn = 1
                    self.ypos += 60
                    pygame.time.delay(2000)
                    pygame.display.update()
            else:
                if self.moneys == 3:
                    sound = pygame.mixer.Sound('30140500_ghost_by_throneaudio_preview.mp3')
                    sound.play()
                    for message in range(15):
                        if turn == 1:
                            message = game.round.saySomething(self, self.level)
                            font1 = pygame.font.SysFont('chalkduster.ttf', 72)
                            img1 = font1.render(message, True, (255, 255, 255))
                            display.blit(img1, (5, self.ypos))
                            turn = 0
                        else:
                            pygame.draw.rect(display, (255, 255, 255), (random.randint(1700, 1940), self.ypos, 800, 20))
                            turn = 1
                        self.ypos += 60
                        pygame.time.delay(2000)
                        pygame.display.update()
                    sound = pygame.mixer.Sound('nmh_scream1.mp3')
                    sound.set_volume(5000)
                    sound.play()
                    pygame.time.delay(50000)
                    quit()
                else:
                    sound = pygame.mixer.Sound('nmh_scream1.mp3')
                    sound.set_volume(5000)
                    pygame.time.delay(50000)
                    sound.play()
                    quit()
            self.level += 1

    class miniGame:

        def __init__(self, height, width):

            self.background = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.money = (255, 0, 0)
            self.exit = (255, 255, 255)

            self.size = 10
            self.speed = self.size
            self.x = int(width/2)
            self.y = int(height/2)

            self.mx = random.randint(0, width)
            self.my = random.randint(0, height)

            self.ex = random.randint(0, width)
            self.ey = random.randint(0, height)

            self.moneyCollected = False
            self.run = True

        def returnPosToExit(self):
            if self.ex < self.x:
                xd = self.x - self.ex
            else:
                xd = self.ex - self.x
            if self.ey < self.y:
                yd = self.y - self.ey
            else:
                yd = self.ey - self.y
            distance = math.sqrt(xd**2+yd**2)
            return distance

        def returnPosToMoney(self):
            if self.mx < self.x:
                xd = self.x - self.mx
            else:
                xd = self.mx - self.x
            if self.my < self.y:
                yd = self.y - self.my
            else:
                yd = self.my - self.y
            distance = math.sqrt(xd**2+yd**2)
            return distance


        def Move(self, keys):
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed
            if keys[pygame.K_d]:
                self.x += self.speed

            posToExit = self.returnPosToExit()
            posToMoney = self.returnPosToMoney()

            if posToExit < self.size:
                self.run = False
            if posToMoney < self.size:
                self.moneyCollected = True


pygame.init()

displayWidth = 1920
displayHeight = 1080

display = pygame.display.set_mode((displayWidth, displayHeight))

font1 = pygame.font.SysFont('chalkduster.ttf', 72)
img1 = font1.render('hi sisters', True, (255, 255, 255))

gamre = game.round()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gamre.dialog(display)
    minigame = game.miniGame(displayHeight, displayWidth)
    while minigame.run != False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        minigame.Move(pygame.key.get_pressed())
        display.fill(minigame.background)
        pygame.draw.rect(display, minigame.color, (minigame.x, minigame.y, minigame.size, minigame.size))
        pygame.draw.rect(display, minigame.exit, (minigame.ex, minigame.ey, minigame.size, minigame.size))
        pygame.draw.rect(display, minigame.money, (minigame.mx, minigame.my, minigame.size, minigame.size))
        pygame.display.update()
    if minigame.moneyCollected == True:
        gamre.moneys += 1

    pygame.display.update()
    display.fill((0, 0, 0))
