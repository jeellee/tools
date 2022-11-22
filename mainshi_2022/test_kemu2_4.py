from test_kemu2_3 import *

a = A()
b = B()     # B在__all__中未定义，import * 的时候不会导入
print(a)
print(b)
