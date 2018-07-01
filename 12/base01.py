
import pygame
import time
import random
class Base(object):
    def __init__(self,imgpath,screen,x,y):
        self.screen=screen# 创建的窗口 对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=imgpath
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)#尺寸

class Plan(Base):
    def __init__(self,imgpath,screen,x,y):
        Base.__init__(self,imgpath,screen,x,y)
        self.hero_plan = pygame.image.load(self.img_path)
        self.bullet_list = []
        self.bullet1_list = []
        self.bullet_rmlist = []
        self.bomb_list=[]
        self.hit = False
        self.image_num = 0 #While True增加次数，效果延迟
        self.image_index = 0 # 爆炸图片id
        self.create_image()
        self.flag1=False
    def create_image(self):
        self.bomb_list.append(pygame.image.load('./images/enemy1_down1.png'))
        self.bomb_list.append(pygame.image.load('./images/enemy1_down2.png'))
        self.bomb_list.append(pygame.image.load('./images/enemy1_down3.png'))
        self.bomb_list.append(pygame.image.load('./images/enemy1_down4.png'))

    def display(self):#设置飞机
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index],self.rect)
            self.image_num += 1
            if self.image_num == 7:
                self.image_index += 1
                self.image_num = 0
            if self.image_index >= 3:
                #self.bomb_list.clear()
                self.image_index=0
                #self.rect.x=0
                #self.rect.y=-10
               # print('游戏胜利')
                print('游戏结束')
            #    exit()
        else:
            #self.screen.blit(self.image,self.rect)
            self.screen.blit(self.hero_plan,self.rect)
        if len(self.bullet_list) > 0:
            for i in self.bullet_list: #遍历列表中的i对象，执行一次飞机显示子弹就显示
                if i.judge():
                    self.bullet_list.remove(i)
                i.display()           #子弹的对象.display()
                i.move()
        else:
            for i in self.bullet1_list:
                if i.judge():
                    self.bullet_list.remove(i)
                i.display()           #子弹的对象.display()
                i.move3()
    def bomb(self):
            #print('111111111111')
        self.hit = True


class HeroPlane(Plan):
    def __init__(self,imgpath,screen,x,y):
        Plan.__init__(self,imgpath,screen,250,300)


    def fire(self):#发射子弹，执行一次发射一次，子弹保存在列表里
        self.bullet_list.append(Bullet('./images/bullet.png', self.screen,self.rect.x,self.rect.y))
    def fire1(self):#发射子弹，执行一次发射一次，子弹保存在列表里
        self.bullet1_list.append(Bullet('./images/bullet.png', self.screen,self.rect.x,self.rect.y))



class Diji(Plan):

    def __init__(self,imgpath,screen,x,y):
         Plan.__init__(self,imgpath,screen,0,0)
         self.flag='left'#设置敌机的行走标志位，默认值

    def fire(self,hero):#发射子弹，执行一次发射一次，子弹保存在列表里
         self.bullet_list.append(Bulletdj('./images/bullet1.png',self.screen,self.rect.x,self.rect.y))
    def fire1(self):#发射子弹，执行一次发射一次，子弹保存在列表里
        self.bullet1_list.append(Bullet('./images/bullet.png', self.screen,self.rect.x,self.rect.y))

         #judge_bao(hero,Bullet_f)

    def auto_control(self):
         if self.flag=='left'  :
             self.rect.x += 2
         elif self.flag=='right':
             self.rect.x -= 2

         if self.rect.x >=400-self.rect.width:
             self.flag='right'
         elif self.rect.x <= 0:
             self.flag='left'
    def auto_control1(self):
         if self.flag=='left'  :
             self.rect.x += 1
             self.rect.y += 1
         elif self.flag=='right':
             self.rect.x -= 1
             self.rect.y -= 1

         if self.rect.x >=400-self.rect.width:
             self.flag='right'
         elif self.rect.x <= 0:
             self.flag='left'

class Bullet_f():
     def __init__(self,imgpath,screen,x,y):
         self.screen=screen #窗口建立同飞机的窗口建立
         self.x=x+40
         self.y=y+20
         self.img_path=imgpath
         self.bullet = pygame.image.load(self.img_path)

     def display(self):
         self.screen.blit(self.bullet,(self.x,self.y))
         #将self.x .y直接传入，不同飞机长宽高



class Bullet(Bullet_f): #创建子弹类
     def __init__(self,imgpath,screen,x,y):
         Bullet_f.__init__(self,imgpath,screen,x,y)

     def judge(self):
         if self.y >= 500:
             return True
         else:
             return False

     def move(self):
         self.y-=2
     def move3(self):
         self.y-=10


class Bulletdj(Bullet_f): #创建敌机子弹类
     def __init__(self,imgpath,screen,x,y):
         Bullet_f.__init__(self,imgpath,screen,x,y)

     def judge(self):
         if self.y >= 500:
             return True
         else:
             return False

     def move(self):
        self.y+=2



def key_control(hero,diren,diren1,move_step):
     for event in pygame.event.get():
         if event.type == pygame.QUIT: #退出游戏
             print('Exit Success')
             pygame.quit()
             exit()#退出程序  不加能退出报错
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 hero.fire()  #按space可发火
             #elif event.key == pygame.K_b:
             #    diren.bomb()
             elif event.key == pygame.K_r:
                 hero.fire1()
     keys_pressed = pygame.key.get_pressed()#放到列表
     if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
         if hero.rect.x <=300:
             hero.rect.x += move_step
     if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
         if hero.rect.x >0:
             hero.rect.x -= move_step
     if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
         if hero.rect.y >0:
             hero.rect.y -= move_step
     if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
         if hero.rect.y <=300:
             hero.rect.y += move_step

     diren.auto_control()
     diren1.auto_control1()

def panduan(hero,diren,diren1):
    for i in hero.bullet_list:# 摧毁敌机大x行走
        if diren.rect.y+124 >= i.y >=diren.rect.y and diren.rect.x +90 >= i.x >= diren.rect.x and i.y>0:
            diren.bomb()
            print('hero win')
            exit()
        if diren1.rect.y+124 >= i.y >=diren1.rect.y and diren1.rect.x +90 >= i.x >= diren1.rect.x and i.y>0:
            diren1.bomb()
            print('hero win')
            exit()
    for i in hero.bullet1_list:#摧毁敌机小 xy行走
        if diren.rect.y+124 >= i.y >=diren.rect.y and diren.rect.x +90 >= i.x >= diren.rect.x and i.y>0:
            diren.bomb()
            print('hero win')
            exit()
        if diren1.rect.y+124 >= i.y >=  diren1.rect.y and diren1.rect.x +90 >= i.x >= diren1.rect.x and i.y>0:
            diren1.bomb()
            print('hero win')
            exit()
    for i in diren.bullet_list:#大飞机摧毁已方飞机
        if hero.rect.y+124 >= i.y >= hero.rect.y and hero.rect.x +90 >= i.x >= hero.rect.x and i.y>0:
            hero.bomb()
            print('diren win')
            exit()
    for i in diren1.bullet_list:#小飞机摧毁已方飞机
        if hero.rect.y+124 >= i.y >= hero.rect.y and hero.rect.x +90 >= i.x >= hero.rect.x and i.y>0:
            hero.bomb()
            print('diren win')
            exit()

