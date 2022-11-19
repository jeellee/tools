# coding: utf-8

"""
lambda只是一个表达式，函数体比def简单很多，很多时候定义def，然后写一个函数太麻烦，这时候就可以用lambda定义一个匿名函数

lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
"""
a = map(lambda x: x*x, [y for y in range(10)])
print a
"""
map()：映射，用法和filter()类似，也是将序列放入函数进行运算，但是，不论运算结果为什么，map()都将忠实反馈，这是map()和filter()的主要区别。
请注意，filter()和map()中的function都必要有一个返回值。
"""


b = list(filter(lambda x:True if x % 3 == 0 else False, range(100)))
print b
"""
filter()：简单的理解为过滤器，需要两个参数，function，和一个序列（字符串、列表、元组都是序列），过滤器会依次将序列的值传入function中，
如果返回True的话，将其重新生成一个列表返回。
"""

"""
函数式编程
函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。
而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言

map
filter
reduce
都是函数式编程
"""

def add(x, y):
    return x+y

sum = reduce(add, [1, 2, 3, 4, 5])
print sum


print reduce(lambda x,y: x+y, map(lambda x: x*x, [1, 2, 3, 4, 5]))


