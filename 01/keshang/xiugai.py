import os


def xiugai(nameold,namenew):
    os.rename(nameold,namenew)
    print('new name %s'%namenew)

a=input('输入要修改的名字')
b=input('输入修改后的名字')
xiugai(a,b)

"""
def delete(name):
    os.remove(name)
    print('删除%s 成功'%name)
delete('111.txt')
"""




