#coding=utf-8

#一个字符串 list，每个元素是 1 个 ip，输出出现次数最多的 ip

def mostIP(lista):
  dip={}
  #IP和个数保存到字典中
  for i in lista:
    if dip.has_key(i):
      dip[i]+=1
    else:
      dip[i]=1
 
  #IP个数保存到列表中，排序，取最后一个即最大
  listv=[]
  for k,v in dip.items():
    listv.append(v)

  listv.sort() 
  max=listv[-1]

  #返回字典中值最大的key，即IP
  #可能存在多个IP出现次数相同，所以使用list保存
  listk=[]
  for k in dip.keys():
    if dip[k]==max:
      listk.append(k)
   
  return listk


a=["10.1.0.1","10.1.0.2","10.1.0.1","10.1.2.58","10.1.0.2"]
print "a=",a
print "出现次数最多的IP为:", mostIP(a)