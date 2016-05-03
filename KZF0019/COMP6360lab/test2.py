'''
Created on Mar 21, 2016

@author: KevinFAN
'''
import random
class test2(object):
    def count(self):

        for i in range(0,19):
            r = random.randrange(0,60000)
            r2 = (float(r)-30000)/100000
            print r2
a = test2()
start = a.count()
            