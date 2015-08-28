#coding=utf-8
def  max(list):
  '''your code'''
  ''' return max value of list'''
  max=list[0]
  sec=list[0]
  for i in list:
    if i>max:
      sec=max
      max=i
    elif i>sec:
      sec=i
  print sec
  return sec,max

a=[2,3,6,5,4,7]
max(a)



     