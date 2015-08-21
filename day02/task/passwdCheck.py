#icoding=utf-8

listNum = []
dictNum = {'digitNum':0, 'alphaNum':0, 'otherNum':0}
passwd = raw_input("input:")
passwdLen = len(passwd)
for i in passwd :
  if i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z' :
    dictNum['alphaNum'] += 1
  elif i >= '0' and i <= '9' :
    dictNum['digitNum'] += 1
  else :
    dictNum['otherNum'] += 1
listNum = dictNum.values()
if listNum.count(0) == 0 and passwdLen >= 8:
  print "Ç¿"
elif listNum.count(0) == 1 and passwdLen >= 8:
  print "ÖĞ"
else :
  print "Èõ"
