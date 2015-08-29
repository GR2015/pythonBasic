# coding=utf-8

List = ['10.10.1.10', '10.10.2.10', '10.10.0.10', '10.10.0.10']
def ip(List):
  a = {}
  for i in List:
    a[i] = List.count(i)

  m = max(a.values())  # 求values的最大值
  for key, valuer in a.items():
    if m == valuer:
        print key

ip(List)