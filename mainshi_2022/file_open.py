# coding: utf-8

"""
read: 一次读取文件的全部内容, python把内容读取到内存, 用一个str对象表示
F.read([size]) size为读取的长度，以byte为单位

readline
F.readline([size]) 读一行，如果定义了size，有可能返回的只是一行的一部分

readlines
F.readlines([size]) 把文件每一行作为一个list的一个成员，并返回这个list。
其实它的内部是通过循环调用readline()来实现的。
如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分
"""
# input = open('data', 'r')    # 默认第二个参数是r, 表示读取 到输入流
# input = open('data', 'rb')   # rb, 读取二进制文件

# input = open('test11.py')
# c = input.read()
#
# print c

# input = open('test11.py')
# c = input.read(10)
#
# print c
# d = input.read(10)   # 继续读取
# print d


# input = open('test11.py')
# c = input.readline()
#
# print c

# input = open('test11.py')
# c = input.readlines()
#
# print c

# input.close()      # 记得要关闭文件


"""
写入文件
write 一次写入
writelines 写入多行, 性能要高

文件读取模式:
（1）r模式：
该模式打开的文件必须存在，如果不存在，将会出错；并且，该模式打开的文件，只能读，不能向文件中写入。（只读）
（2）r+模式：
该模式打开的文件必须存在，如果不存在，将会出错；并且，该模式打开的文件，可以向文件中写入。
（3）w模式：
该模式打开的文件如果已经存在，则先清空，否则新建一个文件，然后只能写入数据，不能读取。
（4）w+模式
该模式打开的文件如果已经存在，则先清空，否则新建一个文件，然后可以写入数据，也可以读取。
（5）a模式
该模式打开的文件如果已经存在，不会清空，否则新建一个文件，写入的内容追加到文件尾；不能读取数据。（以追加的方式写入）
（6）a+模式
该模式打开的文件如果已经存在，不会清空，否则新建一个文件，写入的内容追加到文件尾；也可以读取数据

总结:
r 读取文件(文件不存在时, 会报错, 不会新建文件)
w 写入文件(先清空, 再写入)
a 写入文件(不清空, 追加写入)
+ 表示同时可读也可写

"""
# output = open('test11.py', 'w')  写文本文件
# output = open('test11.py', 'wb')  写二进制文件
# output = open('test11.py', 'w+')  追加写文件

# file_object = open('test_file', 'w')    # 文件不存在时, 自动创建
# file_object.write('hello jeellee!')
# file_object.close()

# file_object = open('test_file', 'a')
# file_object.write('hello jeellee!')
# file_object.read()    # 会报错
# file_object.close()


file_object = open('test_file', 'a')
file_object.writelines(['aaaaaaaaaaaa\n', 'bbbbbbbbbbb'])
file_object.close()


with open('test_file', 'a') as f:
    for line in f:
        print line.strip()


with open('test_file', 'a') as f:
    content = f.read()     # 问价较小时， 一次读取


with open('test_file', 'a') as f:
    for line in f.readlines():     # 配置文件 这样读比较方便
        print line.strip()
