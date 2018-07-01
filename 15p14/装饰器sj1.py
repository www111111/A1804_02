

def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
                #定义函数：完成包裹数
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
@makeBold
def test1():
    return "hello world-1"
@makeItalic
def test2():
    return "hello world-2"
@makeBold
@makeItalic  #先执行靠近test3的
def test3():
    return "hello world-3"

print(test1())
print(test2())
print(test3())
#<b>hello world-1</b>
#<i>hello world-2</i>
#<i><b>hello world-3</b></i>










