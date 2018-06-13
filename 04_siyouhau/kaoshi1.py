class Tool():#(object)
    '''挑出100-200中到的素数，只能被自己和1整除的'''
    def sushu(self):
        for i in range(100,200):
            flag=True             #标志位
            for z in range(2,i):  #挑出任何一个能被其他数字整除的数，整除即退出
                if i%z==0:
                    flag=False
                    break

            if flag==True:        #标志位应用
                print(i)          #不能被其他数整数以后，没有执行标志位，这时执行输出i

t=Tool()
t.sushu()



