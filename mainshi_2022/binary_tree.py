# -*- coding: utf-8 -*-

"""
二叉树:
二叉树的遍历, 前中后的分别是根据根节点所在位置判断, 并且遍历必须都是先左后右
根在前: 前序遍历 -->  根左右
根在中: 中序遍历 -->  左根右
根在后: 后序遍历 -->  左右根
"""

"""
前序遍历: 10 6 4 8 14 12 16
中序遍历: 4 6 8 10 12 14 16

推出后序遍历:
4 8 6 12 16 14 10
"""

class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def construct_tree(pre_order, mid_order):
    if len(pre_order) == 0:
        return None
    # 前序遍历的第一个节点, 一定是根节点
    root_data = pre_order[0]
    for i in range(0, len(mid_order)):
        if mid_order[i] == root_data:
            break
    # 递归构造左子树和右子数
    left = construct_tree(pre_order[1:1+i], mid_order[:i])
    right = construct_tree(pre_order[1+i:], mid_order[i+1:])
    return Node(root_data, left, right)

pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
mid_order = [4, 7, 2, 1, 5, 3, 8, 6]

# root = construct_tree(pre_order, mid_order)
# print root.__dict__
# print root.data
# print root.left.data
# print root.right.data
#
# print root.left.left.data
# print root.left.left.right.data


"""
二叉树:
（Binary Tree）是树的一种特殊形式，也就是每个节点之下最多拥有2个孩子，相应地若最多不超过M个孩子，那就成为M叉树，但实际上我们统称为多叉树。
对于二叉树，常用的定理有四条：

深度为i的二叉树最多含有2i−1 个节点；
第i层至多有2i−1个节点；
对于任意一颗二叉树，若其终端节点数为n0,度为2的节点数为n2,则n0=n2+1。证明如下：

（1）n=n0+n1+n2
（2）n=B+1（B为分支总数）
（3）B=n1+2n2
由上述三式即可得出此定理。

对于一棵完全二叉树（除最后一层外每一层都为满二叉树）而言，其叶子节点数具有以下关系：
n0=n2（当n为偶数时）或n+12（当n为奇数时）

"""


"""
链表:
链表（linked list）是一组数据项的集合，其中每个数据项都是一个节点的一部分，每个节点还包含指向下一个节点的链接。
根据结构的不同，链表可以分为单向链表、单向循环链表、双向链表、双向循环链表等

实现:
我们都知道，数组是连续列表，链表是链接列表，二者在概念和结构上完全不同，因此list不能用于实现链表。
在C/C++中，通常采用“指针+结构体”来实现链表；而在Python中，则可以采用“引用+类”来实现链表。
在下面的代码中，SinCycLinkedlist类代表单向循环链表，Node类代表链表中的一个节点：
"""

"""
队列:
双端队列（deque，全名double-ended queue）是一种具有队列和栈性质的线性数据结构。双端队列也拥有两端：队首（front）、队尾（rear），
但与队列不同的是，插入操作在两端（队首和队尾）都可以进行，删除操作也一样。

实现:
在Python中，有两种方式可以实现上述的双端队列ADT：使用内建类型list、
使用标准库collections.deque（其实collections.deque就是Python中双端队列的标准实现）。
"""

"""
栈:
（Stack）是限定只能在表的一端进行插入和删除操作的线性表。
"""


"""
堆排序:
堆排序作是基本排序方法的一种，类似于合并排序而不像插入排序，它的运行时间为O(nlogn)，
像插入排序而不像合并排序，它是一种原地排序算法，除了输入数组以外只占用常数个元素空间。
堆（定义）：（二叉）堆数据结构是一个数组对象，可以视为一棵完全二叉树。如果根结点的值大于（小于）其它所有结点，
并且它的左右子树也满足这样的性质，那么这个堆就是大（小）根堆。
"""


"""
扑克牌中的顺子
1, 2,3,  14 0, 0
"""

def poker(p_list):
    if not p_list or len(p_list) < 3:
        return False

    zero_num = p_list.count(0)
    p_list.sort()
    for i in range(zero_num):
        p_list.remove(0)

    for i in range(len(p_list)):
        if p_list[i] and p_list.count(p_list[i]) > 1:    # 有两张以上相同的牌(对子), 就不是顺子
            return False

        if i > 0 and p_list[i] - p_list[i-1] > 1:
            if zero_num > 0:
                zero_num -= 1
            else:
                return False
    return True

p_list = [1, 4, 5, 0, 0]
print(poker(p_list))

"""
判断闰年
"""
def is_run(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(("{0} 是闰年".format(year)))   # 整百年能被400整除的是闰年
            else:
                print(("{0} 不是闰年".format(year)))
        else:
            print(("{0} 是闰年".format(year)))       # 非整百年能被4整除的为闰年
    else:
        print(("{0} 不是闰年".format(year)))

# is_run(2016)

