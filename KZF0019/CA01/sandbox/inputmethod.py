'''
Created on Sep 3, 2015

@author: KevinFAN
'''
import sys
def Max(x,y):
        return x+y

def Min(x,y):
        return x-y
    
class Area():
     
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
print racp
print dcrp
print fov
    
xMax = Max(racp,fov)
xMin = Min(racp,fov)
yMax = Max(dcrp,fov)
yMin = Min(dcrp,fov)
print xMax
print xMin
print yMax
print yMin
    
