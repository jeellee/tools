# coding: utf-8


class Person(object):
    def __init__(self):
        self.__age = 20

    def get_fullname(self, first_name, second_name):
        return first_name + ' ' + second_name

    def get_age(self):
        return self.__age

    @staticmethod
    def get_class_name():
        return Person.__name__
