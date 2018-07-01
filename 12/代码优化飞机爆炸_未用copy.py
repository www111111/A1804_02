import pygame
import time
import random
from base01 import *


def main():
    #创建游戏窗口
    screen=pygame.display.set_mode((400,450),0,32)

    #把本地文件夹的图片，获取代码
    background=pygame.image.load('./images/background.png')

    #hero = pygame.image.load('./images/hero1.png')
    #rect = pygame.Rect(150,350,100,124)#尺寸

    clock = pygame.time.Clock()
    move_step = 10
    diren=Diji('./images/enemy1.png',screen,250,300)
    diren1=Diji('./images/enemy0.png',screen,250,300)
    hero=HeroPlane('./images/hero1.png',screen,0,0)
    while True:
        screen.blit(background,(0,0))#相对游戏窗口坐标(0,0)
        #judge_bao(hero,Bullet_f)
        diren.display()
        diren1.display()
        hero.display()
        #diren.auto_control()
       # key_control(diren,move_step)
        key_control(hero,diren,diren1,move_step)
        num = random.randint(1,150)# 为了使敌机的出弹速度降低
        if num == 5:
            diren.fire(hero)
            diren1.fire(hero)
#        for i in hero.bullet_list:#摧毁敌机
#            if diren.rect.y+124 >= i.y >= diren.rect.y and diren.rect.x +90 >= i.x >= diren.rect.x and i.y>0:
#                diren.bomb()
#            if diren1.rect.y+124 >= i.y >= diren1.rect.y and diren1.rect.x +90 >= i.x >= diren1.rect.x and i.y>0:
#                diren1.bomb()
#        for i in hero.bullet1_list:#摧毁敌机
#            if diren.rect.y+124 >= i.y >= diren.rect.y and diren.rect.x +90 >= i.x >= diren.rect.x and i.y>0:
#                diren.bomb()
#            if diren1.rect.y+124 >= i.y >= diren1.rect.y and diren1.rect.x +90 >= i.x >= diren1.rect.x and i.y>0:
#                diren1.bomb()
#        for i in diren.bullet_list:
#            if hero.rect.y+124 >= i.y >= hero.rect.y and hero.rect.x +90 >= i.x >= hero.rect.x and i.y>0:
#                hero.bomb()
#        for i in diren1.bullet_list:
#            if hero.rect.y+124 >= i.y >= hero.rect.y and hero.rect.x +90 >= i.x >= hero.rect.x and i.y>0:
#                hero.bomb()
        panduan(hero,diren,diren1)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()






