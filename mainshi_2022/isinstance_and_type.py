# 使用isinstance判断类型，不使用type
# 区别：isinstance 会判断是否是目标类型的实例， 还会判断是否是目标类型子类的实例
# 优先使用内置类型判断

callable(object)
from collections.abc import Container
isinstance(object, Container)

class Body:
    pass

class Teacher(Body):
    pass

a = Body()
b = Teacher()

print((111, type(b) == Body))   # False
print((222, isinstance(b, Body)))   # True
print((333, isinstance(a, Teacher)))   # False

