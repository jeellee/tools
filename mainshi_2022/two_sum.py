# -*- coding: utf-8 -*-
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


class Solution2(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
        return buff_dict

# s2 = Solution2()
# print s2.twoSum(nums, target)


# class Solution3(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for num in nums:
#             if (target - num) in nums:
#                 return [nums.index(num), nums.index(target - num)]


class Solution4(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = list(nums)
        for num in nums:
            num_index = temp.index(num)
            temp[num_index] = None

            if (target - num) in temp:
                return [num_index, temp.index(target - num)]
                # [3, 3]   6
                # [2, 3, 4]

# s3 = Solution3()
# print s3.twoSum(nums, target)

"""
查找和为9的
因为是有序的, 从数组连边开始查找
nums = [2, 7, 3, 6, 11, 15]
        i                j
nums[i] + nums[j] > target, j--
nums[i] + nums[j] < target, i++
"""
class Solution6(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return [i+1, j+1]

# nums = [2, 3, 4, 6, 7, 15]
# target = 9
# s6 = Solution6()
# print s6.twoSum(nums, target)



