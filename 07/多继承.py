class Donkey(object):
    '''驴类 '''
    def zou(self):
        print('走的慢。。。')
    def jiao(self):
        print('驴在叫')

class Horse(object):
    '''马类 '''
    def naili(self):
        print('马力足')
    def jiao(self):
        print('马在叫')

class Mule(Donkey,Horse):
   # def jiao(self):
   #     print('骡子在叫')
    pass

mule1=Mule()
mule1.zou()
mule1.naili()
mule1.jiao()


print(Mule.__mro__)

















