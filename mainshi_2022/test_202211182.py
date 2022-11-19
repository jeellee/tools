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

