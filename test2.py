'''
f=open('test1.py','w+')
f.write('hhhhhhh')
f.seek(0)
print(f.read())
#print(aaaa)
f.close()
'''
#open("test1.py","w+").read()

#f.write('hello word')
#long=f.read(5)
#print(long)
#long=f.read()
#print(long)


'''
content=f.readline(3)
print(content)
for i in content:
    print(i)
'''
'''
ss=f.read()
aa=f.tell()
print(aa)
f.seek(5,0)
cc=f.tell()
print(cc)
f.seek(2,1)
cc=f.tell()
print(cc)
f.close()

'''
'''
cc='hello world'
yy=cc.rfind('lo')
print(yy)

'''
'''
#old_name=input('shur file name')
old_file=open('test1.py','r')
new_file=open('test.txt','w')
new_file.write(old_file.read())
old_file.close()
new_file.close()
'''

'''
#换行追加
a=open('test1.py','a+')
a.write('\ndd')
a.close()
'''






c=open('test1.py','rb')
print(c.tell())
c.seek(3,2)
print(c.tell())
a=c.read()
print(a)
c.close()















