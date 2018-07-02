from game import *
import pygame
import random
def main():
     screen = pygame.display.set_mode((450,800),0,32)
     background = pygame.image.load('./images/background.png')

     hero_plane = Hero_plane(screen,'./images/hero.gif')

     dijiqun = Dijiqun(screen,'./images/enemy0.png')

     while True:
         if random.randint(1,100) == 8:
             dijiqun.add()      #间隔出现敌机
         screen.blit(background,(0,0))
         hero_plane.display()
         dijiqun.display(hero_plane) #显示敌机群
         key_control(hero_plane,3,dijiqun)
         pygame.display.update()


if __name__ == '__main__':
    main()

