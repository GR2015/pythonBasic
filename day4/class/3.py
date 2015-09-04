#coding=utf-8
def giveChange(itemPrice,giveMoney):
  m=giveMoney-itemPrice
  if m!=0:
    listy=[1,2,5,10,20]
    listy.sort()
    listy.reverse()
    dictx={}
    
    
    for i in listy:
      x=m/i
      m=m%i
      dictx[i]=x
      
    for k,v in dictx.items():
      print "%d’≈%d" %(v,k)

  else:
    print "no money left"
  

giveChange(2,100)