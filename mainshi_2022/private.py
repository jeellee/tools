# encoding: utf-8

import pdb


class MyClass(object):
    def __init__(self):
        self.__superprivate = 'Hello'
        self._semiprivate = 'world'



mc = MyClass()

#print mc.__superprivate   # 理论上类外部不可访问, 通过_MyClass__superprivate还是可以访问的(约定最好不要访问)
print mc._semiprivate   # 私有变量, 约定不要在外部访问
# print mc.__dict__  # {'_MyClass__superprivate': 'Hello', '_semiprivate': 'world'}


