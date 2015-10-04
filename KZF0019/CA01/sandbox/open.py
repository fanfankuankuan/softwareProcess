'''
Created on Sep 3, 2015

@author: KevinFAN
'''
import os


def Star():
        Star.ID = []
        Star.BRIGHT = []
        Star.XNUM = []
        Star.YNUM = []

path = os.path.expanduser(r"~/Documents/COMP 6700/SaoChart.txt")


with open(path) as f:
    content = f.read()
    j = 0
    for i in content.splitlines():
            fields = i.split('\t')
            Star.ID = fields[0] + Star.ID
            Star.BRIGHT = fields[1] + Star.BRIGHT
            Star.XNUM = fields[2] + Star.XNUM
            #Star.YNUM = fields[3]
            j += 1
            #print Star.ID
            #print Star.BRIGHT
            #print i[11:21]
            #print i[22:]
            
   
    print Star.ID