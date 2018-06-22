import pygame
class HeroPlane(object):
    def __init__(self,imgpath,screen):
        self.screen=screen
        self.x=150
        self.y=350
        self.w=100
        self.h=124
        self.img_path=imgpath
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)#尺寸
        self.hero_plan = pygame.image.load(self.img_path)
    def display(self):
        self.screen.blit(self.hero_plan,self.rect)
def main():
    #创建游戏窗口
    screen=pygame.display.set_mode((400,500),0,32)

    #把本地文件夹的图片，获取代码
    background=pygame.image.load('./images/background.png')
    #hero = pygame.image.load('./images/hero1.png')

    #定义好位置和尺寸
    #rect = pygame.Rect(150,350,100,124)#尺寸
    #获取游戏时钟控制器
    clock = pygame.time.Clock()
    move = 10

    hero=HeroPlane('./images/hero1.png',screen)
    while True:
        #把 图片 加载到游戏窗口
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero.rect.y-=move
            if event.key == pygame.K_DOWN:
                hero.rect.y+=move
            if event.key == pygame.K_LEFT:
                hero.rect.x-=move
            if event.key == pygame.K_RIGHT:
                hero.rect.x+=move

        pygame.display.update()

        #延时显示
        #时间1/60秒
        clock.tick(60)
#每个程序
#为了能够执行
print(__name__)
if __name__ == '__main__':
    main()







