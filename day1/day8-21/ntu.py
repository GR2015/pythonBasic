# coding=utf-8
a = int(raw_input('请输入一个N的长度：'))
for i in range(a):
    for j in range(a):
        if j == 0 or j == (a - 1):
            print "*",
        elif i == j:
            print "*",
        else:
            print " ",
    print
