'''
Created on Feb 11, 2016

@author: KevinFAN
'''
import math
import random
import os



list = []
class lab1(object):
    def num(self):
        file = open('lab1.txt','w')
        for r in range(1,10,1):
            for p in range(1,9,1):
                for i in range(1,100,1):
                    Failure = 0
                    Success = 0
    #                 print p
                    v = float(p)/10
    #                 print v
                    while(Success<r):
                        number = random.randrange(1,10,1)
                        v2 = float(number)/10
                        if v2 <=v:
                            Success = Success +1
                            #print Success
                        else:
                            Failure = Failure + 1
                    file.write(Failure)
#                     list.append(Failure)
        
#         file = open('lab1.txt','w')
#         file.write(list)
        file.close()
        #print list

start = lab1()
run = start.num()