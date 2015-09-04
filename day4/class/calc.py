#coding=utf-8
def add(x,y):
  return x+y
  
def sub(x,y):
  return x-y
  
def multi(x,y):
  return x*y
  
def div(x,y):
  if y==0:
    print "除数不能为0"
  else:
    return x/y



if __name__ == "__main__":
  assert 3==add(1,2)
  assert 5==sub(6,1)
  assert 9==multi(3,3)
  assert 2==div(4,2)
