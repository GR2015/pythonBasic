# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:26:50 2015

@author: cindychen
"""
#在某个目录下查找是否存在某个文件或目录
import os

def Find_file_or_dir(findpath,file_or_dir):
    for root,dirs,files in os.walk(findpath):
        if file_or_dir in dirs:
            print root+'\\'+file_or_dir
        if file_or_dir in files:
            print root+'\\'+file_or_dir
            
Find_file_or_dir('d:\\python\\0924','aaa')