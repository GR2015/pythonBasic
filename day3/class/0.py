#coding=utf-8
#用递归的方式求列表的和
#l=[1,2,3,4,5]
#f(n） = f(n-1) + l[n-1] 

#n=len(n)
def f(n):
  for i in range(len(n)):
    if n==0:
      return l[-1]
    else:
      result=f(n-1) + l[n-1]
      return result

 
l=[1,2,3,4,5]   
print f(l)


所有字符在单词列表里，返回true
否则返回false



MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    pass # This tells your code to skip this function; delete it when you
         # start working on this function

for i in secret_word:
  if i in lettters_guessed":
    flag=True
  else:
    return False
    break

return flag