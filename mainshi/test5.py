# coding: utf-8

"""
duck typing
鸭子 类型
"""

a = [1, 2, 3, 4]
# a.extend((7, 8, 9))    # [1, 2, 3, 4, 8, 9, 7]
"""
    def extend(self, iterable): # real signature unknown; restored from __doc__
"""
a.extend({7: 10, 8: 10, 9: 10})    # # [1, 2, 3, 4, 8, 9, 7]
print a


class Duck:
    def quack(self):
        print "Quaaaaaack!"


class Bird:
    def quack(self):
        print "bird imitate duck."


class Doge:
    def quack(self):
        print "doge imitate duck."


def in_the_forest(duck):    # 参数是一个类的实例
    duck.quack()

duck = Duck()
bird = Bird()
doge = Doge()
for x in [duck, bird, doge]:
    in_the_forest(x)

# 我们并不关心对象是什么类型，到底是不是鸭子，只关心行为。
# 有这个行为, 就正确执行, 没有就报错, 不检查参数类型(java等其他类型是要检查的)
