'''
Created on 9/1/2015

@author: KevinFAN
'''
import os

path = os.path.expanduser(r"~/Documents/COMP 6700/SaoChart.txt")


with open(path) as f:
    content = f.read()
    for i in content.splitlines():
            fields = i.split('\t')
            print fields[0]
            print fields[1]
            #print fields[0:1]
            #print i
            #print i[0:6]
            #print i[7:10]
            #print i[11:21]
            #print i[22:]
            