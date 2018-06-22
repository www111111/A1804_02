#import time 不用
import pygame

def main():
    #创建游戏窗口
    screen=pygame.display.set_mode((400,500),0,32)

    #把本地文件夹的图片，获取代码
    background=pygame.image.load('./images/background.png')
    hero = pygame.image.load('./images/hero1.png')

    #定义好位置和尺寸
    rect = pygame.Rect(150,350,100,124)
    #获取游戏时钟控制器
    clock = pygame.time.Clock()

    while True:
        #把 图片 加载到游戏窗口
        screen.blit(background,(0,0))#相对游戏窗口坐标(0,0)
        screen.blit(hero,rect)#相对游戏窗口坐标(0,0)

        #移动
        rect.x+=1
        rect.y-=2
        if rect.x>=400:
            rect.x=150
            rect.y=350
        if rect.y<=0:
            rect.y=350
            rect.x=150
        #刷新显示
        pygame.display.update()

        #延时显示
        #时间1/60秒
        clock.tick(60)
        #time.sleep(0.1)




'''
hero_rect = pygame.Rect(100, 500, 120, 126)
print("坐标原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄大小 %d %d" % (hero_rect.width, hero_rect.height))
# size 属性会返回矩形区域的 (宽, 高) 元组
print("英雄大小 %d %d" % hero_rect.size)
'''
#每个程序
#为了能够执行
if __name__ == '__main__':
    main()







