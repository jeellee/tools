# coding: utf-8

"""
Python模块之信号（signal）
"""
import sys
import time
import signal
# print signal.SIGABRT
# print signal.SIG_DFL

# signal包的核心是使用signal.signal()函数来预设(register)信号处理函数
# singnal.signal(signalnum, handler)  signalnum为某个信号，handler为该信号的处理函数


# 进程可以无视信号，可以采取默认操作，还可以自定义操作。
# 当handler为signal.SIG_IGN时，信号被无视(ignore)。
# 当handler为singal.SIG_DFL，进程采取默认操作(default)。
# 当handler为一个函数名时，进程采取函数中定义的操作


# 我们这里用了一个无限循环以便让进程持续运行。
# 在signal.alarm()执行5秒之后，进程将向自己发出SIGALRM信号，随后，信号处理函数myHandler开始执行。
# Define signal handler function
"""
def myHandler(signum, frame):
    print("Now, it's the time")
    exit()

# register signal.SIGALRM's handler
signal.signal(signal.SIGALRM, myHandler)     #
signal.alarm(5)
while True:
    time.sleep(0.5)
    print('not yet')

# signal包的核心是设置信号处理函数。除了signal.alarm()向自身发送信号之外
# ，并没有其他发送信号的功能。但在os包中，有类似于linux的kill命令的函数，分别为
# os.kill(pid, sid)
# os.killpg(pgid, sid)
# sid为信号所对应的整数或者singal.SIG*

"""

"""
协程
"""
# 生产者
def produce(l):
    i = 0
    while 1:
        if i < 5:
            l.append(i)
            print 'produce: 111', l
            yield i
            i = i + 1
            time.sleep(1)
            print 'produce: 222'
        else:
            return


# 消费者
def consume(l):
    print 'consume: start'
    p = produce(l)    # 并不立即执行, 暂停在yield处
    while 1:
        try:
            p.next()        # next取出一个后, produce继续执行yield后面的
            print 'consume: 222', l
            while len(l) > 0:
                print l.pop()
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