
class Test(object):
    def __init__(self):
        self.switch='open'#初始化开关
    def div(self,a,b):
        try:
            return a/b
        except Exception as r:#抓异常在此步骤以后
            if self.switch=='open':#开关开，执行捕捉。否则，抛出。
                print('程序异常，原因：%s'%r)
            else:
                raise
test=Test()
#test.switch='close'
print(test.div(2,0))


























