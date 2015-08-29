#coding=utf-8
import string
#判断已经猜的字符是否把密码都涵盖了,
#已经猜到的字符组成的字符串要多于密码字符串才可以
#比如密码字符串是'abc',猜到的字符串是'adfebfdc',这样才可以说是覆盖了密码字符串
def word_guessed(secret_word,letters_guessed):
 for i in secret_word:
  if i not in letters_guessed:
   return False    
 return True         
 
#打印已经猜到的密码字符串里面的字符
#比如说密码字符串是'abc',本次输入的字符是b的话，就在相应的位置打印'-b-'
#再次输入的字符是c的话，就打印'-bc'
def print_guessed(secret_word,letters_guessed):
 secret_len=['-']*len(secret_word)   
 for idxi,i in enumerate(letters_guessed):  
  for idxj,j in enumerate(secret_word):   
   if i==j:   
    secret_len[idxj]=i
 print 'current guess result:',''.join(secret_len)  
 
#玩猜字游戏，最多可以猜26次
#在26次之内猜中，就打印猜对了
#超过26次还没有猜中，就打印失败
#每猜一猜都显示还剩下的次数
def print_hangman():
 max_count=26     #最多可以猜的次数
 guessed_count=0  #已经猜的次数
 i=0
 while i<max_count:
  if word_guessed(secret_word,letters_guessed):  
   break
  letters=raw_input('输入你要猜的字母')
  print 'guess left:',max_count-guessed_count  
  letters_guessed.append(letters)   
  print_guessed(secret_word,letters_guessed)   
  i+=1
  guessed_count+=1
 
 if word_guessed(secret_word,letters_guessed):  
  print 'you win,the word is %s' %secret_word
 else:                            
  print 'you loss,not guessed'
 
 print '一共猜了%d次' %guessed_count  
secret_word='good'  #密码字符串
letters_guessed=[]   #用于存放已经猜的字符
print_hangman()  