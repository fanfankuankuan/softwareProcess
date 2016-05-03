'''
Created on Mar 11, 2016

@author: KevinFAN
'''
import random
import math
import matplotlib.pyplot as plt
import numpy as np
class GenerateNegativeBinomial(object):
    def __init__(self):
        pass
    def input(self,p=None,k=None):
        print "Please input the value of p (probability of success): "
        p = input()
        if p >1 and p<0:
            print "The input is not correct!"
#         print p
        print "Please input the value of r (the success number):"
        k = input()
#         print r
        j=0
        list = []
        f = open('NegativeBinomial.dat','w')
        while (j<250):
            data = None
            r = random.randrange(0,100)
            p1 = float(math.pow(p,k))
            h = 1-p
            p2 = float(math.pow(h,r))
            z = r+k-1
            ma = GenerateNegativeBinomial.sed(self,z,r)
            if k >2:
                ma1 = GenerateNegativeBinomial.sed2(self,k)
            if k == 2:
                ma1 = 2
            else:
                ma1 = 1
            data = ma / ma1 * p1 * p2
            if data <1:
                j=j+1
                list.append(data)
                f.write(str(data)+'\n')
        return list
        f.close()
    def sed(self,n,x):
    
        fact = 1
        for i in range(x,n+1):
            fact=fact*i
        return fact
    def sed2(self,z):
        fact = 1
        for i in range(2,z+1):
            fact = fact*i
        return fact
    def test1(self):
        plt.figure(1)
        x = np.linspace(0, 1, 1000)
        r = 5
        for p in range(5,100,5):
            p = float(p)/100
            list = sorted(self.input(p, r))
            plt.plot(x, list)
        plt.show()
#         print list1
    def test2(self):
        plt.figure(2)
        x = np.linspace(0, 1, 1000)
        p = 0.5
        for r in range(1,20,1):
            list = sorted(self.input(p, r))
            plt.plot(x, list)
        plt.show()
start = GenerateNegativeBinomial()
# a = start.test1()
# b = start.test2()
c= start.input()