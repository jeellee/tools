# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        for i,num in enumerate(nums):
            if num not in check:
                check[target-num]=i
            else:
                return [min(i,check[num]),max(i,check[num])]

# s = Solution()
# print s.twoSum(nums, target)


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

nums = [2, 3, 4, 6, 7, 15]
target = 9
s6 = Solution6()
print s6.twoSum(nums, target)



class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args)
        return cls._instance

class MyClass(Singleton):
    a = 1

# mm1 = MyClass()
# print id(mm1)
# mm2= MyClass()
# print id(mm2)



def singleton(cls):
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class MyClass2(Singleton):
    a = 1

mm3 = MyClass()
print id(mm3)
mm4 = MyClass()
print id(mm4)

