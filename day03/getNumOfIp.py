#!/usr/bin/python
#coding=utf-8
'''
一个字符串 list，每个元素是 1 个 ip，输出出现次数最多的 ip
'''
 
def calcIpNum(ipList) :
  ipDict = {}
  for i in ipList :
    if ipDict.has_key(i) :
      ipDict[i] += 1
    else :
      ipDict[i] = 1
  max = 0
  key = ' '
  for i in ipDict.keys() :
    print "IP:"+i + " times：" + str(ipDict[i])
    if ipDict[i] > max :
      max = ipDict[i]
      key = i
  return key,max
  

    
ipList = ['10.12.6.8','192.168.6.8','192.126.61.89','22.32.45.18',\
          '10.12.6.8','10.12.6.8','172.168.61.80','192.126.61.89','10.12.6.8']

tupleIp = calcIpNum(ipList)
print "most times of IP：" + tupleIp[0] + " times：" + str(tupleIp[1])
