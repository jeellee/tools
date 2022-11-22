# encoding: utf-8

import pdb


class A(object):
    def go(self):              # 6
        print("go A go!")

    def stop(self):
        print("stop A stop!")

    def pause(self):
        raise Exception("Not Implememented")


class B(A):
    def go(self):               # 2
        super(B, self).go()     # 3
        print("go B go!")        # 7


class C(A):
    def go(self):               # 4
        super(C, self).go()     # 5
        print("go C go!")        # 6

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")


class D(B, C):
    def go(self):
        super(D, self).go()  # 1
        print("go D go!")     # 8

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")


class E(B, C):
    pass

# pdb.set_trace()
a = A()
b = B()
c = C()
d = D()
e = E()

# a.go()
# b.go()
d.go()
print(d.__class__.mro())
