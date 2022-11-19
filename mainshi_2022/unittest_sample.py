# coding: utf-8

import unittest


class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        for i, num in enumerate(nums):
            if num not in check:
                check[target-num] = i
            else:
                return [min(i, check[num]), max(i, check[num])]

# nums = [1, 2, 3, 4, 5]
# target = 9
# s = Solution()
# print s.twoSum(nums, target)


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum(self):
        nums = [1, 2, 3, 4, 5]
        target = 9
        ret = self.solution.twoSum(nums, target)
        self.assertEqual(ret, [3, 4])

# 执行方式1：
# if __name__ == '__main__':
#     unittest.main()

# 执行方式2：
# python -m unittest two_sum
# python -m unittest two_sum.SolutionTest
# python -m unittest two_sum.SolutionTest.test_twoSum
