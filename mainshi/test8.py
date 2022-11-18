# coding: utf-8

"""
python作用域
变量名解析：LEGB原则
python中的作用域分4种情况：
L：local，局部作用域，即函数中定义的变量；
E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
G：global，全局变量，就是模块级别定义的变量；
B：built-in，系统固定模块里面的变量，比如int, bytearray等。
搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB
"""

"""
首先是pythond的一个奇异现象，在模块层面定义的变量（无需global修饰），如果在函数中没有再定义同名变量，可以在函数中当做全局变量使用：
"""
"""
hehe = 6
def f():
    print(hehe)
f()
print(hehe)
"""
"""
hehe = 6
def f():
    global hehe
    print hehe
    hehe = 2
f()
print(hehe)
# 6
# 2
"""
x = 10
def print_x(x):
    x += 1
    print x

print_x(x)   # 全局变量进入到函数(如果不用global修饰), 就变成函数内部的局部变量
print x
# 11
# 10
print vars()

# 格式化打印dict
import json
aaa = {'name': 1212, 'age': 999, 'kids': {'name': 1111, 'age': 11}}
print json.dumps(aaa, encoding='utf-8', ensure_ascii=False, indent=4)

# 1. 当你在局部变量中命名跟全局变量有重名的时候，就不会使用全局变量
# 2. 函数中可以使用全局变量，但是不能改变，如果想要在函数中改变x的值，你需要在函数中，使用global(全局)来定义这个变量，让其变为全局的。


