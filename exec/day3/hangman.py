#coding=utf-8
import string
#�ж��Ѿ��µ��ַ��Ƿ�����붼������,
#�Ѿ��µ����ַ���ɵ��ַ���Ҫ���������ַ����ſ���
#���������ַ�����'abc',�µ����ַ�����'adfebfdc',�����ſ���˵�Ǹ����������ַ���
def word_guessed(secret_word,letters_guessed):
 for i in secret_word:
  if i not in letters_guessed:
   return False    
 return True         
 
#��ӡ�Ѿ��µ��������ַ���������ַ�
#����˵�����ַ�����'abc',����������ַ���b�Ļ���������Ӧ��λ�ô�ӡ'-b-'
#�ٴ�������ַ���c�Ļ����ʹ�ӡ'-bc'
def print_guessed(secret_word,letters_guessed):
 secret_len=['-']*len(secret_word)   
 for idxi,i in enumerate(letters_guessed):  
  for idxj,j in enumerate(secret_word):   
   if i==j:   
    secret_len[idxj]=i
 print 'current guess result:',''.join(secret_len)  
 
#�������Ϸ�������Բ�26��
#��26��֮�ڲ��У��ʹ�ӡ�¶���
#����26�λ�û�в��У��ʹ�ӡʧ��
#ÿ��һ�¶���ʾ��ʣ�µĴ���
def print_hangman():
 max_count=26     #�����ԲµĴ���
 guessed_count=0  #�Ѿ��µĴ���
 i=0
 while i<max_count:
  if word_guessed(secret_word,letters_guessed):  
   break
  letters=raw_input('������Ҫ�µ���ĸ')
  print 'guess left:',max_count-guessed_count  
  letters_guessed.append(letters)   
  print_guessed(secret_word,letters_guessed)   
  i+=1
  guessed_count+=1
 
 if word_guessed(secret_word,letters_guessed):  
  print 'you win,the word is %s' %secret_word
 else:                            
  print 'you loss,not guessed'
 
 print 'һ������%d��' %guessed_count  
secret_word='good'  #�����ַ���
letters_guessed=[]   #���ڴ���Ѿ��µ��ַ�
print_hangman()  