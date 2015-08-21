# coding=utf-8
try:
    a = int(raw_input("请输入一个正整数："))
    for i in range(a):
        for j in range(a):
            if i == 0 or i == (a - 1) or j == 0 or j == (a - 1):
                print "*",
            else:
                print " ",
        print
except ValueError:
    print "请输入一个正整数！"
