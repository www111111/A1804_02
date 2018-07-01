
#2种
from inspect import isgeneratorfunction

def scq(i,t):

    while i<t:
        i+=1
        yield(i)

f = scq(0,5)
print(next(f))
next(f)
for i in f:
    print(i)

print(isgeneratorfunction(scq)) # True
