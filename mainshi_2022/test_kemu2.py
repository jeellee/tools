print((False == 0))


# 加密算法

def myFun(srcSent, offset):
    def enCrypt(aChar):
        op = lambda x: chr((ord(aChar) - x + offset) % 26 + x)
        return op(97) if str.islower(aChar) else (op(65) if str.isupper(aChar) else aChar)
    return ''.join(map(enCrypt, srcSent))

"""
In [11]: str.islower('3')
Out[11]: False

In [12]: str.isupper('3')
Out[12]: False

数字3 时 直接返回3
"""


# import os
# fobj = open('test.txt', 'r')
# while True:
#     aline = input('enter a line (. quit):')
#     if aline != '.':
#         fobj.write('%s%s' % (aline, os.linesep))
#     else:
#         break

print((True or False))
print((True or False and False))  # True  and 优先级大于 or

tuple1 = (20)

print((type(tuple1)))   # int类型

tuple2 = (20,)
print((type(tuple2)))   # tuple类型 一个元素时必须加,号

tuple3 = ()
print((type(tuple3)))   # tuple类型



aaa = "Runobb"
print((1, aaa[0:-1]))
print((2, aaa[-1:0]))
# R u n o  b  b
# 0 1 2 3  4  5
# -6  -5  -4  -3   -2   -1   # 从后往前数

print((3, aaa[0:-2]))
print((4, aaa[0:-6]))
print((5, aaa[0:5]))   # 右不包含
print((5, aaa[0:6]))   # 右不包含
print((5, aaa[0:7]))   # 右不包含


# 向下取整 取小
print((9 // 2))   # 4
print((-9 // 2))   # -5

# == is区别
# 字符窜
stra = 'abcd'
strb = 'abcd'
print((stra is strb))   # True 字符窜有缓存，不是引用，比较的是值，实际没有is这种比法 相当于==

# 字典
"""
In [40]: a = {'a': 1, 'b': 2}

In [41]: b = {'b': 2, 'a': 1}

In [42]: a == b
Out[42]: True

In [43]: a is b
Out[43]: False

In [44]: id(a)
Out[44]: 116319744

In [45]: id(b)
Out[45]: 116364992
-------------------------------------
In [46]: stra = 'abcd'

In [47]: strb = 'abcd'

In [48]: stra is strb
Out[48]: True

In [49]: id(stra)
Out[49]: 112107184

In [50]: id(strb)
Out[50]: 112107184

--------------------------------------------
In [52]: {'a': 1, 'b': 2} == dict({'a': 1, 'b': 2})
Out[52]: True

In [53]: {} == dict()
Out[53]: True

"""

# 科目二真题
# 001
x = {1, 2, 3, 4, 5}
# x.remove(2)   # 不存在时报错
# print('001', x)

# del x[2]
# print('001', x)

x.discard(2)   # set专用 不存在时不报错
print('001', x)

# x.pop(2)  # 方法不存在

"""
In [1]: ([1,2],1,2)
Out[1]: ([1, 2], 1, 2)

In [2]: {[1,2],1,2}    # set中元素是唯一的，list是可变对象，无法判断是否唯一
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-4d4615845542> in <module>
----> 1 {[1,2],1,2}

TypeError: unhashable type: 'list'

In [3]: {(1,2),1,2}
Out[3]: {(1, 2), 1, 2}

In [4]: {[1,2]:1,1:2,2:3}      # 字典的key是不可变的
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-35ec4648d287> in <module>
----> 1 {[1,2]:1,1:2,2:3}

TypeError: unhashable type: 'list'
"""

# 位运算符
# 位运算符是用来操作二进制的。
# 位运算共有 & | ^ ~ << >>六种操作方法
# <<（左移）
# 将数字转化为二进制后，向二进制里添加几个零（取决于左移的位数），再返回变换后二进制对应的数。

# >>（右移）
# 将数字转化为二进制后，将二进制里最后面的几个数剔除（取决于右移的位数），再返回变换后二进制对应的数。
# 1 --> 0      删除， 向右，删除1
print(1 >> 2)  #
# 1  --> 001   添加0，向左，箭头也向左， 添加2个0（向左添加2个0，向右添加没有意义）
print(1 << 2)

print(1 << 2 >> 1)   # 1  -> 001  -> 01

# for...else...  for正常结束（包括for的对象是空列表）时，才执行else，非正常结束不执行
"""
In [9]: for i in []:
   ...:     print('aaa')
   ...: else:
   ...:     print('bbb')
   ...:
bbb

In [10]: for i in [1]:
    ...:     print('aaa')
    ...: else:
    ...:     print('bbb')
    ...:
aaa
bbb

In [11]: for i in [1]:
    ...:     print('aaa')
    ...:     break
    ...: else:
    ...:     print('bbb')
    ...:
aaa
"""

# -可迭代对象  迭代器
# 凡是可以使用for...in的都是可迭代对象  可以使用next的是迭代器
"""
In [54]: data = [1,2,3,4,5]
In [60]: from collections.abc import Iterable, Iterator

In [61]: isinstance(data, Iterable)
Out[61]: True

In [63]: isinstance(data, Iterator)   # 不是迭代器，不能使用next
Out[63]: False

In [65]: iter(data)                  # 转换为迭代器 可使用next
Out[65]: <list_iterator at 0x6f35dc0>

In [66]: data2 = iter(data)

In [67]: isinstance(data2, Iterable)
Out[67]: True

In [68]: isinstance(data2, Iterator)
Out[68]: True

In [69]: iter(data2, 3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-69-90695fb0542a> in <module>
----> 1 iter(data2, 3)

TypeError: iter(v, w): v must be callable

In [70]: data2.next()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-70-59f3a57a3042> in <module>
----> 1 data2.next()

AttributeError: 'list_iterator' object has no attribute 'next'

In [71]: data2
Out[71]: <list_iterator at 0x6af2a90>

In [72]: [i for i in data2]
Out[72]: [1, 2, 3, 4, 5]

In [73]: next(data2)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-73-000eabdf7c3d> in <module>
----> 1 next(data2)

StopIteration:

In [74]: data2 = iter(data)

In [75]: next(data2)
Out[75]: 1

----------------------------
In [76]: data3 = (1,2,3,4,5)

In [77]: isinstance(data3, Iterable)
Out[77]: True

In [78]: isinstance(data3, Iterator)
Out[78]: False

----------------------------生成器
In [85]: def func(data):
    ...:     for i in data:
    ...:         yield i
    ...:

In [86]: data4=func([1,2,3,4,5])

In [87]: data4
Out[87]: <generator object func at 0x0000000006761C80>

In [88]: isinstance(data4, Iterable)   # 可迭代
Out[88]: True

In [89]: isinstance(data4, Iterator)   # 也是迭代器，可以使用next
Out[89]: True

In [91]: next(data4)
Out[91]: 1
"""

# -列表切片赋值
"""
In [93]: res = [1,2,3,4,5]

In [94]: res[1:3]='abc'       # 左闭右开  2，3会分别替换a，b， 还会新增c

In [95]: res
Out[95]: [1, 'a', 'b', 'c', 4, 5]

In [101]: res = [1,2,3,4,5]

In [102]: res[1:1]='abc'

In [103]: res
Out[103]: [1, 'a', 'b', 'c', 2, 3, 4, 5]

------------------------- # 要替换某个值 得用赋值
In [104]: res = [1,2,3,4,5]

In [105]: res[1]='abc'

In [106]: res
Out[106]: [1, 'abc', 3, 4, 5]
"""

# -match search
"""
In [107]: pattern='back'

In [108]: import re

In [109]: re.match(pattern, 'backup')  # 从头匹配，匹配到pattern 返回不为空
Out[109]: <re.Match object; span=(0, 4), match='back'>

In [110]: re.search(pattern, 'backup')
Out[110]: <re.Match object; span=(0, 4), match='back'>

In [111]: re.search(pattern, 'txt.backup')
Out[111]: <re.Match object; span=(4, 8), match='back'>

In [112]: re.match(pattern, 'txt.backup')

In [113]:
"""

# -列表一边循环 一边删除
"""
In [113]: data=[1,2,3,4,5]

In [114]: for i in data:
     ...:     data.remove(i)
     ...:

In [115]: print(data)
[2, 4]

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
        nonlocal b
        print('inner b:', b)
        b = 20
        global a
        a = 1000
    inner()
    print('outer b:', b)

outer()
print('a: ', a)
