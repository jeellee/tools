# coding: utf-8

import unittest
from mock import Mock
from mock import create_autospec
from mock import patch
from app.person import Person

"""
class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person_instance = Person()

    # def test_get_age(self):
    #     self.assertEqual(20, self.person_instance.get_age())
    #
    #     self.person_instance.get_age = Mock(return_value=10)
    #     self.assertEqual(10, self.person_instance.get_age())

    def test_get_fullname(self):
        # self.person_instance.get_fullname = mock.Mock(return_value='jeel lee')
        # self.assertEqual('jeel lee', self.person_instance.get_fullname())  # mock的方法没有参数，调用时不用传参数

        self.person_instance.get_fullname = create_autospec(
            self.person_instance.get_fullname, return_value='jeel lee')

        self.assertEqual('jeel lee', self.person_instance.get_fullname('jeel', 'lee'))

    def test_get_age(self):
        # side_effect 依次返回指定值
        self.person_instance.get_age = Mock(side_effect=[10, 20, 30])
        self.assertEqual(self.person_instance.get_age(), 10)
        self.assertEqual(self.person_instance.get_age(), 20)
        self.assertEqual(self.person_instance.get_age(), 30)

    def test_should_raise_exception(self):
        self.person_instance.get_age = Mock(side_effect=TypeError('integer error'))
        # 只要调就会抛出异常
        self.assertRaises(TypeError, self.person_instance.get_age)

"""


class PersonTest(unittest.TestCase):
    mock_get_class_name = Mock(return_value='Guy')

    # 在patch中给出定义好的Mock的对象，好处是定义好的对象可以复用
    @patch('app.person.Person.get_class_name', mock_get_class_name)
    def test_should_get_class_name(self):
        self.assertEqual(Person.get_class_name(), 'Guy')
