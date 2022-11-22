import contextlib
import time


class TimeIt(contextlib.AbstractContextManager):
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(("Running cost seconds ", time.time() - self.start))


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
        print(("param is zero", e))
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
print((example.__name__))   # wrapper
print((example.__doc__))   # None


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

# __all__

from test_kemu2_3 import A, B    # B在__all__中未定义，指定import B 的时候会导入,不会报错

a = A()
b = B()

print(a)
print(b)


# __del__    # 内存不需要的时候，才调用这个方法（当对象还有引用时，不会调用）

# subprocess 模块  windows
# 验证路径前应该先将其标准化？？
# 变量作用域， 必考
# mock path要考

# try...except
try:
    print()        # 执行代码
    # raise          # 不正确，必须指定异常
except:
    raise       # 发生异常时执行的代码
else:
    pass        # 未发生异常时执行的代码
finally:
    pass        # 不管有没有异常都会执行的代码

# 在except中raise时，可以不带异常（抛出的是当前捕获的异常），
# 不在except中raise时，必须带异常

# -字典删除的方法
{}.pop()   # 带key参数
{}.clear()
del {}['a']
{}.popitem()
"""
In [13]: data={'a':1}

In [14]: data.popitem()
Out[14]: ('a', 1)

In [15]: data={'a':1, 'b': 2}

In [16]: data.popitem()
Out[16]: ('b', 2)

In [17]: data={'a':1, 'b': 2}

In [18]: data.pop()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-18-9e84b3a8fb7e> in <module>
----> 1 data.pop()

TypeError: pop expected at least 1 argument, got 0

In [19]: data.pop('a')
Out[19]: 1

In [20]: data
Out[20]: {'b': 2}
"""
[].clear()
[].pop(1)   # 索引
[].remove('obj')   # 成员
del [][0]

set().remove('obj')
set().pop()
set().clear()
set().discard('obj')  # 没有时不报错

t = (1,)   # 不变得，没有删除方法
# del t[0]   # 报错，不支持
del t  # 可以删除这个t变量

# -禁止使用jsonpickle
# -禁止使用simplejson的scanstring模块
# -解析xml时 使用参数resolve_entities
# -禁止使用私有 或 弱加密算法， 如DES MD5等？？还有啥
# -使用/dev/random生产安全随机数 还可以使用secrets模块  os.urandom在linux下不安全 windows下安全
# -函数参数多时， 使用class、namedtuple、dataclass进行封装
# -包与模块的引用？？importlib

# -round 四舍五入
"""
In [28]: round(1.4)
Out[28]: 1

In [29]: round(1.5)
Out[29]: 2

In [30]: round(1.6)
Out[30]: 2

In [31]: round(1.9)
"""

# -server端发起请求之前要验证SSRF漏洞

# -使用tempfile.mkstemp 不要使用tempfile.mktemp

# -函数定义 函数参数
"""
In [32]: def func(**args, a=1):     # 带默认值类型的参数 必须放在最后
    ...:     pass
  File "<ipython-input-32-7237a7a5d1f0>", line 1
    def func(**args, a=1):
                     ^
SyntaxError: invalid syntax


In [33]: def func(*args, a=1):
    ...:     pass
    ...:

In [34]: def func(a=1, *args):
    ...:     pass
    ...:
    ...:

In [35]: func(a=1, 1)           # 可以定义，某些情况下 不能使用
  File "<ipython-input-35-9909481d3bac>", line 1
    func(a=1, 1)
              ^
SyntaxError: positional argument follows keyword argument


In [36]: func(a=1, (1,2))
  File "<ipython-input-36-11426b66e46b>", line 1
    func(a=1, (1,2))
              ^
SyntaxError: positional argument follows keyword argument


In [37]: func(1, (1,2))

In [38]: def func(a=1, **args):
    ...:     pass
    ...:
    ...:

In [39]: func({'a': 1, 'b': 2})

"""

# -调用外部程序会命令使用绝对路径
import subprocess
# subprocess.run(['gcc', '--version'], shell=False)  # 错误
subprocess.run(['/usr/bin/gcc', '--version'], shell=False)  # 正确


# -代码覆盖率最高的是：组合覆盖， 其他的语句、条件、判定


# -禁止代码中包含公网地址（任何公网，不止huawei，如www.baidu.com）,可以使用配置方式
# 例外情况：xml中需要指定的  标准协议必须制定的等


# -日志：不能记录明文口令 秘钥，加密的也不行

# -等价类测试 todo
# -数据组合测试 todo 单一选择组合




