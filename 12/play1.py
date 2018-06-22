import pygame

def main():
    #创建游戏窗口
    screen=pygame.display.set_mode((400,500),0,32)

    #把本地文件夹的图片，获取代码
    background=pygame.image.load('./images/background.png')
    hero = pygame.image.load('./images/hero1.png')

    #把 图片 加载到游戏窗口
    screen.blit(background,(0,0))#相对游戏窗口坐标(0,0)
    screen.blit(hero,(150,350))#相对游戏窗口坐标(0,0)

    #刷新显示

    pygame.display.update()

    #防止一闪而退
    while True:
        pass



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







