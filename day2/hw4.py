#coding=utf-8
'''
检查密码
passwd='dsfaf12'

密码强度第一题：
强 >=8  并且 密码包含字母和数字
中 >=8, 或者包含字母，或者数字
弱 <8 ，包含字母或者数字

c1 : 长度>=8
c2: 包含字母
c3: 包含数字

强：满足c1,c2,c3
中：满足c1 and (c2 or c3)
弱：满足c2 or c3


密码强度第二题：
c1 : 长度>=8
c2: 包含数字
c3: 包含！@#￥%

强：满足c1,c2,c3
中: 满足2个条件
弱：满足1个条件
'''

#密码强度第一题
passwd='dsfaf12'
#passwd=raw_input("请输入密码：")
x=len(passwd)
if x>=8:
  flagc1=True
else:
  flagc1=False

for i in passwd:
  if i >='a' and i <='z' or i >='A' and i <='Z':
    flagc2=True
    break
  else:
    flagc2=False

for i in passwd:
  if i >='0' and i <='9':
    flagc3=True
    break
  else:
    flagc3=False

while (flagc1):
  if (flagc2 and flagc3):
    print "密码强度为：强"
    break
  elif (flagc2 or flagc3):
    print "密码强度为：中"
    break
  else:
    print "密码包含非字母数字字符"
    break

while (flagc1==False):
  if (flagc2 or flagc3):
    print "密码强度为：弱"
    break
  else:
    print "密码包含非字母数字字符"
    break
  

#密码强度第二题：
passwd='dsfaf12'
#passwd=raw_input("请输入密码：")
x=len(passwd)
if x>=8:
  flagc1=True
  c1=1
else:
  flagc1=False
  c1=0

for i in passwd:
  if i in "！@#￥%":
    flagc2=True
    c2=1
    break
  else:
    flagc2=False
    c2=0

for i in passwd:
  if i >='0' and i <='9':
    flagc3=True
    c3=1
    break
  else:
    flagc3=False
    c3=0

c=c1+c2+c3
if c==3:
  print "强"
elif c==2:
  print "中"
elif c==1:
  print "弱"
else:
  print "太弱"