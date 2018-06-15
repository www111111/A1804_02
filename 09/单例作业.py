
class GirlF(object):
    __instance=None
    __gf_flag=True
    def __init__(self,name):
        if GirlF.__gf_flag == True:
            self.name=name
            GirlF.__gf_flag=False#GF_改
    def __new__(cls,k):             #因为init有参数所以，在先执行的new里面加入参数k
        if cls.__instance == None:
            cls.__instance=object.__new__(cls)#重写
        return cls.__instance

G1=GirlF('小花花')
G2=GirlF('小花')
print(G1.name)
print(G2.name)
print(id(G1))
print(id(G2))
























