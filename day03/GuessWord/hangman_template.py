#coding=utf-8
# Name:
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
import random
from random import randrange
from string import *
from hangman_lib import *


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "C:\\words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()



def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word


# CONSTANTS
#MAX_GUESSES = 6

# GLOBAL VARIABLES 

result_list = []
letters_guessed = []
alpha_dict = {}

# From part 3b:
def word_guessed(secret_word, alpha_guessed):
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    
    '''
    alpha_dict.has_key[alpha_guessed] == True
    ˵���Ѿ��¹�����ĸ��
    '''
    
    if alpha_guessed in secret_word and not alpha_dict.has_key(alpha_guessed) :
        alpha_dict[alpha_guessed] = 1
        return True
    return False




def print_guessed(secret_word, alpha_guessed):
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global result_list

    #randNum = random.randint(0,2)
    for idx, i in enumerate(secret_word) :
        if alpha_guessed == i :
            result_list[idx] = alpha_guessed
    print "current guess result :" + "".join(result_list)# + "-" * randNum
    
    


#ͳ�Ƶ����в�ͬ��ĸ���ܸ���
def alpha_number(word) :
    dictTmp = {}
    for i in word :
        if dictTmp.has_key(i) :
            dictTmp[i] += 1
        else :
            dictTmp[i] = 1   
    alphaNum = len(dictTmp.keys())
    return alphaNum
    
    
def play_hangman():

    global result_list
    
    mistakes_made = 0
    #secret_word = 'congratulate'
    secret_word = get_word()
    result_list =  ["-"] * len(secret_word)
    #�����У���ͬ��ĸ���ܸ���
    alphaTotalNum = alpha_number(secret_word)
    
    #��ʼ�´ʻ�����ڵ����в�ͬ�����ܸ�����2����alphaTotalNum + 2
    leftChances = alphaTotalNum + 2
    
    while 1 :
        if  alphaTotalNum <= 0 :
            print_hangman_image(0)
            print "Congratulate,You Win !!!"
            exit()
        elif leftChances == 0 and result_list.count('-') != 0:
            print_hangman_image(8)
            print "sorry, you die !!!"
            print "Answer :", secret_word
            exit()
            
        print "%d times left" %(leftChances)
        alpha_guessed = raw_input("please input a letters :").strip().lower()
        letters_guessed.append(alpha_guessed)
        if len(alpha_guessed) == 1 :
            if word_guessed(secret_word, alpha_guessed) :
                print_guessed(secret_word, alpha_guessed)
                #ÿ����һ�Σ�ʣ�µĲ´ʻ����1������´ʵ��ܳ��ȼ�1
                leftChances -= 1
                alphaTotalNum -= 1
                continue
            else :
                mistakes_made += 1
                leftChances -= 1
                print_hangman_image(mistakes_made)
                continue
        else :
            print "please input a letters, please try again !"
            continue
    
    #return None

#***************************�������*****************************

play_hangman()
