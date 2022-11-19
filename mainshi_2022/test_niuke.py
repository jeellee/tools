# -*- coding: utf-8 -*-

# while True:
#     try:
#         a = raw_input().strip()
#         if not a.isdigit():
#             continue
#         a = set(list(a))
#         a = sorted(a, reverse=True)
#         a = "".join(a)
#         print a
#     except:
#         break


# while True:
#     try:
#         a = raw_input()
#         if not a.isdigit():
#             break
#         a = set(list(a))
#         a = sorted(a, reverse=True)
#         a = int("".join(a))
#         print a
#     except:
#         break

# a = input()
# a = set(list(str(a)))
# a = sorted(a, reverse=True)
# a = int("".join(a))
# print a
#
#
# while True:
#     try:
#         a = raw_input().strip()
#         print a[::-1]
#     except:
#         break


# print list(312312312)
# while True:
#     try:
#         num = int(input())
#         if isinstance(num, int):
#             list1 = sorted(set(str(num)), reverse=True)
#             output = int("".join(map(str, list1)))
#             print(output)
#     except:
#         break


# while True:
#     try:
#         a = input()
#         b = input()
#         print(str(int(a) + int(b)))
#     except:
#         break

# while True:
#     try:
#         a = input()
#         a = set(list(str(int(a))))
#         a = int("".join(sorted(a, reverse=True)))
#         print a
#     except:
#         break

# 1 题目
# （题来源牛客网华为2019秋招笔试题）
#
# 1.1 问题描述
# 给定一个正整数，给出消除重复数字以后最大的整数。
#
# 1.2 输入示例
# 423234
#
# 1.3 输出示例
# 432
#
# 2 问题分析
# 这道题想了很久，没有想出来，采用牛客上提供的方法。
#
# 此题相当于一个字符串查重调整问题，需要两重循环，（相当于冒泡排序需要两层循环）。
#
# 用两指针i,j开始指向字符串的首地址，然后开始遍历，j作为查重指针（查找[0,i]之间的字符串）。
#
# 如果出现了重复数字，则str[i] == str[j]，此时要考虑删掉str[i]还是str[j]的问题，比如有这样一个子串4232，i指向第4个，j指向第2个，
# 如果删str[i]结果为423，如果删str[j]则结果为432，显然要删掉str[j]，寻找一个参考标准，j后面的数字是3，3比2大，如果删除2，
# 则会导致3向前移，则最终结果就会变大，所以判断标准str[j+1]>str[j]时，则删掉str[j]，否则删掉str[i]。


def fun(input_str):
    find_list = []
    for j in range(len(input_str)):
        num_str = input_str[j:]
        temp = ""
        for i in range(len(num_str)):
            v = num_str[i]
            if not temp:
                temp = v
            else:
                temp_list = list(temp)
                if v in temp_list:
                    repeat_index = temp_list.index(v)
                    temp_list.append(v)
                    temp_list.pop(repeat_index)
                    new_temp = int("".join(temp_list))
                    if int(temp) < new_temp:
                        temp = str(new_temp)
                else:
                    temp += v

        find_list.append(int(temp))
    print find_list
    return max(find_list)


while True:
    try:
        a = raw_input()
        if not a.isdigit():
            break
        print fun(a)
    except:
        break

# 23452  -> 3452
# 41432  -> 4132
# 423234 -> 423
# 3236321  -> 6321



