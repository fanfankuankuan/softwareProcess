'''
Created on Apr 24, 2016

@author: KevinFAN
'''
import random
import math

class lab3(object):
    def __init__(self):
        pass
    def uniform(self):
        st = 2
        print "The value of station is "
        print st
        FS = 1500
        print "The value of packet size is " 
        print FS 
        print " bytes"
        Bd = 10
        print "The value of bandwidth is " 
        print  Bd 
        print " Mbps"
        Tr = 1500.0 * 8.0 / 10000.0 
        
        print Tr
        Max = 0.06
        Min = 0.0001
        j = 0.0002
        f = open('lab3.dat','w')
        for i in range(1 , 1000):
            N = (j - Min) / (Max - Min)
            Po = 1 - Tr / N 
            S = Po * Tr
            j = j + 0.00005
            f.write(str(S)+'\n')
            print S 
        f.close()
start = lab3()
a = start.uniform()


        
        