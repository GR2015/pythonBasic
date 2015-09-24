# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:50:59 2015

@author: cindychen
"""
#使用程序建立一个多级的目录，在每个目录下，新建一个和目录名字一样的txt文件,并写入1990
import os

def Create_dir_file(findpath,name_of_file,layers):
    #findpath表示开始路径，name_of_file表示要创建的文件or目录,layers表示要建立的目录层数 
    os.chdir(findpath)
    while layers>0:
        #创建目录
        if os.path.exists(findpath+'\\'+name_of_file):
            print 'the dir %s is exit' %(name_of_file)
        else:
            os.mkdir(name_of_file)
        #切换目录
        findpath=findpath+'\\'+name_of_file
        os.chdir(findpath)
        #创建文件并写入内容
        if os.path.exists(findpath+'\\'+name_of_file+'.txt'):
            print 'the file %s.txt is exit' %(name_of_file)
        f=open(name_of_file+'.txt','w')
        f.write('1990')
        f.close()
        #修改还需要创建多级目录的级数
        layers-=1
        
Create_dir_file('d:\\python\\0924\\','cindy',4)     
       