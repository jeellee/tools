#!coding=utf-8

"""
分苹果的问题

作者：将夜酱
链接：https://www.nowcoder.com/discuss/925356?type=all&order=recall&pos=&page=1&ncTraceId=&channel=-1&source_id=search_all_nctrack&gio_id=ED798F7AAAB485923FF8FA5E05B45B53-1654091206088
来源：牛客网

问题是：
现在有两个人A和B想要分苹果，每个苹果都有自己的重量，两人对于分得的苹果都有自己的要求：
A的要求是：希望尽可能分到更重的苹果
B的要求是：希望自己分得的各个苹果的重量的二进制数的忽略进位的和 等于 另一个人（A）分 得的各个苹果的重量的二进制数的忽略进位的和。

我的表述可能不是很清楚，这里举两个例子：

例子1：有3个苹果，重量分别为12、5、9。那么按照题目的要求，最好的分法是：A获得重量为12、5的两个苹果，B获得重量为9的苹果。
此时刚好满足B的要求——A所分得的两个苹果的重量12和5，12的二进制数为1100，5的二进制数为0101，这两个二进制数忽略进位的和等于1001，转化为十进制数即为9，刚好是B所分得的苹果的重量。

例子2：有3个苹果，重量分别为3、5、6。那么按照题目的要求，最好的分法是：A获得重量为5、6的两个苹果，B获得重量为3的苹果。
此时刚好满足B的要求——A所分得的两个苹果的重量5和6，5的二进制数为0101， 6的二进制数为0110，这两个二进制数忽略进位的和等于0011，转化为十进制数即为3，刚好是B所分得的苹果的重量。

其实就是异或，但原题就是如我上方差不多的表述，希望各位有看明白。

现在要求输入两行数据
第一行数据为m，即现在有m个苹果来分给这两人
第二行数据为这m个苹果，每个苹果的重量
结果是输出A能分到的苹果的最大重量，如果不能满足B的要求，则输出-1

3
3 5 6

1-不进位 是指每个数都不进位
2-排序找到最大数 计算最大数的二进制表示
3-B分的是A 分的苹果的 二进制之和（不进位）
A分5，6 那么B分3

3 011
5 101
6 110

使用异或运算符^

12 9 5
"""

"""
华为（题目已变化）

作者：牛客119451535号
链接：https://www.nowcoder.com/discuss/955981
来源：牛客网

题目描述：
A，B两个人把苹果分为两堆，A希望按照它的计算规则等分苹果，他的计算规则是按照二进制加法计算，并且不计算进位，12+5=9（1100+0101=9），
B的计算规则是十进制加法，包括正常进位，B希望在满足A的情况下获取苹果重量最多，输入苹果的数量和每个苹果重量，输出满足A的情况下获取的苹果总重量，
如果无法满足A的要求，输出-1。

输入描述：
输入第一行是苹果数量：3
输入第二行是每个苹果重量：3 5 6

3  5   6异或是0, 此时分给A 3即满足A的要求  那么B就是11=5+6

输出描述：
输出第一行是B获取的苹果总重量：11

示例1：
输入：
3
3  5  6
输出：
11

示例2：
输入：
8
7258  6579   2602  6716  3050   3564  5396  1773
输出：
35165 
"""


def calc(l):
    ret = l[0]
    for i in range(1, len(l)):
        ret = ret ^ l[i]
    return ret


def func():
    while True:
        n = int(input())
        l = list(map(int, input().strip().split()))
        total = sum(l)

        l.sort()

        b_target = calc(l)
        if b_target == 0:
            print(total - l[0])
        else:
            print(-1)


"""
有一种兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子。
例子：假设一只兔子第3个月出生，那么它第5个月开始会每个月生一只兔子。
一月的时候有一只兔子，假如兔子都不死，问第n个月的兔子总数为多少？

1   0
2   0
3   1
4   1
5   1+1
6   1+1+1
7   1+1+1+1+1
8   f(7) + f(7-2)   # 前1个月的兔子 + 新出生的兔子（也就是2个月前的兔子数量）1+1+1+1+1 + 1+1+1
数据范围：输入满足 
"""


def tuzi(n):
    if n < 3:
        return 0
    if n == 3 or n == 4:
        return 1
    return tuzi(n-1) + tuzi(n-2)


def func1():
    n = int(input().strip())
    if n < 3:
        print(0)
        return
    # 第n个月的兔子 = 第n-2个月的兔子  + 第n个月出生的兔子？？
    # m
    print(tuzi(n))


"""
链接：https://www.nowcoder.com/questionTerminal/3959837097c7413a961a135d7104c314
来源：牛客网
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成
另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家 Levenshtein 提出的，故又叫 Levenshtein Distance 。
例如：

字符串A: abcdefg
字符串B: abcdef

通过增加或是删掉字符 ”g” 的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。

要求：
给定任意两个字符串，写出一个算法计算它们的编辑距离。
数据范围：给定的字符串长度满足 1 \le len(str) \le 1000 \1≤len(str)≤1000 
"""


def func2():
    str1, str2 = input().strip(), input().strip()
    edit = [[j+i for j in range(len(str2)+1)] for i in range(len(str1)+1)]   #
    # for i in edit:
    #     print(i)

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            edit[i][j] = 0

    # for i in edit:
    #     print(i)

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                d = 0
            else:
                d = 1     # 不相等 编辑距离+1
            edit[i][j] = min(edit[i-1][j]+1, edit[i][j-1]+1, edit[i-1][j-1]+d)
    print(edit[len(str1)][len(str2)])


"""
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足 
https://www.nowcoder.com/questionTerminal/184edec193864f0985ad2684fbc86841
"""


def func3():
    while True:
        try:
            s = input()
            if len(s) <= 8:
                print('NG')
            else:
                l = [0, 0, 0, 0]
                for i in s:
                    if 'a' <= i <= 'z':
                        l[0] = 1
                    elif 'A' <= i <= 'Z':
                        l[1] = 1
                    elif i.isdigit():
                        l[2] = 1
                    else:
                        l[3] = 1
                if sum(l) < 3:
                    print('NG')
                else:
                    for i in range(len(s)-2):   # 判断不能有子窜重复
                        x = s[i:i+3]
                        if x in s[i+3:]:
                            print('NG')
                            break
                    else:
                        print('OK')
        except:
            break


"""
给一个01矩阵，1代表是陆地，0代表海洋， 如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
岛屿: 相邻陆地可以组成一个岛屿（相邻:上下左右） 判断岛屿个数。
例如：
输入
[
[1,1,0,0,0],
[0,1,0,1,1],
[0,0,0,1,1],
[0,0,0,0,0],
[0,0,1,1,1]
]
对应的输出为3
(注：存储的01数据其实是字符'0','1')
"""


def func4(grid):
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1]
    ]
    if not grid:
        return 0

    def dfs(i, j):
        grid[i][j] = '0'
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                dfs(x, y)

    m, n = len(grid), len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':    # 遍历（入口）找到1时，进行深度搜索
                res += 1
                dfs(i, j)
    return res


"""
最长有效括号(困难)
给定一个只包含 ‘(’ 和 ‘)’ 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: “(()”
输出: 2
解释: 最长有效括号子串为 “()”
示例 2:

输入: “)()())”
输出: 4
解释: 最长有效括号子串为 “()()”

注意：最长有效 是指的  有效字符串中括号都是成对出现的
如  
((()())) 有效
)(()())( 无效

暴力解法：
括号是成对出现的， 从后往前遍历， 每次移动两步， 依次判断是否是 有效（可以放入栈中，进行弹出，全部能够出栈，就是有效的）的

"""


def is_valid(sub_s):
    stack = []
    for i in sub_s:
        if i == "(":
            stack.append("(")
        elif stack:
            stack.pop()
        else:
            return False    # 右括号弹出时，一定有一个左括号可以弹出，否则就不是有效的
    return not stack


def func5():
    s = input().strip()
    num = 0
    for i in range(0, len(s)+1):
        for j in range(2, len(s)+1):
            sub_s = s[i: j]
            if is_valid(sub_s):
                num = max(num, len(sub_s))
    print(num)


# 栈解法
def func6():
    s = input().strip()
    l, cur_l = 0, 0
    stack = [-1]
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                cur_l = i - stack[-1]
                l = max(cur_l, l)
    print(l)


"""
【数字图色】疫情过后，希望小学终于又重新开学了，三年二班开学第一天的任务是将后面的黑板报重新制作。黑板上已经写了N个正整数，
同学们需要给这每个数分别上一种颜色。为了让黑板报既美观又有学习意义，老师要求同种颜色的所有数都可以被这种颜色中最小的那个数整除。
现在请你帮帮小朋友们，算算至少需要多少种颜色才能给这N个数进行上色。
输入描述:
第一行有一个正整数N，其中1<=N<=100。
第二行有个N个int型整数(保证输入数据在[1,100]范围内)，表示黑板上各个正整数的值。
输出描述:
输出只有一个整数，为最少需要的颜色种数。
示例1:
输入
3
2 4 6
输出
1
"""

def func7():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    nums.sort()
    used = []
    ret = []
    for i in range(n):
        if i in used:
            continue
        m = nums[i]
        l = [i]
        used.append(i)
        for j in range(n):
            if j not in used and nums[j] % m == 0:
                l.append(j)
                used.append(j)
        ret.append(l)
    print(ret)



"""
双十一众多商品进行打折销售
  小明想购买自己心仪的一些物品
  但由于购买资金限制
  所以他决定从众多心仪商品中购买三件
  而且想尽可能得花完资金
  现在请你设计一个程序 计算小明尽可能花费的最大资金数

  输入描述：
    输入第一行为一维整型数组m
    数组长度小于100
    数组元素记录单个商品的价格
    单个商品加个小于1000

    输入第二行为购买资金的额度r
    r<100000

  输出描述：
     输出为满足上述条件的最大花费额度

   注意：如果不存在满足上述条件的商品请返回-1

  示例：
     输入
      23,26,36,27
      78
     输出
      76
     说明：
      金额23、26、27得到76而且最接近且小于输入金额78

   示例：
       输入
       23,30,40
       26
       输出
        -1
       说明
       因为输入的商品无法满足3件之和小于26
       故返回-1

   输入格式正确无需考虑输入错误情况
"""

def func8():
    price_list = list(map(int, input().strip().split(",")))
    money = int(input().strip())
    from itertools import combinations
    com_prices = combinations(price_list, 3)
    max_money = 0
    for com_price in com_prices:
        if sum(com_price) > money:
            continue
        max_money = max(sum(com_price), max_money)
    if not max_money:
        print(-1)
    else:
        print(max_money)


"""
字符统计
输入：
一行字符串， 有大小写
输出：
按字符出现次数降序输出， 同字母大小写个数相同，先输出小写，再输出大写

xxyyyzYYY
输出：
y:3;Y:3;x:2;z:1
"""

def func9():
    s_l = list(input().strip())
    s_dict = {}
    for s in s_l:
        if s in s_dict:
            s_dict[s] += 1
        else:
            s_dict[s] = 1

    map_s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    from functools import cmp_to_key

    def my_cmp(s1, s2):
        ss1, num1 = s1
        ss2, num2 = s2
        if num1 > num2:
            return 1
        elif num1 == num2:
            index1 = map_s.index(ss1)
            index2 = map_s.index(ss2)
            if index1 < index2:
                return 1
            else:
                return -1
        else:
            return -1

    print(sorted(s_dict.items(), key=cmp_to_key(my_cmp), reverse=True))


if __name__ == "__main__":
    func9()
