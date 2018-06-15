



#import mtest.t01
#import mtest.t02     #跨级进行调用。调的级在同一个大文件夹里面，二小文件夹里。
from mtest.t01 import *
from mtest.t02 import *
t01()
t02()


#mtest.t01.t01()
#mtest.t02.t02()


