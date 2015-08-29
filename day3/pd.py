# coding=utf-8
# 写2个函数分别统计一个字符串里面所有字母，数字的个数
def digitNum(str1):
    digitNum = 0
    for i in str1:
        if i >= '0' and i <= '9':
            digitNum += 1
    return digitNum


def alphaNum(str1):
    alphaNum = 0
    for i in str1:
        if i.isalpha():
            alphaNum += 1
    return alphaNum


str1 = raw_input("please input a string :")
print "digit :", digitNum(str1)
print "alpha :", alphaNum(str1)
