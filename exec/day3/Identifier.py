#coding=utf-8
#判断一个字符串是否是一个合法的标识符
def Identifier(str):
 if str=='':  
  return 'is not identifier '
 else:
  if str[0]>='0' and str[0]<='9':   
   return 'the frist chr is digit,is not identifier'
  else:
   for i in str:   
    if i=='_' or (i>='0' and i<='9') or (i>='a' and i<='z') or (i>='A' and i<='Z'):  
     flag='is identifier'
    else:                        
     return 'is not identifier'
   return flag
 
print '"kong"',Identifier('')
print '"kongge"',Identifier(' ')
print '"1dkjf"',Identifier('1dkjf')
print '"_"',Identifier('_')
print '"_123"',Identifier('_123')
print '"_123fkd"',Identifier('_123fkd')
print '"_123dfkj@#$"',Identifier('_123dfkj@#$')
print '"dkfj123"',Identifier('dkfj123')
print '"djfk_242"',Identifier('djfk_242')
print '"@#"',Identifier('@#')
print '"dkfj_@#fdf"',Identifier('dkfj_@#fdf')
print '"DKFj_fdf"',Identifier('DFKj_fdf')