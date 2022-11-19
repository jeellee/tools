print(False == 0)


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

print(True or False)
print(True or False and False)  # True  and 优先级大于 or

tuple1 = (20)

print(type(tuple1))   # int类型

tuple2 = (20,)
print(type(tuple2))   # tuple类型 一个元素时必须加,号

tuple3 = ()
print(type(tuple3))   # tuple类型



aaa = "Runobb"
print(1, aaa[0:-1])
print(2, aaa[-1:0])
# R u n o  b  b
# 0 1 2 3  4  5
# -6  -5  -4  -3   -2   -1   # 从后往前数

print(3, aaa[0:-2])
print(4, aaa[0:-6])
print(5, aaa[0:5])   # 右不包含
print(5, aaa[0:6])   # 右不包含
print(5, aaa[0:7])   # 右不包含


# 向下取整 取小
print(9 // 2)   # 4
print(-9 // 2)   # -5

# 字符窜
stra = 'abcd'
strb = 'abcd'
print(stra is strb)   # True 字符窜有缓存，不是引用，比较的是值，实际没有is这种比法 相当于==






