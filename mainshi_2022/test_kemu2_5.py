# 多继承 继承顺序，初始化顺序
class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super().__init__()
        print("B")


# class C(A, B):
#     def __init__(self):
#         super().__init__()
#         print("C")


class C1(B, A):
    def __init__(self):
        super().__init__()
        print("C1")


# c = C()

# 报错如下, 在创建类C时就已经报错， 还未走到实例化这里
"""
Traceback (most recent call last):
  File "D:/learn/tools/mainshi_2022/test_kemu2_5.py", line 12, in <module>
    class C(A, B):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B
"""

c1 = C1()   # 不报错
"""
A
B
C1
"""


# -nonlocal global
"""
nonlocal 用来声明外层的局部变量。
global 用来声明全局变量。

nonlocal、global 关键字的用法
"""
a = 100
def outer():
    b = 10
    def inner():
        nonlocal b    # 使用外层的局部变量
        print('inner b:', b)
        b = 20
        global a
        a = 1000      # 使用全局变量
    inner()
    print('outer b:', b)

outer()
print('a: ', a)

""" 打印
inner b: 10
outer b: 20
a:  1000
"""

b2 = 100
def outer2():
    b2 = 10
    def inner():
        nonlocal b2    # 使用外层的局部变量
        b2 = 20
    print('outer b2-1:', b2)
    inner()
    print('outer b2-2:', b2)

outer2()
print('b2: ', b2)
"""
outer b2-1: 10
outer b2-2: 20
b2:  100       # 没有使用global声明使用全局变量，全局变量无变化
"""

# -切片列表
"""
In [118]: atr='World'

In [119]: atr[-5:0]   # 记住 第-5个 和 第0个 都是W， 切片后就为空
Out[119]: ''

In [120]: atr[-5:-1]
Out[120]: 'Worl'

In [121]: atr[-5:]
Out[121]: 'World'
"""