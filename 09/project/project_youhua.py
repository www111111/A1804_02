import project_tool

#人性化显示主菜单
#1.查看销售菜品 选择菜品 查看已点菜单  删除所选菜品 返回上级菜单
#2.现金付款 会员卡付款  返回上级菜单
#3.办卡  会员卡充值  返回上级菜单
#4.添加菜品
def system():
    print('*'*30)
    print('欢迎使用街边早餐管理系统 --- 1388888888')
    print('店内优惠活动：现在办理会员卡可享受全店商品5折优惠！',end='\n\t')
    print('1.买家服务',end='\n\t')
    print('2.付款结帐',end='\n\t')
    print('3.会员服务',end='\n\t')
    print('4.卖家服务',end='\n\t')
    print('0.退出系统')
    print('*'*30)




#付款函数 调用 现金付款函数和刷卡付款函数
def fuKuanZ():
    print('1.现金付款')
    print('2.刷卡付款')
    print('3.退出菜单')
    zjL=int(input('根据提示选择相应的付款方式'))
    if(zjL==1):
        project_tool.c.fuKuan()
        print('*'*30)
    elif(zjL==2):
        project_tool.c.shuCard()
        print('*'*30)
    elif(zjL==3):
        system()


#会员函数，调用办理会员卡函数和会员卡充值函数
def huiY():
    print('*'*30)
    print('1.办理会员卡')
    print('2.会员卡充值')
    print('3.退出子菜单')
    coo=int(input('根据提示输入相应选项'))
    if coo==1:
        print('*'*30)
        project_tool.c.banKa()
        huiY()
    elif coo==2:
        print('*'*30)
        project_tool.c.cunKuan()
        huiY()
    else:
        print('返回主菜单')#执行完他以后直接进到主菜单

# 主函数
while(True):
    system()
    coo=int(input('根据提示输入相应功能编号'))
    if(coo==1):#调用买家函数
        project_tool.cai1.dianCai()
    elif(coo==2):#调用付款函数
        fuKuanZ()
    elif(coo==3):#调用会员服务函数
        huiY()
    elif(coo==4):#卖家添加菜服务
        project_tool.cai1.add_cai()
    elif(coo==0):#退出系统函数
        print('-^ ^-'*7)
        print('已退出系统,欢迎下次光临')
        print('-^ ^-'*7)
        break







