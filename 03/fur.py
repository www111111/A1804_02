class House:
    def __init__(self,name,area):
        self.name=name
        self.area=area
        self.fur=[]
    def __str__(self):
        a=''
        for i in self.fur:
            a+=i+','
        return '在%s,买了房子,又买了 %s房子可用面积剩余%s.'%(self.name,a,self.area)
    def addFur(self,item):
        #if self.area>=item.area:
         #   self.area-=item.area
        self.fur.append(item.name)
        #else:
        #print('房子已经容纳不下了,面积还剩%d'%self.area)
    def set_gz(self,item):

        if self.area>=item.area:
            self.area-=item.area
        else:
            print('房子已经容纳不下了,面积不足还剩%d'%self.area)
    def get_add(self,name):
        if name=='朋友':
            self.name='北京'
        elif name=='aa':
            self.name='巴厘岛'
class Fur:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return '买了一个 %s cm 的 %s '%(self.area,self.name)

class light:
    def __init__(self,name,area,color):
        self.name=name
        self.area=area
        self.color=color
    def __str__(self):
        return '买了一个 %s cm 的 %s '%(self. area,self.name)
    def light_open(self):
        print('开灯')
    def light_bright(self):
        print('灯亮了')
    def light_close(self):
        print('关灯')
def zh(item):
    item.light_open()
    item.light_bright()
    item.light_close()


qh=House('清华',300)
qh.get_add('朋友')
print(qh)
sr_bed=Fur('双人床',100)
print(sr_bed)
qh.set_gz(sr_bed)
qh.addFur(sr_bed)
light=light('装饰灯',200,'白色')
print(light)
qh.set_gz(light)
qh.addFur(light)
print(qh)
zh(light)
print(100*'*')




'''
qh.get_add('aa')
print(qh)
sr_bed=Fur('单人床',50)
print(sr_bed)
qh.set_gz(sr_bed)
qh.addFur(sr_bed)
print(qh)
'''







