
_one=1
two=2
class Person(object):

    def dowork(self):
        self._work()
        self.__away()
    def _work(self):
        print('my _work')
    def __away(self):
        print('my __away')

class Person01(Person):
    pass
xiaohua=Person()
#xiaohua.__away()
xiaohua._work()

























