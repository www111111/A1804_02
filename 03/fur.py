class House:
    def __init__(self,name,area):
        self.name=name
        self.area=area
        self.fur=[]
    def __str__(self):
        a=''
        for i in self.fur:
            a+=i
        return '在%s,买了%s平房子,里面有%s.'%(self.name,self.area,a)
    def addFur(self,item):
        self.fur.append(item.name)
class Fur:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return '买了一个 %s cm 的 %s '%(self.area,self.name)

qh=House('清华','100')
print(qh)
sr_bed=Fur('双人床','100')
print(sr_bed)
qh.addFur(sr_bed)
print(qh)

sr_bed=Fur('单人床','50')
print(sr_bed)
qh.addFur(sr_bed)
print(qh)








