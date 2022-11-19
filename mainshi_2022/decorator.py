# coding: utf-8

"""
装饰器
decorator
<b><i>hello</i></b>
"""
def decorator(func):
    def warp(arg):
        try:
            return func(arg)
        except:
            print 'error'
    return warp

@decorator
def divide(a):
    return 100/a

divide(0)

# 1. 装饰两次

def say():
    return 'hello'


def make_blob(func):
    def warp():
        return "<b>"+func()+"</b>"
    return warp


def make_li(func):
    def warp():
        return "<li>"+func()+"</li>"
    return warp

new_say = make_blob(make_li(say))

# print new_say
# print new_say()


@make_blob
@make_li
def say2():
    return 'hello'

# print say2()    # <b><li>hello</li></b>


# 2. 装饰带参数的函数

def make_strong(func):
    def warp(name):
        return "<li>"+func(name)+"</li>"
    return warp


@make_strong
def say3(name):
    return 'hello'+" "+name

# make_strong(say3)('jeellee')
# print say3("jeellee")


# 3. 装饰器本身带参数的装饰器
def make_strong2(welcome):
    def warp(func):
        def warp_deep(name):
            return "<li>"+welcome+": "+func(name)+"</li>"
        return warp_deep
    return warp


def say4(name):
    return 'hello'+" "+name

# print make_strong2('welcome!')(say4)('jeellee')


@make_strong2('welcome')
def say5(name):
    return 'hello'+" "+name

# print say5('jeellee')


# 4. 装饰类方法

def make_young(method):
    def warp(self, name):
        self.age -= 3
        return method(self, name)
    return warp


class Lucy(object):
    def __init__(self):
        self.age = 30

    @make_young
    def say_age(self, name):
        print "I am {name}, my age is {age}".format(name=name, age=self.age)


# l = Lucy()
# l.say_age('jeellee')


# 5. functools.wraps()

def foo():
    print "foo func"

# print foo.__name__     # foo


def bar(func):
    def warp():
        print "bar func"
        return func()
    return warp

@bar
def foo2():
    print "foo func"

# print foo2.__name__    # warp


import functools


def bar2(func):
    @functools.wraps(func)
    def warp():
        print "bar func"
        return func()
    return warp


@bar2
def foo3():
    print "foo func"

# print foo3.__name__    # foo3

# 6. 应用
import time


def benchmark(func):      # 函数运行时间
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print 'benchmark: '+func.__name__, time.clock()-t
        return res
    return wrapper


def logging(func):       # 日志
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print 'logging: '+func.__name__, args, kwargs
        return res
    return wrapper


def counter(func):        # 计数器
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "counter: {0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))


# print reverse_string('ni hao jeellee')


@counter
@benchmark
@logging
def get_random_futurama_quote():
    from urllib import urlopen
    # result = urlopen("http://www.baidu.com").read()
    result = urlopen("http://www.sina.com.cn/").read()
    try:
        value = result.split("<title>")[1].split("</title>")[0]
        return value.strip()
    except:
        return "No, I'm ... doesn't!"


@counter
@benchmark
@logging
def get_random_futurama_quote2(url):
    from urllib import urlopen
    # result = urlopen("http://www.baidu.com").read()
    result = urlopen(url).read()
    try:
        value = result.split("<title>")[1].split("</title>")[0]
        return value.strip()
    except:
        return "No, I'm ... doesn't!"

print get_random_futurama_quote2("http://www.sohu.com/")
