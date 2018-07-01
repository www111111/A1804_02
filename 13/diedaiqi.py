from collections import Iterable

#第一种迭代
L =[ x*2 for x in range(5)]
print(L)
L =( x*2 for x in range(5))#每执行一次就返回迭代
print(L)
#print(next(L))
#print(next(L))
#print(next(L))
#print(next(L))
#print(next(L))
#print(next(L))
for i in L:
   print(i)

print(isinstance([x*2 for x in range(5)], Iterable))


