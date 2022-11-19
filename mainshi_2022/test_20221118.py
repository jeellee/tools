# encoding: utf-8
# 3.1.2 字符串格式化
# 简单字符串使用+号即可
# 复杂使用format和f,尽量避免使用%
print(f"{1}")
print("hello {}".format("world"))
print("hello {name}".format(name="aaa"))

# 合理使用字符串引号
# 同一文件使用一种 单引号或双引号， 尽量不使用转义
# 多行使用三引号的双引号（文件中本身都使用单引号时，可以使用三重单引号）

print("a dsdas dasda dsadas "
      "dsadasda")


# 不使用难以理解的字面量
value = 1000  # 错误
minutes = 1
# FIXME: 待修改缺陷，合入代码时去掉
# TODO: 待完备事项，合入代码时去掉
seconds = minutes * 1000   # 正确

# 使用if seq  和 if not seq判断序列是否为空

if []:
    print("aaa")

if not []:
    print("bbbb")

# 字符串切割，尽量不使用负数切割， 且把切割和步进分开写

mylist = [1, 2, 3, 4, 5, 6]
mylist2 = mylist[::2]
mylist3 = mylist2[1:3]

# 反转列表例外 [::-1]


# 字典键值 不要相同，后面会覆盖前面的


# 字典取值，不建议直接使用[]
# 正确，用异常捕获
data = dict()
try:
    value = data["key"]
except KeyError:
    pass

# s使用get

# 使用defaultdict
from collections import defaultdict
data = defaultdict(str)
print(data["key"])  # 有默认值 不会报错

# 代码层面上 key一定存在时 可以使用[]

# 使用isinstance判断类型，不使用type
# 优先使用内置类型判断

callable(object)
from collections.abc import Container
isinstance(object, Container)



# 不使用 == 判断对象是否相等
# is判断是否指向同一个对象（判断两个对象id是否相等）， ==会调用__eq__方法判断是否等价（判断两个对象的值是否相同）
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if hasattr(other, "age"):
            return self.age == other.age

# 使用==判断内置类型的值是否相等，不要使用is 和 is not



# 隐式bool值
# 为False的值： None False 0， 0.0， 0j， '', (), [], {}, set(), range(0), range(8,5)
# 对象定义了__bool__切返回False，对象定义了__len__切返回0

# lambda不超过1行


# 不要把lambda赋值给变量，不便于调试



# 同一个函数 返回值，统一为显示或隐式
# 返回类型要一致
# 错误
def test(a):
    if a > 0:
        return "aaaa"

# 正确
def test(a):
    if a > 0:
        return "aaaa"
    return None


# 避免在条件和循环中有过多的判断，可以将判断分成多个表达式



# 禁止使用可变对象作为参数默认值
def test(args=[]):  # 错误
    pass

# 正确
def test1(args=None):
    args = args or []


# 类的私有变量是__双下划线  保护的变量是_单下划线
# 私有 表示仅允许在本类使用
# 保护 表示仅允许在本类和继承类使用


# 未实现数值运算符的 魔法方法时，要return NotImplemented 而不是抛出NotImplementedError
# return NotImplemented解释器会自动使用关联（后备）的方法， 如 def __eq__(self, other):



class Entity:
    def __init__(self, eid, name, age):
        self.__eid = eid
        self._name = name
        self.age = age

class EntityA(Entity):
    def get_name(self):
        return self._name
    def get_age(self):
        return self.__age   # 父类私有变量，不能被继承

obj_a = EntityA(1, "lijie", 13)
print(obj_a.get_name())

print(obj_a._name)  # 保护的变量，不建议直接使用


# try except
# 只将 可能引发一场的最少代码放入try except
try:
    a = 1  # 不会有异常，应该放外面
    b = 0  # 不会有异常，应该放外
    res = a / b
except ZeroDivisionError as e:
    raise Exception("aaa") from e


# 禁止通过异常捕获泄露敏感信息，即在捕获时打印敏感信息


# 不要在finally中 return， 否则有异常时，不会抛出


# 禁止对一个包的导入， 及使用绝对导入 又使用相对导入

# from third_lib import module_a   三方库使用绝对路径导入，正确
# from huawei_sdk import module_b    二方库使用绝对路径导入， 正确
# 本项目库可以使用相对路径导入  from .module_c import aaa

# 同时具备 可执行 可导入的文件内， 使用相对导入，会发生导入错误  ！！！！

# 如
# !/usr/bin/env python3
# import sys
# from . import model   会报错

# 导入耗时较高的模块 可以使用from import 单独导入所需方法


# copy deepcopy
# 对于数字 字符和其他原子类型对象，没有拷贝的说法， 对其重新赋值，也只是重新创建一个对象而已，替换掉旧的


# 修改sys.path
# 建议使用sys.path.append  或 修改PYTHONPATH环境变量
# 建议从项目或 子项目的根目录 开始加入搜索路径
# sys.path.append  sys.path.extend


# 读写文件
"""
r 读取   r+ 可读可写， 光标在开始，需移动光标到结尾
w 写入  已存在时会清空文件   w+ 可都可写 会清空已有文件
x 独暂时创建， 存在时会失败
a 从文件结尾添加
+ 更新 可读可写

可进行组合使用
"""
# 会清空
with open("aaa.txt", "w", encoding="utf-8") as f:
    f.write("aaa")

# 不清楚编码时 可以使用三方库charset辅助检测
# 或者列出所有可能的 编码格式  逐一尝试读取


# 临时文件
# 不使用有风险的tempfile.mktemp  使用安全的 mkstemp mkdtemp NamedTemporaryFile


# logging模块
# 建议使用logging.info("this is log: %s", "aaa")方式，会存在懒插值，比较好
# 不要使用logging.info("this is log: %s" % "aaa")方式

# 禁止在日志中记录 口令 秘钥 包括加密的秘钥和口令  使用***代替


# 合并字符串
# 追求性能 用list.append + str.join()
# 追求时间 用+ +=

# list成员个数较大时， 使用固定大小创建list

# tuple性能比list好  更快  更省内存

# 安全随机数
# 禁止使用random模块用于安全加密中，因为生成的是伪随机数，是高斯分布或均匀分布等 不适真正的随机数， 但在windows下是安全的，可以使用
# 1-建议使用3.6版本以上系统提供的 os.urandom生成安全随机数
# 2-或者使用secrets模块生成


# 使用ssl.SSLSocket 代替socket.Socket
# 传输数据不敏感时 使用普通的就可以，性能较好
# 已经经过适当加密时，可以使用
# 整个网络是可信时，可以使用











