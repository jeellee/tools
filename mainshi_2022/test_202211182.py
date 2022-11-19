import contextlib
import time


class TimeIt(contextlib.AbstractContextManager):
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Running cost seconds ", time.time() - self.start)


with TimeIt():
    test = [i for i in range(100000)]


# 不要在finally中 return， 否则有异常时，不会抛出
def control_statement_in_finally(param):
    ret = -1
    try:
        ret = 1 / param
    finally:
        return ret


def control_statement_in_finally2(param):
    ret = -1
    try:
        ret = 1 / param
    except ZeroDivisionError as e:
        print("param is zero", e)
        raise
    finally:
        return ret


# control_statement_in_finally(0)
control_statement_in_finally2(0)

# 要保证finally中代码能够正常结束， 不出现异常


# 装饰器
# 建议使用 functools.wraps
# 使用一般装饰器 会改写被装饰部分的属性  如__name__ __doc__等

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("aaaaaa")
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    """this is example"""


example()
print(example.__name__)   # wrapper
print(example.__doc__)   # None


from functools import wraps


def my_decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("aaaaaa")
        return func(*args, **kwargs)
    return wrapper


# 为启动文件 添加硬编码启动头 #！/usr/bin/python3.7  明确解释器版本
# 如果文件只是子项目，不作为启动文件，则不建议添加


# 禁止在代码中 包含公网地址 ip等


"""
In [19]: 4>False
Out[19]: True

In [20]: 4>True
Out[20]: True

In [21]: 4>3==2
Out[21]: False

In [22]: 4>3==2
Out[22]: False

In [23]: 4>3==3
Out[23]: True

In [24]: 3==2
Out[24]: False

In [25]: 4>3 and 3==2   # 4>3==2这个写法 相当于 4>3 and 3==2  （类似  b < a < c 即 b < a and a < c）
Out[25]: False

In [26]: 4>3 and 3==3
Out[26]: True

# 虚数不支持
In [27]: 5+4j > 2-3j
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-27-c20bc1df3d84> in <module>
----> 1 5+4j > 2-3j

TypeError: '>' not supported between instances of 'complex' and 'complex'

In [28]: (5+4j) > (2-3j)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-28-e6adf29dab3e> in <module>
----> 1 (5+4j) > (2-3j)

TypeError: '>' not supported between instances of 'complex' and 'complex'

# 元组 也不支持比较啊？？？
In [30]: (3,2) < ('a','b')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-30-6ebae767d474> in <module>
----> 1 (3,2) < ('a','b')

TypeError: '<' not supported between instances of 'int' and 'str'

In [31]: (3,2)<('a','b')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-413b366b1901> in <module>
----> 1 (3,2)<('a','b')

TypeError: '<' not supported between instances of 'int' and 'str'

# 挨个比较 ascii值
In [32]: 'abc'>'xyz'
Out[32]: False

In [33]: 3>2>2
Out[33]: False

In [34]: ord('a')
Out[34]: 97

In [35]: ord('x')
Out[35]: 120

In [36]: 'abc'<'xyz'
Out[36]: True

# 挨个比较 数字
In [37]: (3,2)<(3,1)
Out[37]: False

In [38]: (3,2)>(3,1)
Out[38]: True

In [39]: (3,2)>(3,3)
Out[39]: False

In [40]: (3,2)>(2,3)
Out[40]: True

# 对对象中每个值乘
In [41]: ('hi')*4   # ('hi')没加逗号 相当于一个单字符窜
Out[41]: 'hihihihi'

In [42]: ('hi',)*4
Out[42]: ('hi', 'hi', 'hi', 'hi')

In [43]: ['hi']*4
Out[43]: ['hi', 'hi', 'hi', 'hi']

In [44]: [['hi']]*4
Out[44]: [['hi'], ['hi'], ['hi'], ['hi']]

"""