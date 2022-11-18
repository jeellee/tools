# encoding: utf-8

"""
为了理解yield有什么用,首先得理解generators(生成器),而理解generators前还要理解iterables(迭代器)


"""

# 当你创建了一个列表, 你可以一个一个的读取它的每一项,这叫做iteration
mylist = [x*x for x in range(3)]
# print mylist          # [0, 1, 4]

# 生成器也是迭代器的一种,但是你只能迭代它们一次
# mygenerator = (x*x for x in range(3))
# print mygenerator      # <generator object <genexpr> at 0x10ab4de10>

# for i in mygenerator:
#     print i

# mygenerator.next()    # 运行完for,  再运行就会报错, 已经没有数据了
# 生成器和迭代器的区别就是用()代替[], 还有你不能用for i in mygenerator第二次调用生成器:首先计算0,然后会在内存里丢掉0去计算1,直到计算完4.

# yield
def createGenerator():
    for i in range(3):
        yield i*i
        print "...", i

mygenerator = createGenerator()

# print mygenerator    # <generator object createGenerator at 0x10b7e9e10>

print mygenerator.next()
print mygenerator.next()
# print mygenerator.next()
# print mygenerator.next()
"""

class Bank():    # 让我们建个银行,生产许多ATM
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

hsbc = Bank()
atm = hsbc.create_atm()
print atm        # <generator object create_atm at 0x106b65eb0>

print atm.next()
print atm.next()
print atm.next()
print atm.next()
print atm.next()
print atm.next()

hsbc.crisis = True    # 经济危机, 就不能再创建atm了
print atm.next()

hsbc.crisis = False    # 经济危机过了, 还是不能创建atm, 需要重新创建bank
print atm.next()

atm = hsbc.create_atm()  # 需要重新创建bank
print atm.next()
"""
