import pygame
import time
import random
class Base(object):         #设飞机的父类
     def __init__(self,imgpath,screen,x,y):
         self.screen=screen #创建的窗口 对象
         self.x=x
         self.y=y
         self.w=100
         self.h=124
         self.images = imgpath
         self.rect = pygame.Rect(self.x,self.y,self.w,self.h)#设置飞机尺寸
class Plane(Base):
    def __init__(self,screen,imgpath,x,y):
        Base.__init__(self,imgpath,screen,x,y)
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.load_image = pygame.image.load(self.images) #加载飞机的图片
        self.fire_list = []     #存放子弹列表
        self.bom = []           #存放飞机图片列表
        self.enemy_bom = []     #存放敌机的爆炸图片
        self.create__image()    #添加爆炸图片函数
    def create__image(self):
        self.bom.append(pygame.image.load('./images/hero_blowup_n1.png'))
        self.bom.append(pygame.image.load('./images/hero_blowup_n2.png'))
        self.bom.append(pygame.image.load('./images/hero_blowup_n3.png'))
        self.bom.append(pygame.image.load('./images/hero_blowup_n4.png'))
        self.enemy_bom.append(pygame.image.load('./images/enemy0_down1.png'))
        self.enemy_bom.append(pygame.image.load('./images/enemy0_down2.png'))
        self.enemy_bom.append(pygame.image.load('./images/enemy0_down3.png'))
        self.enemy_bom.append(pygame.image.load('./images/enemy0_down4.png'))
    def display(self):
        self.screen.blit(self.load_image,self.rect) #将图片添加到屏幕
        for i in self.fire_list:
            if i.judge():
                self.fire_list.remove(i)            #删除过界子弹
            i.display()
            i.move(3)                               #设置速度并移动
class Hero_plane(Plane):
    def __init__(self,screen,images):
        Plane.__init__(self,screen,images,250,500)
        self.fire_list = []
        self.num = -2
    def fire(self):
        self.fire_list.append(Hero_bullet(self.screen,'./images/bullet-3.gif',self.rect.x,self.rect.y))
    def bomb(self):
        a = 0
        for i in self.bom:                          #遍历子弹图片列表
            self.screen.blit(i,(self.rect.x,self.rect.y)) #在屏幕上显示相应的图片
            pygame.display.update()
            time.sleep(0.4)
            if a == 3:
                print('游戏失败，结束游戏')
                exit()                  #如果我方飞机爆炸，直接退出游戏
            a += 1

class Enemy_plane(Plane):
    def __init__(self,screen,images):
        super().__init__(screen,images,random.randint(0,390),random.randint(1,200))   #随机位置产生敌机
        self.flag = 'right'
        self.num = 2
        self.hit = False
        #self.fire_list = []
    def auto_move(self):
        if self.flag == 'right':
            self.rect.x += 5
            self.rect.y += 2
        else:
            self.rect.x -= 2
            self.rect.y += 1
        if self.rect.x >= 400:
            self.flag = 'left'
        elif self.rect.x <= 0:
            self.flag = 'right'
    def fire(self):
        self.fire_list.append(Enemy_bullet(self.screen,'./images/bullet-1.gif',self.rect.x,self.rect.y))

    def bomb(self):
        for ss in self.enemy_bom:      #遍历爆炸图片并相应显示,遍历完即爆炸图片消失
            self.screen.blit(ss,(self.rect.x,self.rect.y))
            pygame.display.update()
            clock = pygame.time.Clock() #和update使用
            clock.tick(20)
        self.hit = True                 #爆炸以后设置删除敌机的标志位

class Dijiqun(object):                  #定义敌机群类
    def __init__(self,screen,images):
        self.screen = screen
        self.images = images
        self.dijiqun_list = []          #存放敌机的列表
        #self.a = 1
    def add(self):
        self.dijiqun_list.append(Enemy_plane(self.screen,self.images))
    def display(self,hero_plane):
        for i in self.dijiqun_list:
            i.display()
            i.auto_move()
            if random.randint(1,100) == 8:
                i.fire()
            if i.rect.y > 800:
                self.dijiqun_list.remove(i)     #如果过界就会消失
            jiluo(hero_plane,i,51,39)           #在hero_plane遍历子弹，与敌机i的位置比较
            jiluo(i,hero_plane,100,124)         #在i遍历子弹，与hero_plane的位置比较
            if i.hit == True:                   #如果爆炸标志为为True，删除图片
                self.dijiqun_list.remove(i)
def jiluo(zidan,zhui,w,h):
    for i in zidan.fire_list:
        if (zhui.rect.x < i.x < zhui.rect.x +w) and (zhui.rect.y < i.y < zhui.rect.y + h):
            zhui.bomb()

class Bullet(object):
    def __init__(self,screen,images,x,y):
        self.images = images
        self.load_images = pygame.image.load(self.images)
        self.x = x
        self.y = y
    def display(self):
        self.screen.blit(self.load_images,(self.x,self.y))
    def judge(self):
        if (self.y > 800) or (self.y <0):
            return True
        else:
            return False

class Hero_bullet(Bullet):
    def __init__(self,screen,images,x,y):
        super().__init__(screen,images,x,y)
        self.screen = screen
        self.images = images
        self.x = x
        self.y = y
    def move(self,num):
        self.y -= num

class Enemy_bullet(Bullet):
    def __init__(self,screen,images,x,y):
        super().__init__(screen,images,x,y)
        self.screen = screen
        self.images = images
        self.x = x
        self.y = y
    def move(self,num):
        self.y += num

def key_control(hero,move_step,dijiqun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('游戏退出')
            pygame.quit()
            exit()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y >= 5:
            hero.rect.y -= move_step
    elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y <= 500:
            hero.rect.y += move_step
    elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x >= 0:
            hero.rect.x -= move_step
    elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x <= 350:
            hero.rect.x += move_step
    elif keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_SPACE]:
            hero.fire()




