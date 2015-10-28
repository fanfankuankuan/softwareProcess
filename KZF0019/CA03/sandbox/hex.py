'''
Created on Oct 27, 2015

@author: KevinFAN
'''
import random

b = random.randrange(1,32767)
c = hex(b)
d = c[2:]
if b < 16:
    d = '000' + d
if b < 256 and b >= 16:
    d = '00' + d
if b < 4096 and b >= 256:
    d ='0' + d
print d
b = random.randrange(32768,65535)
c = hex(b)
d = c[2:]
print d