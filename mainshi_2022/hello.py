# encoding: utf-8


class Hello():
    def hello(self, name):
        print 'hello, %s' % name

h = Hello()
h.hello('jeellee')

print type(Hello)
print type(h)

print "-----------------------------"

# type 创建类


def fn(self, name):
    print 'hello, %s' % name

Hello2 = type('Hello', (object,), dict(hello=fn))

h = Hello2()
h.hello('jeellee')
print type(Hello2)
print type(h)


# metalclass 控制类的创建行为(允许创建类和修改类)
