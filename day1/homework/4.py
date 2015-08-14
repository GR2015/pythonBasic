a_list=[3,5,6,12]

print a_list[0]

print a_list[3]

print a_list[1:]

print a_list

a_list.reverse()
print a_list

a_list=[3, 5, 6, 12]
b_list=[]
for i in a_list:
  i*=3
  b_list.append(i)

print b_list



a_list=[3, 5, 6, 12]
b_list=[]
for i in a_list:
  if i%2==0:
    t=True
  else:
    t=False
  b_list.append(t)

print b_list
