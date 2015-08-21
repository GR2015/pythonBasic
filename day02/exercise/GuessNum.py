#!/usr/bin/python
#coding=utf-8
import random

randNum = random.randint(1,100)
print "*****************猜数游戏开始*****************"
n = 0
while 1 :
  try :
    receiveNum = int(raw_input("please input a positive integer x："))
    print "\n"
  except :
    print "please input a positive integer!\nGame Over!!!"
  if receiveNum == randNum :
    print "Congratulation,You Win!!!"
    n += 1
    print "A total of %d steps" %(n)
    print "**********Game Over************"
    break
  elif receiveNum > randNum :
    print "Great!!!Please try again!!!"
    n += 1
    continue
  else :
    print "Small!!!Please try again!!!"
    n += 1
    continue




