import pygame
import time
import random
from base01 import *

def main():
    #创建游戏窗口
    screen=pygame.display.set_mode((400,450),0,32)

    #把本地文件夹的图片，获取代码
    background=pygame.image.load('./images/background.png')

    clock = pygame.time.Clock()
    move_step = 10
    diren=Diji('./images/enemy1.png',screen,250,300)
    diren1=Diji('./images/enemy1.png',screen,250,300)
    hero=HeroPlane('./images/hero1.png',screen,0,0)
    while True:
        screen.blit(background,(0,0))#相对游戏窗口坐标(0,0)
        #judge_bao(hero,Bullet_f)
        #diren.display()
        #diren1.display()
        hero.display()
        key_control(hero,diren,diren1,move_step)
        num = random.randint(1,150)# 为了使敌机的出弹速度降低
        if num == 5:
            diren.fire(hero)
            diren1.fire(hero)
        panduan(hero,diren,diren1)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()






