
import sys

#sys.path.append('..')#在跨级，跨文件夹进行调用的时候将系统默认中添加自己的路径。
sys.path.append('/home/congchao/git_new1/scr')
print(sys.path)
from mtest.t01 import *
from mtest.t02 import *
t01()
t02()




