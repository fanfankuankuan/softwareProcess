'''
Created on Feb 11, 2016

@author: KevinFAN
'''

import random


list = []
class lab1(object):
    def num(self):
        file = open('lab1.txt','w')
        for r in range(1,10,1):
#             for p in range(1,9,1):
            for p in range(1,4,1):
                for i in range(1,1000,1):
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
                    st = str(Failure) + ' '
                    try:
                        file.writelines(st)
                    except:
                        pass
        file.close()

start = lab1()
run = start.num()