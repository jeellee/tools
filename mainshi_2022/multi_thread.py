# coding: utf-8
import sys

"""
多进程和多线程
1. 二者的最大区别就是, 是否共享资源, 后者是共享资源的,而前者是独立的.

2. 相对于进程的轻型特征,多线程环境有个最大的问题就是 如何保证资源竞争,死锁, 数据修改等, 便有了 线程安全 (thread safety)的提出

3.  线程安全是在多线程的环境下, 线程安全能够保证多个线程同时执行时程序依旧运行正确,
    而且要保证对于共享的数据,可以由多个线程存取,但是同一时刻只能有一个线程进行存取

4. 加锁, 加锁可以保证存取操作的唯一性, 从而保证同一时刻只有一个线程对共享数据存取

5. 通常加锁也有2种不同的粒度的锁:
   fine-grained(所谓的细粒度), 那么程序员需要自行地加,解锁来保证线程安全
   coarse-grained(所谓的粗粒度), 那么语言层面本身维护着一个全局的锁机制,用来保证线程安全

   前一种方式比较典型的是 java, Jython 等, 后一种方式比较典型的是 CPython (即Python),  如GIL


logging 是线程安全的么？
是的，handler 内部使用了 threading.RLock() 来保证同一时间只有一个线程能够输出。
但是，在使用 logging.FileHandler 时，多进程同时写一个日志文件是不支持的。
"""

"""
6. twisted和tornado
twisted和tornado是基于事件的异步网络框架，异步体现在线程和tornado协程，
事件其实就是对IO多路复用机制的包装，在windows上包装的是select，在linux2.5+上包装的是epoll，在大多数BSD上包装的是kqueue。


"""

"""
7. TCP的粘包
UDP丢包是因为数据包在传送过程中丢失了 而TCP是基于流式的发送 并且存在丢包重发机制 TCP是可靠连接而UDP是不可靠的这个我就不多说了
关于TCP的粘包 正是由于TCP是流式传送的 也就是连接建立后可以一直不停的发送 并没有明确的边界定义
而你用UDP发送的时候 是可以按照一个一个数据包去发送的 一个数据包就是一个明确的边界
而TCP并没有数据包的概念 是完全流式的 他会开辟一个缓冲区 发送端往其中写入数据 每过一段时间就发送出去 然后接收端接收到这些数据
但是并不是说我发送了一次数据就肯定发送出去了 数据会在缓冲区中
有可能后续发送的数据和之前发送的数据同时存在缓冲区中随后一起发送 这就是粘包的一种形式
接收端也有产生粘包的情况 如果应用程序没有及时处理缓冲区中的数据 那么后续到达的数据会继续存放到缓冲区中 也就是2次接收的数据同时存在缓冲区中
下次取缓冲区的时候就会取出2次粘包后的数据 这是粘包的另外一种形式 还有其他许多形式 比如填充缓冲区到一半缓冲区满了直接发送了 但是其实那个包还没填充完全 这个就是不完整的粘包了 剩余数据会在下次发送的时候补上
关于解决方法 如果你是连续的整个数据流 比如发送文件 那么完全不考虑粘包也无所谓 因为可以建立连接后发送 发送完毕后断开连接 整个数据流就是整个一个文件 无论数据从那里切开都无所谓 整个拼接后依旧是整个一个文件的数据
如果你发送的数据是多次通信 比如把一个目录下所有的文件名都发送过去 那么就不能当作一个整体发送了 必须对他们划分边界 有一个很简单的处理方法 就是采用"数据长度+实际数据"的格式来发送数据 这个"数据长度"的格式是固定宽度的 比如4字节
可以表示0~4GB的宽度了 足够用了 这个宽度说明了后续实际数据的宽度 这样你就可以把粘包后的数据按照正确的宽度取出来了
每次都是取出4字节 随后按照正确的宽度取出后续部分的就OK了
如果你的所有数据都是固定宽度的 比如不停的发送温度数据 每个都是1字节 那么宽度已知了 每次你都取出一个1字节就OK了 所以就不用发送宽度数据了
当然你也可以按照建立连接断开连接来划分边界 每次发送数据都打开关闭一次连接 不过对于频繁的小数据量是不可取的做法 因为开销太大 建立连接和关闭连接也是需要耗费网络流量的
总而言之 粘包的情况是无法绝对避免的 因为网络环境是很复杂的 依赖发送和接收缓冲区的控制是不能保证100%的 只要在发送的数据中说明数据的宽度随后在接收部分按照这个宽度拆开就OK了 宽度全都是统一的已知宽度的情况下拆开更加容易 连在发送端填入宽度数据都可以省去了
"""

"""
Bottleneck  瓶颈
"""

"""
线程
启动一个线程实际上就是把一个函数传入, 并创建Thread实例, 然后调用start开始执行
"""
import time
import _thread        # 低级模块
import threading     # 高级模块, 对thread的封装, 大多数情况使用threading即可


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        print('thread %s >>> %s...' % (threading.current_thread().name, n))
        n += 1
        time.sleep(1)
    print('thread %s is ended...' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
th = threading.Thread(target=loop, name='LoopThread')
th.start()
th.join()
print('thread %s is ended...' % threading.current_thread().name)




"""
协程
"""
# 生产者
def produce(l):
    i = 0
    while 1:
        if i < 5:
            l.append(i)
            print('produce: 111', l)
            yield i
            i = i + 1
            time.sleep(1)
            print('produce: 222')
        else:
            return


# 消费者
def consume(l):
    print('consume: start')
    p = produce(l)    # 并不立即执行, 暂停在yield处
    while 1:
        try:
            next(p)        # next取出一个后, produce继续执行yield后面的
            print('consume: 222', l)
            while len(l) > 0:
                print(l.pop())
        except StopIteration:
            sys.exit(0)

# produce每生产一个, consume就消费一个,
l = []
consume(l)

"""
consume: 111
produce: 111 [0]
consume: 222 [0]
0
produce: 222
produce: 111 [1]
consume: 222 [1]
1
produce: 222
produce: 111 [2]
consume: 222 [2]
2
produce: 222
produce: 111 [3]
consume: 222 [3]
3
produce: 222
produce: 111 [4]
consume: 222 [4]
4
produce: 222
"""