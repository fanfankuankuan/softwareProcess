'''
Created on Feb 11, 2016

@author: KevinFAN
'''
import math
import random


class lab1(object):
    def num(self):
        for r in range(1,10,1):
            for p in range(1,9,1):
                Failure = 0
                Success = 0
                v = float(p /10)
                while(Success<r):
                    number = random.randrange(1,10,1)
                    v2 = float(number/100)
                    if v2 < v:
                        Success = Success +1
                    else:
                        Failure = Failure + 1
                print (Success+Failure)