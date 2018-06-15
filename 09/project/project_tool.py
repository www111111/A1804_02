import random
lis=[]          #存放所点菜品的列表
lis1=[]         #办卡用存储账户和密码所用列表
lis_addcai=[]   #卖家添加菜单

class Cai(object):
    __instance=None
    __cp_flag=False
    def __init__(self,name):
        if Cai.__cp_flag==False:
            self.name=name
            Cai.__cp_flag=True
    def __new__(cls,k):
        if Cai.__instance == None:
            Cai.__instance=object.__new__(cls)
        return Cai.__instance
    def  xuanzeC(self):
        while(True):
            try:
            #display_xiaos()
                dianCai=input('菜名')
                for dic_addcai in lis_addcai:
                    if dic_addcai['caiMing']==dianCai:
                        print('已点菜：%s' % dic_addcai['caiMing'] )
                        lis.append(dic_addcai)
                        panD=input('是否选好菜 输入 Y/N \t')
                        #判断是否选好菜，选好即可跳出循环，未选择好继续循环
                if (panD=='Y'):
                    break
            except Exception as result:
                print('程序异常,原因是：%s'%result)
    #卖家添菜函数
    def add_cai(self):
        while True:
            try:
                i=1
                maiJia=int(input('输入卖家密码'))  #防止买家篡改密码设置固定密码
                n=int(input('输入添加菜的个数'))   #卖家根据添加菜数设置循环次数
                if maiJia==123:
                    while(i<=n):
                        caiMingI=input('卖家请添加菜名 \t')
                        priceI=int(input('卖家请添加价钱 \t'))
                        dic_addcai={'caiMing':caiMingI,'price':priceI}
                        lis_addcai.append(dic_addcai)
                        i+=1
                    break
                else:
                    print('密码输入错误')
            except Exception as result:
                print('程序异常,原因是：%s'%result)

    #显示销售的产品
    def display_xiaos(self):
        print('所点菜名如下 ： ')
        for a in lis_addcai:                    #遍历列表查找相应的菜单
            print('菜名 :%s '% a['caiMing'])    #显示菜名
            print('价格 :%d '% a['price'])
            print('已显示所有菜单')

    #显示已点菜品函数
    def displayAll(self):
        print('所点菜名如下 ： ')
        for a in lis:                           #遍历列表查找相应的菜单
            print('菜名 :%s '% a['caiMing'])    #输出菜名
            print('已显示所有菜单')

    #删除已点菜品函数
    def delete(self):
        try:
        # print('*'*30)
            coo=int(input('请选择 1 删除部分\n请选择 2 删除全部\n'))
            if coo==1 :
                dCi=input('输入菜名字 \t')
                print('请删除 %s 菜名' % dCi)
                for dic in lis:
                    if dic['caiMing'] == dCi:
                        lis.remove(dic)
                print('删除 %s 成功' % dCi)

            elif coo==2:
                lis.clear()
        except exception as result:
            print('程序异常,原因是：%s'%result)

    def dianCaiD(self):
        print('1.查看销售菜品')
        print('2.选择菜品')
        print('3.查看已点菜单')
        print('4.删除所选菜品')
        print('5.返回上级菜单')
        print('*'*30)
    def dianCai(self):
        self.dianCaiD()
        while(True):
            zjL=int(input('根据提示选择点菜子菜单'))
            if(zjL==1):
                self.display_xiaos()
                print('*'*30)
                self.dianCaiD()
            elif(zjL==2):
                self.xuanzeC()
                print('*'*30)
                self.dianCaiD()
            elif(zjL==3):
                self.displayAll()
                print('*'*30)
                self.dianCaiD()
            elif(zjL==4):
                self.delete()
                print('*'*30)
                self.dianCaiD()
            elif(zjL==5):
                print('返回上级菜单')
                break

cai1=Cai('满汉全席')


class Card(Cai):
#定义现金付款函数
    __instance=None
    __cp_flag=False
    def __init__(self,name):
        if Card.__cp_flag==False:
            self.name=name
            Card.__cp_flag=True
    def __new__(cls,k):
        if Card.__instance == None:
            Card.__instance=object.__new__(cls)
        return Card.__instance
    def fuKuan(self):
        for dic in lis:
            try:
                print('菜名 ： %s 价格 ： %d '%(dic['caiMing'],dic['price']))
                mony=int(input('price'))
                if mony>dic['price']:         #判断如果输入的钱大于菜的单价即找零
                    zl=mony-dic['price']      #计算找零 给的价钱-商品价格
                    print('找零 %d 元' %zl)
                elif mony<dic['price']:
                    print('输入金额不足')
                else:#(dir['caiMing']=='gbr'):
                    print('付款成功')
            except Exception as result:
                print('程序异常,原因是：%s'%result)


    money=0
    #定义刷卡函数
    def shuCard(self):
        try:
            name=input('输入会员帐号')
            pas=int(input('输入会员密码'))
            for dic1 in lis1:
                if (dic1['name']==name) and (dic1['pas']==pas):
                    for dic in lis:#在菜单列表中遍历字典
                        if(money<dic['price']):  #如果付款金额小于菜价会跳到主界面
                            print('您余额不足请充值，系统将自动为您退出到主界面')
                            break
                        print('菜名 ： %s 价格 ： %.2f'%(dic['caiMing'],dic['price']*0.5))
                        print('付款成功')
                        dic1['money']=dic1['money']-dic['price']*0.5
                        print('卡内余额 %.2f元' %dic1['money'])

        except Exception as result:
            print('程序异常,原因是：%s'%result)

#办理会员卡函数
    def banKa(cls):
        try:
            dic1={}
            print('办理会员卡业务')
            name=input('设置会员帐号')
            pas=int(input('设置会员密码'))
            dic1={'name':name,'pas':pas,'money':cls.money}
            lis1.append(dic1)
            print('办理会员卡成功')
        except Exception as result:
            print('程序异常,原因是：%s'%result)




#会员卡充值函数
    def cunKuan(self):

        global money
        name_chongZhi=input('输入充值的帐号')
        coo=int(input('第一次办卡充值按 1\n一次以上卡片充值按 2\n'))
        for dic1 in lis1:

            if(dic1['name']== name_chongZhi):
                if  len(lis1)!=0 and coo==1:     #判断卡中是否有余额，没有余额 提示 并充值
                    dic1['money']=0
                    print('卡内余额不足')
                    print('请充值')
                    money=int(input('请冲入金额'))
                    dic1['money']=dic1['money']+money
                    print('卡内余额 %d' % dic1['money'])
                elif  len(lis1)!=0 and coo==2:   #如果有余额，就直接冲入相应的充值金额
                    jeIn=int(input('请冲入金额'))
                    dic1['money']=dic1['money']+jeIn
                    print('卡内余额 %d' %dic1['money'])



c=Card('黄金卡')
print(c.name)
d=Card('白金卡')
print(d.name)

