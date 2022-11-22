# -*- coding: utf-8 -*-

"""
从字符窜中, 找出最长的一个子窜, 子窜中没有字母重复
"""

aaa = "tjhrtvkwwojbqhjjfkboaccenrxihcsanbtgxdcttnujvfscrwqtyuynmxwvbqxorquowzhpmdzjlrlc"


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = [[] for _ in range(len(s))]
        for i, v in enumerate(s):
            for j, l in enumerate(list1):
                if j > i:
                    continue
                if 'None' in l:
                    continue
                if v not in l:
                    l.append(v)
                else:
                    l.append('None')
        max_len = 0
        max_str = ''
        for i in range(len(list1)):
            v = list1[i]
            v_len = len(v)
            if 'None' in v:
                v_len = len(v)-1
            if max_len < v_len:
                max_len = v_len
                max_str = ''.join(v)
        print(max_len, max_str)


# s = Solution()

# print s.lengthOfLongestSubstring('dvdf')
# print s.lengthOfLongestSubstring(aaa)


class Solution2:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}    # 以value做key, index做值, 存储已使用的, 并不断移动start的位置, 判断start与前面字符间的最大距离

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

# s = Solution2()
# s.lengthOfLongestSubstring('dvdf')

aaa = "tjhrtvkwwo"
class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        i = j = max_len = 0
        set_temp = set()
        while j < len(s):
            if s[j] not in set_temp:   # 当发现在里面的时候, 就从前到后找一遍, 逐个删除, 直到将在里面的那个数也删除掉, 然后继续执行
                set_temp.add(s[j])
                j += 1
                max_len = max(max_len, len(set_temp))
            else:
                set_temp.remove(s[i])
                i += 1
        return max_len

# s = Solution3()
# print s.lengthOfLongestSubstring('dvdfd')

aaa = "tjhrtvkwwojbqhjjfkboaccenrxihcsanbtgxdcttnujvfscrwqtyuynmxwvbqxorquowzhpmdzjlrlc"


# aaa = "tjhrtvkwwo"


class Solution5:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        i = j = max_len = 0
        max_str = set()
        while j < len(s):
            if s[j] in max_str:
                i += 1
                max_str.remove(s[j])
            else:
                max_str.add(s[j])
                j += 1
                max_len = max(max_len, len(max_str))

        return max_len

s = Solution5()
print(s.lengthOfLongestSubstring('dvdfd'))

"""
"""
class Solution4(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


# s = Solution4()
# print s.findMedianSortedArrays([1,2,2,3], [4,5])



"""
将数组中所有为0的元素移动到数组尾部
[1, 0, 3, 2, 0] --->  [1, 3, 2, 0, 0]
"""
# 简单粗暴的解法,
# 时间复杂度O(n), 空间复杂度O(n)
nums = [0, 1, 0, 3, 12]
class Solution6(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp_nums = []
        for i in range(len(nums)):
            if nums[i]:
                temp_nums.append(nums[i])

        for i in range(len(nums)-len(temp_nums)):
            temp_nums.append(0)
        return temp_nums


# s = Solution6()
# print s.moveZeroes(nums)

# 原地完成: 时间复杂度O(n), 空间复杂度: O(1)
# 0, 1, 0, 3, 12
# k
# 1, 1, 0, 3, 12
#    k

class Solution7(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0      # [0....k) 存放非0元素
        for i in range(len(nums)):
            if nums[i]:
                nums[k] = nums[i]
                k += 1

        print(nums)
        for i in range(k, len(nums)):
            nums[i] = 0

# s = Solution7()
# s.moveZeroes(nums)
# print nums


# 交换元素
# 考虑全部是非0元素
class Solution8(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0      # [0....k) 存放非0元素
        for i in range(len(nums)):
            if nums[i]:
                if i != k:     # 自身不交换
                    nums[k], nums[i] = nums[i], nums[k]
                k += 1

        # print nums
        # for i in range(k, len(nums)):
        #     nums[i] = 0

# s = Solution8()
# s.moveZeroes(nums)
# print nums



"""
75. Sort Colors
[1, 2, 1, 0, 2, 2]  --> [0, 1, 1, 2, 2, 2]
1. 最简单的, 直接调用sort函数
2. 计数统计, 统计1, 2, 3各有多少个
3. 三路快排

0        zero   two    n-1

0到zero之间都是0  zero到two之后都是1   two到n-1之前都是2
"""

class Solution9(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # nums.sort()

        #  时间复杂度O(n),空间复杂度O(1), 只有一次遍历
        zero = -1
        two = len(nums)
        i = 0
        while i < two:     # [0...zero] 都是0 [zero+1...two-1]都是1, [two...len(nums)]都是2
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1

nums = [1, 2, 1, 0, 2, 2]
s = Solution9()
s.sortColors(nums)
print(nums)


"""
215. Kth Largest Element in an Array
利用快排来找出第k大的元素的位置

[3,2,1,5,6,4] and k = 2, return 5.
一种方法, 直接从大到小排序, 找到第二个数即可
另一种方法, 取出最大值, 然后删除, 第k次找到的最大值就是第k大的数

利用快排, k小于基准点的索引, 就在左边查找, 大于就在右边查找
"""

class Solution10(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        mid = nums[l]

        for i in range(len(nums)):
            if l > r:
                return
            if nums[i] < mid:
                l += 1
            elif nums[i] > mid:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1



"""
209. Minimum Size Subarray Sum
For example, given the array [2,3,1,2,4,3] and s = 7,

相隔最短, 并且大于s的子数组

使用滑动窗口解决
"""
class Solution11(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = -1     # [l...r]是滑动的窗口
        sum = 0
        res = len(nums)+1   # 设置比最大值还大的
        while j < len(nums):
            if j+1 < nums and sum < s:
                j += 1
                sum += nums[j]
            else:
                sum -= nums[i]
                i += 1

            if sum >= s:
                res = min(res, j-i+1)
        if res == len(nums)+1:
            return 0
        return res




class Node():
  __slots__=['_item', '_next']    # 限定Node实例的属性
  def __init__(self,item):
    self._item=item
    self._next=None              # Node的指针部分默认指向None
  def getItem(self):
    return self._item
  def getNext(self):
    return self._next
  def setItem(self,newitem):
    self._item=newitem
  def setNext(self,newnext):
    self._next=newnext


class SingleLinkedList():
  def __init__(self):
    self._head=None  # 初始化链表为空表
    self._size=0

  def isEmpty(self):
      return self._head == None

  def add(self, item):
      temp = Node(item)
      temp.setNext(self._head)
      self._head = temp

  def append(self, item):
      temp = Node(item)
      if self.isEmpty():
          self._head = temp  # 若为空表，将添加的元素设为第一个元素
      else:
          current = self._head
          while current.getNext() != None:
              current = current.getNext()  # 遍历链表
          current.setNext(temp)  # 此时current为链表最后的元素

  def search(self, item):
      current = self._head
      founditem = False
      while current != None and not founditem:
          if current.getItem() == item:
              founditem = True
          else:
              current = current.getNext()
      return founditem


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# def create_linked_list(arr=None, n):


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            next = cur.__next__
            cur.next = pre

            pre = cur
            cur = next
        return pre



