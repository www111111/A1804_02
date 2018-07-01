import copy


a='cc'
b=copy.copy(a)
print(id(a))
print(id(b))
print(a is b)

a='cc'
b=copy.deepcopy(a)
print(id(a))
print(id(b))
print(a is b)

a='b'
b=a
print(id(a))
print(id(b))
print(a is b)


print('11111111111')
a=[1,2,3]
b=copy.copy(a)
print(id(a))
print(id(b))
print(a is b)

print('11111111111')


a=[1,2,3]
b=a
print(id(a))
print(id(b))
print(a is b)


a=[1,2,3] #list可变所以内存地纸不同
b=copy.deepcopy(a)
print(id(a))
print(id(b))
print(a is b)


a=(1,2,3) #trup不可变所以内存地纸不同
b=a
print(id(a))
print(id(b))
print(a is b)


a={'b':2,'c':3}
b=a
print(id(a))
print(id(b))
print(a is b)


a={'b':2,'c':3} #字典可变所以内存地纸不同
b=copy.deepcopy(a)
print(id(a))
print(id(b))
print(a is b)








