class test(object):

    __money=1
    def get(self):
        return self.__money
    def set(self,value):
        self.__money=value
    money=property(get,set)  #属性

class test1(object):

    __money=1
    @property
    def n(self):#注意get set 的名字相同
        return self.__money
    @n.setter
    def n(self,value):
        self.__money=value

test_p=test1()
print(test_p.n)
test_p.n=98
print(test_p.n)





















