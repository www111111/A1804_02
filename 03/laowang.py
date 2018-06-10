
class People:
    def __init__(self,name,role):
        self.name=name
        self.role=role
        self.ph=100
    def __str__(self):
        return '创建角色%s成功 还剩%d 血量'%(self.name,self.ph)

    def kaiqiang(self):
        print('%s开枪射击目标，并击中目标'%self.name)

    def zhuangZiDan(self,item,zidan):
        print('往AK弹夹装子弹')
        item.rongliang=zidan
        print('枪内有子弹%s个'%item.rongliang)

    def shangDanJia(self):
        print('将弹夹放入AK')

    def shangTang(self):
        print('AK子弹上膛，准备发射')

    def diaoxue(self,shashangli):
        self.ph-=shashangli
        print('剩余血量 %s'%self.ph)

class Gun:
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed

    def jub_danjia(self,item):
        if item.rongliang>0:
            print('AK有弹夹有子弹，剩余%s发子弹'%item.rongliang)
            item.rongliang-=1
        else:
            print('AK已无弹夹，剩余%s发子弹'%item.rongliang)

class Clip:
    def __init__(self,rongliang):
        self.rongliang=rongliang

    def londing_Clip(self):
        print('子弹加入弹夹,已装%s个子弹'%self.rongliang)

    def set_cunzidan(self,item):
        self.rongliang+=item
        return '已存入子弹 %s发'%self.rongliang

class Bullet:
    def __init__(self,shashangli):
        self.shashangli=shashangli

    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)#查看剩余血量
        print('子弹产生了%s伤害'%self.shashangli)

    def fashe(self):
        print('子弹飞起来了')

laowang=People('老王','攻击型人物')
zidan=Clip(0)
gun1=Gun('红色','快')
gun1.jub_danjia(zidan)
laowang.zhuangZiDan(zidan,10)#老王将弹夹放入子弹
laowang.shangDanJia()#弹夹放入AK
gun1.jub_danjia(zidan)#查看弹夹子弹数量
laowang.shangTang()#子弹上膛

dr=People('敌人','防御型')#建立敌人
print(dr)#输出属性
dr_zidan=Bullet(5)#设置子弹伤害

i=10
while i>0:
    i-=1
    laowang.kaiqiang()#老王开枪
    dr_zidan.shanghai(dr)#查看剩余血量
    gun1.jub_danjia(zidan)



'''
laowang.kaiqiang()#老王开枪
dr_zidan.shanghai(dr)#查看剩余血量
gun1.jub_danjia(zidan)#查看弹夹子弹数量
#print(dr)
#dr_zidan.shanghai(dr)


laowang.kaiqiang()#老王开枪
dr_zidan.shanghai(dr)
gun1.jub_danjia(zidan)

laowang.kaiqiang()#老王开枪
dr_zidan.shanghai(dr)
gun1.jub_danjia(zidan)

laowang.kaiqiang()#老王开枪
dr_zidan.shanghai(dr)
gun1.jub_danjia(zidan)

'''









