import pygame
class HeroPlane(object):
    def __init__(self,imgpath,screen):
        self.screen=screen# 创建的窗口 对象
        self.x=150
        self.y=350
        self.w=100
        self.h=124
        self.img_path=imgpath
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)#尺寸
        self.hero_plan = pygame.image.load(self.img_path)
        self.bullet_list = []

    def display(self):      #设置飞机
        self.screen.blit(self.hero_plan,self.rect)
        for i in self.bullet_list: #遍历列表中的i对象，执行一次飞机显示子弹就显示
            i.display()           #子弹的对象.display()
            i.move()

    def fire(self):#发射子弹，执行一次发射一次，子弹保存在列表里
        self.bullet_list.append(Bullet('./images/bullet.png', self.screen,self.rect.x,self.rect.y))


class Bullet(object): #创建子弹类
    def __init__(self,imgpath,screen,x,y):
        self.screen=screen #窗口建立同飞机的窗口建立
        self.x=x+40
        self.y=y-40
        self.img_path=imgpath
        self.bullet = pygame.image.load(self.img_path)


    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
        #将self.x .y直接传入，不同飞机长宽高

    def move(self):
        self.y-=2

def key_control(hero,move_step):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #退出游戏
            print('Exit Success')
            pygame.quit()
            exit()#退出程序  不加能退出报错
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.fire()  #按space可发火
    keys_pressed = pygame.key.get_pressed()#放到列表
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        hero.rect.x += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        hero.rect.x -= move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        hero.rect.y += move_step


def main():
    #创建游戏窗口
    screen=pygame.display.set_mode((400,500),0,32)

    #把本地文件夹的图片，获取代码
    background=pygame.image.load('./images/background.png')

    #hero = pygame.image.load('./images/hero1.png')
    #rect = pygame.Rect(150,350,100,124)#尺寸

    clock = pygame.time.Clock()
    move_step = 10

    hero=HeroPlane('./images/hero1.png',screen)
    while True:
        screen.blit(background,(0,0))#相对游戏窗口坐标(0,0)
        hero.display()
        key_control(hero,move_step)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()







