'''
#coding utf-8
ts=open('ts.txt','w+')
ts.write('春眠不知晓\n处处蚊子咬\n')
ts.close()

ts=open('ts.txt','r+')
a=ts.read()
print(a)
ts.close()
'''
'''
ts=open('ts.txt','a+')
ts.write('-*-')
ts.close()
ts=open('ts.txt','r+')
a=ts.read()
print(a)
ts.close()
ts=open('ts.txt','a+')
ts.write(a)
ts.close()

ts=open('ts.txt','r+')
a=ts.read()
print(a)
ts.close()

'''
'''
#在唐诗以后追加符号
ts=open('ts.txt','r+')
f2=open('ts2.txt','w+')
c=ts.readlines()
print(c)

for i in c:
    d=len(i)
  #  print(d)
    #s=i[:len(i)-1]
    f2.write(s+'*\n')

    print('%s'%(s+'*'))

f2=open('ts2.txt','r+')
ss=f2.read()
print(ss)
f2.close()



ts=open('ts.txt','a+')
ts.write(ss)
ts.close()

ts=open('ts.txt','r+')
print(ts.read())
#print(sss)
ts.close()


print('文件名字',ts.name)
print('文件是否关闭',ts.closed)
print('文件访问模式',ts.mode)


'''


ts=open('ts.txt','w+')
ts.write('春眠不知晓\n处处蚊子咬\n')
ts.close()

ts=open('ts.txt','r+')
c=ts.readline()
print(c)
print('当前位置是 %d'% (ts.tell()))
c=ts.readline()
print(c)
print('当前位置是 %d'% (ts.tell()))
ts.close()


ts=open('ts.txt','r+')
ts.seek(0,0)
c=ts.readline(5)
print(c)
ts.close()

f2.open('bl.txt'.'w+')
ts=open('ts.txt','w+')

for i in ts:
    f2.write(i)
    print('')







