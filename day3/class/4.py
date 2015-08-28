#coding=utf-8
ĞèÒªĞŞ¸Ä
'''201.123.1.1
0 ~ 255'''
import sys
def isValidIp(ip):
  iplist=ip.split(".")
  
  if len(iplist)!=4:
    return False
  for i in iplist:  
    if (int(i)>=0 and int(i)<=255):
      flag=True
    else:
      flag=False
      break
  
  return flag

print isValidIp("255.255.200.1")
print isValidIp("255.a.a.a")
    