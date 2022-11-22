# coding: utf-8
"""
最大公约数
最小公倍数

由于两个数的乘积等于这两个数的最大公约数与最小公倍数的积。
即（a，b）×[a，b]=a×b。所以，求两个数的最小公倍数，就可以先求出它们的最大公约数，然后用上述公式求出它们的最小公倍数。
"""
a = 36
# 1 2 3 4 6 9 12 18
b = 21
# 1 3 7


def max_common(a, b):
    # 36 % 21  15
    # 21 % 15  6
    # 15 % 6   0
    while b:
        a, b = b, a % b
    return a

print(max_common(a, b))


def min_Common(a, b):
    c = a*b
    while b:
        a,b = b, a%b
    return c//a


print(min_Common(a, b))


"""
中位数
"""

# def median(data):
#     data.sort()
#     half = len(data) // 2
#     return (data[half] + data[~half])/2
#
# l = [1,3,4,53,2,46,8,42,82]
#
# # print median(l)
#
# data = [1, 2, 3, 4, 8, 42, 46, 53, 82, 27]
#
# print data[~5]
#
# print 5
# print ~4


def extend_list(val, list=[]):
    list.append(val)
    return list


list1 = extend_list(10)
print(list1)     # [10]
list2 = extend_list(123, [])
print(list2)     # [123]
list3 = extend_list('a')
print(list3)     # [10, 'a']
print("--------------")
print(list1)    # list1 = [10, 'a']
print(list2)    # list2 = [123]
print(list3)    # list3 = [10, 'a']


class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print((Parent.x, Child1.x, Child2.x))  # [1,1,1]
Child1.x = 2
print((Parent.x, Child1.x, Child2.x))  # [1,2,1]
Parent.x = 3
print((Parent.x, Child1.x, Child2.x))  # [3,2,3]

