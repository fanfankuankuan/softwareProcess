'''
Created on Sep 4, 2015

@author: KevinFAN
'''
import string
import os
import sys

def Max(x,y):
        return x+y

def Min(x,y):
        return x-y
    
class mix():
    racp = []
    dcrp = []
    fov = []

try:
    racp = input('Enter the xnum:')
    dcrp = input('Enter the ynum:')
    fov  = input('Enter the field of view:')
except EOFError:
    print 'Error Input!'
    sys.exit()
    
xMaxnum = Max(racp,fov)
xMinnum = Min(racp,fov)
yMaxnum = Max(dcrp,fov)
yMinnum = Min(dcrp,fov)

j = 0
list1 = []
list2 = []
path = os.path.expanduser(r"~/Documents/COMP 6700/Sao.txt")


with open(path) as f:
    content = f.read()
    for i in content.splitlines():
            fields = i.split('\t')
            j += 1
            #print fields[2]
            if (string.atof(fields[2]) <= xMaxnum and string.atof(fields[2]) > xMinnum): 
                if (string.atof(fields[3]) <= yMaxnum and string.atof(fields[3]) > yMinnum):
                    print "Star ID",fields[0], "in the square, the brightness is ", fields[1] 
                    list1.append(fields[0])
                    list2.append(fields[1])
                    
                else :
                    pass
            else :
                pass     
#print list1
#print list2
minbr = list2[0]
for k in list2 :
    if k < minbr :
        minbr = k


print 'the bright star ID is ', list1[list2.index(minbr)],'the brightness is: ',minbr
