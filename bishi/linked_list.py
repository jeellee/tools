#!coding=utf-8

"""
定义链表
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, x):
        next_node = ListNode(x)
        self.next = next_node
        return next_node

    def print_list(self):
        print(self.val)
        next_node = self.next
        while next_node:
            print(next_node.val)
            next_node = next_node.next


def func1():
    # ll = [1, 2, 3]
    node = ListNode(1)
    node1 = node.add(2)
    node1.add(3)

    node.print_list()


# ===========================

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(node.val)
            node = node.next
        # print("->".join(nodes))
        return "->".join(nodes)

    def __str__(self):
        return self.__repr__()


def func2():
    lll = LinkedList()
    first_node = Node("1")
    second_node = Node("2")
    third_node = Node("3")

    lll.head = first_node
    first_node.next = second_node
    second_node.next = third_node

    print(lll)


if __name__ == "__main__":
    func2()

