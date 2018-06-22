import pygame

def main():
    #创建游戏窗口
    screen=pygame.display.set_mode((400,500),0,32)

    #把本地文件夹的图片，获取代码
    background=pygame.image.load('./images/background.png')
    hero = pygame.image.load('./images/hero1.png')

    #定义好位置和尺寸
    rect = pygame.Rect(150,350,100,124)#尺寸
    #获取游戏时钟控制器
    clock = pygame.time.Clock()
    move = 10
    while True:
        #把 图片 加载到游戏窗口
        screen.blit(background,(0,0))#相对游戏窗口坐标(0,0)
        screen.blit(hero,rect)#相对游戏窗口坐标(0,0)

        #刷新显示
        pygame.display.update()

        #延时显示
        #时间1/60秒
        clock.tick(60)

        #游戏事件 退出 监听
        for event in pygame.event.get():
            print(event)
            print(event.type)
            if event.type == pygame.QUIT: #退出游戏
                print('exit')
                pygame.quit()
                exit()#退出程序  不加能退出报错
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rect.y-=move
                if event.key == pygame.K_DOWN:
                    rect.y+=move
                if event.key == pygame.K_LEFT:
                    rect.x-=move
                if event.key == pygame.K_RIGHT:
                    rect.x+=move

'''
hero_rect = pygame.Rect(100, 500, 120, 126)
print("坐标原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄大小 %d %d" % (hero_rect.width, hero_rect.height))
# size 属性会返回矩形区域的 (宽, 高) 元组
print("英雄大小 %d %d" % hero_rect.size)
'''
#每个程序
#为了能够执行
print(__name__)
if __name__ == '__main__':
    main()







