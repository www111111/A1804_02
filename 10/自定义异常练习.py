
class MyError(Exception):
    def __init__(self,name):#可加age等变量
        self.name=name

def login():
    acc=input('account')
    pas=input('passwd')
    if len(acc) < 5:
        raise MyError('ErrorLogin:登录帐号位数不对')
    elif len(pas)<6:
        raise MyError('ErrorLogin:登录密码位数不足6位')
    else:
        if acc=='12345' and pas=='123456':
            print('登录成功')
        else:
            print('登录失败')
try:
    login()
except Exception as r:
    print('程序异常，原因是：%s'%r)#r.name  r.age r抓Myerror




















