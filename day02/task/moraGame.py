#coding=utf-8
import random
'''
����ʯͷ����Ϸ
'''

print "************�˻�����ʯͷ����Ϸ*************"
print "*                                         *"
print "*        1��ʯͷ  2�����   3��         *"
print "*               E/s������Ϸ               *"
print "*                                         *"
print "*****************Pythonʵ��****************"

winNum = 0  #Ӯ�Ĵ���
EqualNum = 0 #ƽ�ֵĴ���
FaildNum = 0 #ʧ�ܵĴ���

while 1 :
  #��Ϸ���������б�
  gameNumList = ['1','2','3']
  '''��Ϸ����ֵ�,������ǰ��������ں�
     E-ƽ�� W-��Ӯ F-����Ӯ
  '''
  gameResultDict = {'11':'E', '12':'W', '13':'F', \
                    '21':'F', '22':'E', '23':'W', \
                    '31':'W', '32':'F', '33':'E'}
  
  #�Ӽ��̻�ȡ��Ϸ���ֻ������˳�����
  
  inputNum = raw_input("���ȭ��")
  if inputNum == 'e' or inputNum == 'E' :
    print "������%d�֣�Ӯ%d�֣�ƽ%d�֣���%d��" %((winNum + EqualNum + FaildNum),winNum,EqualNum,FaildNum)
    exit()
  elif inputNum not in gameNumList :
    print "\n�밴��Ϸ��������������ʯͷ������ȷ���֣�\n1��ʯͷ 2����� 3��"
    continue
    
  #�������1-3֮����������������ȭ
  randNum = str(random.randint(1,3))
  
  if gameResultDict[inputNum + randNum] == 'E' :
    print "ƽ��\n"
    EqualNum += 1
  elif gameResultDict[inputNum + randNum] == 'W' :
    print "��Ӯ\n"
    winNum += 1
  elif gameResultDict[inputNum + randNum] == 'F' :
    print "����\n"
    FaildNum += 1  
  
  
  
  
  





