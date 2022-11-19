# coding: utf-8

"""
排序算法:
O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) (指数级的算法是非常的慢的 )
快速排序和冒泡排序
"""

a = [42, 41, 94, 28, 27, 89, 48, 1, 29, 54, 33, 64, 60, 70, 89, 97, 53, 12, 29, 5]


"""
快速排序 O(n*logn)级别的计算
"""
# 以42为基准, 小与他的放到左边, 大于他的放到右边
# 不能直接操作arr, 只能操作下标

# 第一种方式(个人J觉得不好理解)
def quick_sort_1(arr):
    if len(arr) > 1:
        qsort(arr, 0, len(arr) - 1)


def qsort(arr, start, end):
    base = arr[start]
    pl = start
    pr = end
    while pl < pr:
        while pl < pr and arr[pr] >= base:
            pr -= 1
        if pl == pr:
            break
        else:
            arr[pl], arr[pr] = arr[pr], arr[pl]

        while pl < pr and arr[pl] <= base:
            pl += 1
        if pl == pr:
            break
        else:
            arr[pl], arr[pr] = arr[pr], arr[pl]

    # now pl == pr
    if pl - 1 > start:
        qsort(arr, start, pl - 1)
    if pr + 1 < end:
        qsort(arr, pr + 1, end)

arr = []
l = 0
r = len(arr)-1
base = arr[l]
def m_quick_sort(arr, l, r):
    while l < r:
        if arr[r] > base:
            r -= 1

        if arr[l] < base:
            l -= 1

        arr[l], arr[r] = arr[r], arr[l]







# print a
# quick_sort(a)
# print a


# 第二种方式(好理解)

def quick_sort_2(arg):
    if arg == []:
        return []
    bigList = []
    smallList = []
    middle = arg[0]
    for i in arg[1:]:
        if i <= middle:
            smallList.append(i)
        else:
            bigList.append(i)
    return quick_sort_2(smallList)+[middle]+quick_sort_2(bigList)
# print quickSort(a)


"""
冒泡排序, 一次排序将最小的那个找出来,放在0位置(挨个找余下的最小1个，一个个放)
二次排序, 从1位置开始挨个对比

n + (n-1) + (n-2) + ... + 1 = n(n-1)/2

O(n^2)级别的计算
"""
def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
            print lists
    return lists

# bubble_sort(a)


"""
插入排序

描述
插入排序的基本操作:
一位一位的计算, 每计算到下一位, 就和前面已经排好的数据进行比较, 放在合适的位置即可
  |
4 5 2 4 9 8 1
j i
        |
4    5  2 4 9 8 1
j-1  j  i
1 + 2 + ... +(n-1) + n = n(n+1)/2
O(n^2)级别的计算
"""
def insert_sort(lists):
    for i in range(1, len(lists)):
        j = i-1
        while j >= 0:
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
                j -= 1
            else:
                break
    return lists

# insert_sort(a)
# print lists


"""
直接选择排序

描述
每一次都选出最小的那个数 与第一个数交换, 交换后, 从第二数开始再次循环
4      1 2 4 9 8 5
i      j
min
-------
i      j
       min
O(n^2)级别的计算
"""

def select_sort(lists):
    for i in range(len(lists)):
        min = i
        for j in range(i+1, len(lists)):
            if lists[j] < lists[min]:
                min = j
                lists[i], lists[min] = lists[min],lists[i]
    return lists

# select_sort(a)



# O(n*logn)级别的计算是如何计算的?
def nlogn_sort(n):
    count = 1
    sz = 1
    while sz < n:
        sz *= 2
        for i in range(n):
            print 'nlogn_sort, ', count
            count += 1

# nlogn_sort(100)


# 素数（没有除1和自身外的约数）判断  O(sqrt(n))级别的计算(开根号)
def is_prime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            # print 'i-----', i
            return False
        i += 1
    return True

# print is_prime(113)



"""
binary_search  二分查找法:
先排序, 然后一半一半的查找
"""



"""
时间复杂度为O(logn)的运算:
求x的n次方

每次减半, 没有别的复杂运算, 复杂度为O(logn), 如果直接连乘的话, 复杂度为O(n)

这两种复杂度是有本质的差别的
"""
def pow(x, n):
    # assert n > 0
    if n == 0:
        return 1.0
    t = pow(x, n/2)  # 2^5
    if n%2 != 0:
        return x*t*t
    return t*t
print pow(2, 5)


if __name__ == '__main__':
    import time, math, random
    for i in range(10, 16):
        arry_len = int(math.pow(2, i))
        arry = [random.randint(1, math.pow(2, i)) for _ in range(arry_len)]
        start = time.time()
        # quick_sort_2(arry)
        # quick_sort_1(arry)
        # select_sort(arry)
        print '2^%s: %s spend time: %s' % (i, arry_len, time.time()-start)