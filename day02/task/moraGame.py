#coding=utf-8
import random
'''
剪刀石头布游戏
'''

print "************人机剪刀石头布游戏*************"
print "*                                         *"
print "*        1表石头  2表剪刀   3表布         *"
print "*               E/s结束游戏               *"
print "*                                         *"
print "*****************Python实现****************"

winNum = 0  #赢的次数
EqualNum = 0 #平局的次数
FaildNum = 0 #失败的次数

while 1 :
  #游戏规则数字列表
  gameNumList = ['1','2','3']
  '''游戏结果字典,输入在前，随机数在后
     E-平局 W-人赢 F-机器赢
  '''
  gameResultDict = {'11':'E', '12':'W', '13':'F', \
                    '21':'F', '22':'E', '23':'W', \
                    '31':'W', '32':'F', '33':'E'}
  
  #从键盘获取游戏数字或者是退出符号
  
  inputNum = raw_input("请出拳：")
  if inputNum == 'e' or inputNum == 'E' :
    print "您共玩%d局，赢%d局，平%d局，输%d局" %((winNum + EqualNum + FaildNum),winNum,EqualNum,FaildNum)
    exit()
  elif inputNum not in gameNumList :
    print "\n请按游戏规则输入代表剪刀石头布的正确数字！\n1表石头 2表剪刀 3表布"
    continue
    
  #随机生成1-3之间的数，代表机器出拳
  randNum = str(random.randint(1,3))
  
  if gameResultDict[inputNum + randNum] == 'E' :
    print "平局\n"
    EqualNum += 1
  elif gameResultDict[inputNum + randNum] == 'W' :
    print "你赢\n"
    winNum += 1
  elif gameResultDict[inputNum + randNum] == 'F' :
    print "你输\n"
    FaildNum += 1  
  
  
  
  
  





