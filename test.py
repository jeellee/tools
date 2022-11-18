
# 1
class A():
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self is other


class B():
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return str(self) == str(other)

def test():
    a = A("abc")
    b = B("abc")

    print(a == b)   # 调用A的eq方法， b为other参数
    print(b == a)   # 调用B的eq方法， a为other参数


# 2
def func1():
    yield 1
    yield 2


def test1():
    for i in func1():
        print(i)


def test2():
    y = func1()
    # for i in iter(y):
    for i in y:
        print(i)


# 3
class C():
    _a = 2
    __b = 3


def test3():
    c = C()
    print(c._a)
    print(c._C__b)
    print(dir(c))


# 4
def test4():
    # https://blog.csdn.net/Arthur_Holmes/article/details/103435727
    # Ceiling是向上取整
    # floor是向下取整
    # Round是四舍五入的
    import math
    print(math.floor(3.4))
    print(math.floor(3.5))
    print(math.floor(-3.4))
    #
    print(math.ceil(45.17))
    print(math.ceil(-45.17))
    print(math.ceil(3.4))
    #
    print(round(3.5))


# 5
# python的作用域一共有四层：局部作用域 L (Local)-->>闭包函数外的函数中 E ( Enclosing ) -->>全局作用域 G ( Global ) -->> 内建作用域 B (Built-in)。记成LEGB
# https://www.ycpai.cn/python/bw6WhMbw.html
a = 1
list1 = [1]
def add():
    list1.append(2)
    a = 2

def add2():
    global a       # 不可变的，不用global修饰时，相当于重新申请了一个变量
    global list1   # 可变的， 不需要global修饰，也可以修改
    a = 2
    list1.append(2)

# add()
add2()
print(a, list1)


# 6 https://www.cnblogs.com/zpzp/p/15481849.html
# __del__函数 是删除对象 与 del不是一个东西
# del删除的是变量，而不是数据
# dog1变量删除（对象有引用，对象未删除，不会调用__del__），
# 打印
# 删除dog2变量，此时引用次数为0， 会调用__del__删除数据， 打印over
# 最后的打印
#
class Dog():
    def __del__(self):
        print("over")

def test6():
    dog1 = Dog()
    dog2 = dog1

    del dog1
    print("call del")

    del dog2
    print("last line - flag")


# 7-utf-8

def test7():
    # unicode（中文） ---encode("utf-8") ---utf-8（字节）  ----decode("utf-8") ----unicode（中文）
    a = "你好啊"
    print(type(a))

    print(type(a.encode("utf-8")))
    print(a.encode("utf-8").decode("utf-8"))
    # decode后变成unicode 打印出后 就是中文
    # encode后变成utf-8 打印出是子节，传输的时候就使用字节


# 8
def test8():
    """
    a = ["hello"] * 3
    print(a)
    b = [["hello"]] * 3
    print(b)
    """
    #
    item = ["hello"]
    items = [item] * 3   # 这里实际上是引用的item3次，修改item后，引用的都会修改
    print(items)
    items[0][0] = "world"   # item是可变对象，修改后，所有引用的地方都修改了
    print(items)


def test9():
    data_list = [1, 2, 3, 4, 5]
    for i in data_list:
        data_list.remove(i)
    print(data_list)   # 打印 2 4
    #  每次循环 i都会往前，第一次删除1 列表剩余[2, 3, 4, 5]
    #  第二次i往前一个 删除3， 最后一次往前删除5


def test10():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    print(set1 and set2)   # 与1 and 2道理一样，取后面那个
    print(1 and 2)

    print(set1 or set2)    # 取前面的

    print(set1 & set2)   # 取交集
    print(set1 | set2)   # 取并集

    print(set1 - set2)   # 取差集
    # print(set1 + set2)   # 没有加号方法
    print(set1 ^ set2)   # 取与set2不同的






if __name__ == "__main__":
    # test()
    # test1()
    # test2()
    # test3()
    # test4()
    # test7()
    # test8()
    # test9()
    test10()


