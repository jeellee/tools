# coding: utf-8

"""
新式类和旧式类
"""


class C(object):    # 新式类, 新式类继承了object对象
    pass

# print dir(C)
# ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


class B:       # 经典类
    pass

# print dir(B)
# ['__doc__', '__module__']


"""
# __new__是一个静态方法静态方法
# def __new__(cls, *more): # known special case of object.__new__

# 所以调用一个实例c = C(2)，实际执行的代码为：
c = C.__new__(C, 2)
if isinstance(c, C):
    C.__init__(c, 23)  # __init__第一个参数要为实例对象

__new__和__init__的区别
1.__new__是一个静态方法,而__init__是一个实例方法.
2.__new__方法会返回一个创建的实例,而__init__什么都不返回.
3.只有在__new__返回一个cls的实例时, 后面的__init__才能被调用.
4.当创建一个新实例时调用__new__,初始化一个实例时用__init__.
ps: 而__metaclass__是控制类的创建(类其实也是一个对象的实例).
所以我们可以分别使用__metaclass__,__new__和__init__来分别在类创建,实例创建和实例初始化的时候做一些小手脚.
"""


# 用__new__来实现单例
class Singleton(object):
    _singlettons = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._singlettons:
            cls._singlettons[cls] = object.__new__(cls)
        return cls._singlettons[cls]

s1 = Singleton()
print id(s1)
s2 = Singleton()
print id(s2)
"""
另一种单例的实现
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args)
        return cls._instance

class MyClass(Singleton):
    a = 1

用装饰器实现
def singleton(cls, *args, **kw):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    a = 1

用import实现
# mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()

# to use (实例化后, 从另一个文件导入即可)
from mysingleton import my_singleton

my_singleton.foo()
"""

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args)
        return cls._instance

class MyClass(Singleton):
    a = 1

# mm1 = MyClass()
# print id(mm1)
# mm2= MyClass()
# print id(mm2)


def singleton(cls):
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class MyClass2(Singleton):
    a = 1

mm3 = MyClass()
print id(mm3)
mm4 = MyClass()
print id(mm4)


# 用__new__来实现共享属性
class Borg(object):
    _state = {'bbbb': 1}
    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob

class MyClass(Borg):
    a = 1

mc = MyClass()
print 'mc.__dict__', mc.__dict__


# __getattribute__  对新式类的实例来说，所有属性和方法的访问操作都是通过__getattribute__完成，

class listNoAppend(list):
    def __getattribute__(self, item):
        if item == 'append':
            raise AttributeError, item
        return list.__getattribute__(self, item)

a = listNoAppend()
# a.append('aaa')    #

# 多继承
"""
继承关系如下的几个类:
                D(a=1)
            /        \
        B               C(a=2)
            \        /
                A

class D():
    def __init__(self):
        self.a = 1

class B(D):
    pass

class C(D):
    def __init__(self):
        self.a = 2

class A(B, C):
    pass
b = A()
print b.a   # 1
"""
# 在经典对象模型中，方法和属性的查找链是按照从左到右，深度优先的方式进行查找。所以当A的实例b
# 要使用属性a时，它的查找顺序为:A->B->D->C->A，这样做就会忽略类C的定义a, 而先找到的基类D的
# 属性a
"""
class D(object):
    def __init__(self):
        self.a = 1

class B(D):
    pass


class C(D):
    def __init__(self):
        self.a = 2


class A(B, C):
    pass


b = A()
print b.a   # 2

# 新的对象模型采用的是从左到右，广度优先的方式
# 进行查找，所以查找顺序为A->B->C->D，可以正确的返回类C的属性a。

# 这个顺序的实现是通过新式类中特殊的只读属性__mro__，类型是一个元组，保存着解析顺序信息。只能通过
# 类来使用，不能通过实例调用。
print A.__mro__   # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <type 'object'>)
"""

"""
# 协作式调用父类方法
class A(object):
    def go(self):              # 6
        print "go A go!"

class B(A):
    def go(self):               # 2
        print "go B go!"        # 7
        A.go(self)


class C(A):
    def go(self):               # 4
        print "go C go!"        # 6
        A.go(self)


class D(B, C):
    def go(self):
        print "go D go!"     # 8
        B.go(self)
        C.go(self)

d = D()
d.go()
"""
# go D go!
# go B go!
# go A go!
# go C go!
# go A go!
# 从结果看, 执行了两次

# 使用super
class A(object):
    def go(self):              # 6
        print "go A go!"

class B(A):
    def go(self):               # 2
        super(B, self).go()     # 3
        print "go B go!"        # 7


class C(A):
    def go(self):               # 4
        super(C, self).go()     # 5
        print "go C go!"        # 6


class D(B, C):
    def go(self):
        super(D, self).go()  # 1
        print "go D go!"     # 8

d = D()
d.go()
# go A go!
# go C go!
# go B go!
# go D go!
# super()可以看成是更加安全调用父类方法的一种新方式。