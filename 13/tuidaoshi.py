#推导式
a = [i for i in range(1,100,2) ]
print(a)

a = [i for i in range(1,100) if i%2!=0]
print(a)

b = [i for i in range(1,5) for j in range(1,3)]
print(b)

b = [j for i in range(1,5) for j in range(1,3)]
print(b)

#range(5)  0-4
b = [(i,j,k) for i in range(1,5) for j in range(1,3) for k in range(1,3)]
print(b)

