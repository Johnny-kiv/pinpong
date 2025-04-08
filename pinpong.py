from random import Random

import pygame
import random
class enemy:
    def __init__(self,vector,x,color):
        self.vector = vector
        self.width = 60
        self.height = 10
        self.color = color
        self.x = x
        self.y = 50
    def walk(self):
        self.x+=self.vector
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
    def usl(self):
        if self.x < 0:
            self.vector = - self.vector
        if self.x > 340:
            self.vector = - self.vector
class hero:
    def __init__(self):
        self.color = "blue"
        self.x = 160
        self.y = 350
        self.width = 80
        self.height = 10
    def walk(self):
        pressed = pygame.key.get_pressed()
        if not self.x <= 30:
            if pressed[pygame.K_LEFT]: self.x -= 3
        if not self.x >= 290:
            if pressed[pygame.K_RIGHT]: self.x += 3
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
class ball:
    def __init__(self):
        self.color = "white"
        self.x = 200
        self.y = 200
        self.d = 10
        self.w = -1
        self.spy = 2
        self.tx = self.x
        self.ty = self.y
    def walk(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.d)
        if self.x == self.tx and self.y==self.ty:
            print("ye")
            self.tx,self.ty = self.generetion(self.w)
            self.w = -self.w
        print(self.x,self.tx)
        dx = self.x - self.tx

        dy = self.y - self.ty
        print(dx/dy * self.spy * self.w)
        if not dy==0:
            self.x+=dx/dy * self.spy * self.w * -1
        self.y +=self.spy *self.w
    def generetion(self,w):
        if w == 1:
            y= 400
        else:
            y=0
        x = random.randrange(31,269)
        return x,y
pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
done = False
en1 = enemy(-5,335,"red")
en2 = enemy(10,5,"orange")
h = hero()
b = ball()
b.generetion(0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    h.walk()
    b.walk()
    en1.walk()
    en1.usl()
    en2.walk()
    en2.usl()
    pygame.display.flip()
    clock.tick(60)
    screen.fill((0, 0, 0))