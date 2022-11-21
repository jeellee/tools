# coding = utf-8
"""
343. Integer break

将一个数字拆分成多个数字之和， 这些数字相乘 乘积最大
4
1+? 2+? 3+?

n
1+ (n-1)  2+(n-2)... n-1 + 1
"""


class Solution:
    memo = {}

    def break_integer(self, n):
        if n == 1:
            return 1
        if n == 2:  # 1+1
            return 1
        if self.memo[n] != -1:
            return self.memo[n]

        max_res = -1
        for i in range(2, n):
            max_res = max(max_res, i*(n-i), i * self.integerBreak(n-i))
        self.memo[n] = max_res

    def integerBreak(self, n: int) -> int:
        self.memo = [-1] * (n+1)
        return self.break_integer(n)

    def integerBreak2(self, n: int) -> int:
        """动态规划"""
        self.memo = [-1] * (n+1)   # n至少分解成两个数，所以分解后是n+1个数
        for i in range(1, n):   # n至少分解两个数， 那么最大的只能分解到n-1
            # 分解所有小于n的，将i分解为j+(i-j), 备选项
            for j in range(1, i):
                self.memo[i] = max(self.memo[i], i*(i-j), i*self.memo[i-j])  # 最大乘积
        return self.memo[n]


if __name__ == "__main__":
    s = Solution()
    # ret = s.longestPalindrome2("aba")
    ret = s.integerBreak2(4)
    print(ret)
