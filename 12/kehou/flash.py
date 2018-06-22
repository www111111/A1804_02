import pygame
import os
class HeroPlane(object):
    def __init__(self,imgpath,screen):
        self.screen=screen
        self.x=10
        self.y=10
        self.w=1000
        self.h=965
        self.img_path=imgpath
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)#尺寸
        self.hero_plan = pygame.image.load(self.img_path)
    def display(self):
        self.screen.blit(self.hero_plan,self.rect)
def main():
    #创建游戏窗口
    screen=pygame.display.set_mode((500,300),0,32)

    #把本地文件夹的图片，获取代码
    background=pygame.image.load('./images/background.jpg')

    #定义好位置和尺寸
    #rect = pygame.Rect(150,350,100,124)#尺寸
    #获取游戏时钟控制器
    clock = pygame.time.Clock()
    move = 5

    while True:

        p=os.getcwd()
        print(p)
        a=find('jpg$',p)
        hero=HeroPlane(a,screen)

        #把 图片 加到游戏窗口
        screen.blit(background,(0,0))#相对游戏窗口坐标(0,0)
        #screen.blit(hero.hero_plan,hero.rect)#相对游戏窗口坐标(0,0)
        hero.display()
        #刷新显示

        #游戏事件 退出 监听
        for event in pygame.event.get():
            print(event)
            print(event.type)
            if event.type == pygame.QUIT: #退出游戏
                print('exit')
                pygame.quit()
                exit()#退出程序  不加能退出报错


        pygame.display.update()

        #延时显示
        #时间1/60秒
        clock.tick(60)
#每个程序
#为了能够执行
print(__name__)
if __name__ == '__main__':
    main()







