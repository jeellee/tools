# coding: utf-8

import copy
a = [1, 2, 3, 4, ['a', 'b']]

b = a       # 引用

c = copy.copy(a)   # 浅拷贝

d = copy.deepcopy(a)     # 深拷贝


a.append(5)
a[4].append('c')

print a
print b
print c
print d

# [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# [1, 2, 3, 4, ['a', 'b', 'c']]
# [1, 2, 3, 4, ['a', 'b']]




arr = [[]]*5

print id(arr[0]), id(arr[1])    # 4372505880 4372505880, 是对同一个数组的引用

arr[0].append(10)
print arr   # [[10], [10], [10], [10], [10]]


arr[1].append(20)     # [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
print arr

arr.append(30)
print arr            # [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]


"""
1.什么是闭包，闭包必须满足以下3个条件：

必须是一个嵌套的函数。
闭包必须返回嵌套函数。
嵌套函数必须引用一个外部的非全局的局部自由变量。


2.闭包优点

避免使用全局变量
可以提供部分数据的隐藏
可以提供更优雅的面向对象实现
"""
# 嵌套函数但不是闭包, 没有引用外部的局部变量
def nested():
    def nst():
        print('i am nested func %s' % nested.__name__)
    return nst


# 闭包函数
def closure():
    var = 'hello world'    # 非全局局部变量

    def cloe():
        print(var)    # 引用var

    return cloe      # 返回内部函数


cl = closure()
cl()


# 用类实现一个加法的类是这样
class _Add(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


def _Add2(a):
    def add(b):
        return a+b
    return add


ad = _Add2(1)
print ad(1)   # 2
print ad(2)   # 3
print ad(3)   # 4

# 延迟绑定

def multipliers():
    return [lambda x : i*x for i in range(4)]

print [m(2) for m in multipliers()]    # [6, 6, 6, 6]


"""
因为Python解释器，遇到lambda（类似于def）,只是定义了一个匿名函数对象，并保存在内存中，
只有等到调用这个匿名函数的时候，才会运行内部的表达式，而for i in range(4) 是另外一个表达式，
需等待这个表达式运行结束后，才会开始运行lambda 函数，此时的i 指向3，x指向2

"""
# 改写为
def multipliers2():
    return [lambda x,i=i: i*x for i in range(4)]

print [m(2) for m in multipliers2()]    # [0, 2, 4, 6]

