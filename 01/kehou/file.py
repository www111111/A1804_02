'''
f=open('test.txt','w')
f.write('12345\n')

f=open('test.txt','r')
d=f.read()
e=d[:len(d)-1]
print(e+'*')


f=open('test.txt','w')
f.write('67890\n')
f.close()
f=open('test.txt','r')
d=f.read()
e=d[:len(d)-1]
print(e+'*')
f.close()




f=open('test.txt','w')
f.write('12345\n67890\n')
#f.close()

f=open('test.txt','r')
a=f.readlines()
for i in a:
    s=i[:len(i)-1]
    print(s+'*')
f.close()
'''
'''
f=open('test.txt','w+')
f.write('123456\n678906\n')
#f=open('test.txt','r+')
a=f.read()
c=f.tell()
print(c)

f.seek(0,0)
a=f.readline(5)
print(a)
f.close()
'''


f=open('test.txt','r')
f.read()
f.seek(0,0)
for i in f:
    f.read(1)
    s=f.tell()
    print('ds%s,dd%s'%(i,s))
f.close()




'''
def hs(fileName):
    f=open(fileName,'a')
    #c=f.tell()
    #print(c)
    f.close()

    f=open(fileName,'r+')
    a=f.read()
    if len(a)==0:
        print('hahaha')
        f.write('hahaha')
    else:
        print(a)
    f.close()
hs('111')
'''




'''

import os

def cc(path):
    if os.getcwd()==path:
        os.chdir(path)
        print('1111')
        print(os.getcwd())
    else:
        os.mkdir(path)
        print('2222')
        print(os.getcwd())
        os.chdir(path)
        print(os.getcwd())
cc('/home/congchao/git_new1/01/02')

def rm(rmPath):
    os.rmdir(rmPath)
rm('/home/congchao/git_new1/01/02')

def mk(mkPath):
    os.mkdir(mkPath)
mk('/home/congchao/git_new1/01/03')


'''











'''

print(os.getcwd())

os.chdir('../')
print(os.getcwd())
os.chdir('./kehou')
print(os.getcwd())

os.mkdir('s.getcwd()')
print(os.getcwd())
'''


'''
import os

os.lisdir()

'''


