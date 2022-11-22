# coding: utf-8

"""
函数重载主要是为了解决两个问题。

1. 可变参数类型
2. 可变参数个数

对于1. python 可以接受任何类型的参数，如果函数的功能相同，那么不同的参数类型在 python 中很可能是相同的代码，没有必要做成两个不同函数
对于2. 对那些缺少的参数设定为缺省参数即可解决问题

所以1和2 都有了解决方案, python自然不需要重载
"""

a = [1, 2, 3, 4]
# a.extend((7, 8, 9))    # [1, 2, 3, 4, 8, 9, 7]
"""
    def extend(self, iterable): # real signature unknown; restored from __doc__
"""
a.extend({7: 10, 8: 10, 9: 10})    # # [1, 2, 3, 4, 8, 9, 7]
print(a)


class Duck:
    def quack(self):
        print("Quaaaaaack!")


class Bird:
    def quack(self):
        print("bird imitate duck.")


class Doge:
    def quack(self):
        print("doge imitate duck.")


def in_the_forest(duck):
    duck.quack()

duck = Duck()
bird = Bird()
doge = Doge()
for x in [duck, bird, doge]:
    in_the_forest(x)

# 我们并不关心对象是什么类型，到底是不是鸭子，只关心行为。
# 有这个行为, 就正确执行, 没有就报错, 不检查参数类型
