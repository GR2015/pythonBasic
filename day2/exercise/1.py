a=range(10)

#list1
for i in a:
  print i

#list2
for idx,i in enumerate(a): #ö�ٺ������������У������������������Ӧ��Ԫ��
  print idx,i

#list3
a='abcdefg'
for idx in range(len(a)):
  print idx,a[idx]

#list4
cnt=0
for i in a:
  print cnt,i
  cnt+=1

#list5
cnt=0
while cnt<len(a):
  print cnt,a[cnt]
  cnt+=1


#dict
