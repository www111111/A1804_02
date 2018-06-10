cj={}
ifo={}
list_ifo=[]
list_cj=[]
class Banji:
    def __init__(self,class_tea,class_num):
        self.class_tea=class_tea
        self.class_num=class_num
        self.student=[]
    def add_student(self,item):
        #self.student1=student
        self.student.append(item.name)
    def __str__(self):
        return ('班级学生有：%s\n 班主任是：%s'%(self.student,self.class_tea))


class Student:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        #self.cj={}
        ifo={'name':name,'age':age,'sex':sex}
        list_ifo.append(ifo)
       # print(list_ifo)
        print('学生信息已存入成功')
    def addscore(self,d,a,b,c):
        cj={'name':d,'yuwen':a,'shuxue':b,'yingyu':c}
        #self.cj[k]=v
        list_cj.append(cj)
        #print(list_cj)
        print('添加学生信息成功')
    def chakan(self):
        print(self.name)
        print(self.age)
        print(self.sex)
class Score:
    def __init__(self):
        self.yuwen=0
        self.shuxue=0
        self.yingyu=0
    def setcj(self,item,kemv,score):
        item.cj[kemv]=score
        #print(item.kemv)
    def getcj(self,item,cxkm):
        #return self.kemu

        i=item.cj[cxkm]
        print(i)
            #print(item.cj)

    def __str__(self):
        for i in list_cj:
        #if i['name']==name:
            print('姓名：%s\t 语文：%d\t 数学：%d\t 英语：%d\t'%(i['name'],i['yuwen'],i['shuxue'],i['yingyu']))
        return '所有同学成绩如上'

cj_return=Score()
a=''
for i in range(1,3):
    a=input('输入录用信息名字')
    b=int(input('输入录用信息年龄'))
    c=input('输入录用信息性别')
    a=Student(a,b,c)

    e=input('输入录用成绩名字')
    f=int(input('输入录用成绩语文'))
    g=int(input('输入录用成绩数学'))
    h=int(input('输入录用成绩英语'))
   # a=Score()
    a.addscore(e,f,g,h)

#s1=Student('王刚',33,'男')
#s2=Student('李刚',22,'女')
#s1.addscore('王刚',11,22,33)
#s1.addscore('李刚',61,82,93)

name=input('输入录用查询的名字')
for i in list_ifo:
    if i['name']==name:
        print('姓名：%s \t年龄：%s \t性别：%s \t'%(i['name'],i['age'],i['sex']))


for i in list_cj:
    if i['name']==name:
        print('姓名：%s \t语文：%d \t数学：%d \t英语：%d \t'%(i['name'],i['yuwen'],i['shuxue'],i['yingyu']))
print('*'*30)
#print(wangg)

banji=Banji('李四',110)
banji.student.extend(list_ifo)
print(banji.student)
#print(cj_return)


def add_ifo():
    name=input('输入增加的姓名')
    age=input('输入增加的年龄')
    sex=input('输入增加的性别')
    ifo={'name':name,'age':age,'sex':sex}
    list_ifo.append(ifo)
    #print(list_ifo)
    print('增加学生信息成功')
add_ifo()

def delete_ifo():
    name=input('输入删除的姓名')
    for dic in list_ifo:
        if dic['name']==name:
            list_ifo.remove(dic)
            #print(list_ifo)
            print('删除信息完成%s'%dic['name'])
delete_ifo()

def gai_ifo():
    name=input('输入要改的姓名')
    age=input('输入要改的年龄')
    sex=input('输入要改的性别')
    for dic in list_ifo:
        if dic['name']==name:
           dic['name']=name
           dic['age']=age
           dic['sex']=sex
           #print(list_ifo)
           print('改信息完成')
gai_ifo()

def cha_ifo():
    name=input('输入要查询的姓名')
    for dic in list_ifo:
        if dic['name']==name:
            print('姓名：%s \t年龄：%s \t性别：%s \t'%(dic['name'],dic['age'],dic['sex']))
cha_ifo()


