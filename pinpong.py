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
        self.y = 50
        self.d = 10
        self.w = -1
        self.spx = 2
        self.spy = 2
    def walk(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.d)
        self.x+=self.spx
        self.y+=self.spy
    def usl(self,hx,enx):
        if self.x+self.d>=400 or self.x<=0:
            self.spx = -self.spx
        if self.y ==340 and (self.x>=hx and self.x<=hx+80):
            self.spy = -self.spy
        for i in enx:
            if self.y == 60 and (self.x >= i and self.x <= i + 60):
                self.spy = -self.spy
        if self.y<=0 or self.y>=400:
            self.spy = -self.spy
pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
done = False
en1 = enemy(-10,335,"red")
en2 = enemy(10,5,"orange")
h = hero()
b = ball()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    h.walk()
    b.walk()
    b.usl(h.x,[en1.x,en2.x])
    en1.walk()
    en1.usl()
    en2.walk()
    en2.usl()
    pygame.display.flip()
    clock.tick(60)
    screen.fill((0, 0, 0))