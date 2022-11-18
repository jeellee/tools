# coding: utf-8

"""
19.用Python匹配HTML tag的时候，<.*>和<.*?>有什么区别？
前者是贪婪匹配，会从头到尾匹配 <a>xyz</a>，而后者是非贪婪匹配，只匹配到第一个 >。


17.如何用Python来进行查询和替换一个文本字符串？
可以使用sub()方法来进行查询和替换，sub方法的格式为：sub(replacement, string[, count=0])
replacement是被替换成的文本
string是需要被替换的文本
count是一个可选参数，指最大被替换的数量

sub是正则表达式，他的功能更加强大；
而replace只是一个替换

18.Python里面search()和match()的区别？
match()函数只检测RE是不是在string的开始位置匹配，search()会扫描整个string查找匹配,
也就是说match()只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
"""

import re
# pattern = re.compile(r'\d')
# print pattern.sub('no', '12hh34hh')

# pattern.sub('no', '12hh34hh', count=0)  # count默认为0, 表示全部替换; 不为0 表示替换count个
# print pattern.sub('no', '12hh34hh', count=1)


# a = [1, 2]
# b = [3, 4]
#
# 1. 1+2=3  3+4=7
# 7-3=4 / 2 = 2
#
# 4(min) - 2(min)    2
#
# a = [1, 4]
# b = [3, 2]


src = "security/afafsff/?ip=123.4.56.78&id=45"

# 1. match只有在0位置匹配成功才返回
# print re.match(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", src)
# None

# 2. search()会扫描整个string查找匹配
# print re.search(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", src)
# <_sre.SRE_Match object at 0x10eb96030>

# 3.
# ‘ dog|cat’ 匹配的是‘ dog’ 和 ’cat’ ，而不是 ’g’ 和 ’c’ 。如果想限定它的有效范围，必需使用一个无捕获组 ‘(?: )’ 包起来。
# 比如要匹配 ‘ I have a dog’ 或 ’I have a cat’ ，需要写成 r’I have a (?:dog|cat)’ ，而不能写成 r’I have a dog|cat’


print re.findall(r'(\d{1,3}\.){3}\d{1,3}', "security123.4.56.78")
# ['56.']  将()当成了一个组, 匹配不正确
print re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', "security123.4.56.78")
# ['123.4.56.78']


# 4. \b (使用时, 必须前面加r)  匹配一个单词边界，也就是指单词和空格间的位置。
# 例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# print re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", src)


# 5. ?<![\.\d])之前的字符不是.或数字 才匹配
#    (?![\.\d])之后的字符不是.或数字 才匹配
print re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', "security23.123.4.56.78")
# ['23.123.4.56']   没有限定, 能匹配出结果

print re.findall(r'(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', "security23.123.4.56.78")
# ['123.4.56.78']  限定后面的字符不是.或数字 才匹配, 所以从123.开始匹配

re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', "security23.123.4.56.78")
# 前后都限定, 匹配不到了
