from collections import Iterator

lis=[x for x in range(1,101) ]
print(lis)
lis1=[]
lis=iter(lis)

n = 0
a,b = 0,1
while n<101:
    lis1.append(b)
    a,b = b,a+b
    n += 1

for i in lis:
    if i in lis1:
        print(i)

























