# coding = utf-8
"""
5. 最长回文子串 leetcode 5

aba
s(i,j) 是回文子串 那么s(i+1, j-1)肯定是回文子串
i/j  0    1   2
0    a    ab  aba
1         b   ba
2             a
s(i,j) = s(i+1, j-1) and s(i==j)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """自己写的"""
        n = len(s)
        palindrome_list = []
        max_len = 0
        max_str = ''
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    palindrome_list.append((i, j))
                if i == j-1 and s[i] == s[j]:
                    palindrome_list.append((i, j))
                if (i+1, j-1) in palindrome_list and s[i] == s[j]:
                    palindrome_list.append((i, j))
                if j-i+1 > max_len:
                    max_str = s[i:j+1]
                    max_len = j-i+1

        return max_str

    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        dp = [[False]*n for _ in range(n)]
        start = 0
        max_len = 1
        for j in range(1, n):
            for i in range(j):
                if j - i < 3:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        current_len = j-i+1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        current_len = j-i+1
                if dp[i][j] and current_len > max_len:
                    max_len = current_len
                    start = i
        return s[start:start+max_len]


if __name__ == "__main__":
    s = Solution()
    # ret = s.longestPalindrome2("aba")
    ret = s.longestPalindrome("babad")
    print(ret)
