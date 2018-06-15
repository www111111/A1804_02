
class Myerror(Exception):
    def __init__(self,name):
        self.name=name

def get_ps():
    pwd=input('input passwd')
    if len(pwd) != 6:
        raise Myerror('密码输入不等于6位')
try:
    get_ps()
except Exception as r:
    print('程序异常 内容：%s'%r)























