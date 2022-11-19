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
