'''
Created on Mar 7, 2016

@author: KevinFAN
'''
import random
import math


class lab2(object):
    def __init__(self):
        pass
    def input(self):

        print "Please choice which distribution do you want? 1.uniform 2.exponential 3.normal"
        choice = input()
        if choice == 1:
            print "Please input the Max value of uniform distribution:"
            max1 = input()
            print "Please input the Min value of uniform distribution:"
            min1 = input()
            lab2.uniform(self,max1,min1)
        if choice == 2:
            print "Please input the Parameters of exponential distribution:"
            pa = input()
            lab2.exponential(self, pa)
        if choice == 3:
            print "Please input the mean of normal distribution:"
            mean1 = input()
            print "Please input the standard deviation of normal distribution:"
            variance1 = input()
            lab2.normal(self, mean1, variance1)
    def uniform(self,Max,Min):
        j = 0
        ans = None
        f=open('Uniform.dat','w')
        while (j<1000):
            i = random.randrange(0.0,100.0)
            i=float(i)/ 100
#             print i
            ans = float(Max-Min)*i + float(Min)
            j = j +1
            f.write(str(ans)+'\n')
#                 print ans
#                 print ans
           
        f.close()
    def exponential(self,z):
        j = 0
        ans = None
        f = open('exponential.dat','w')
        while (j<1000):
            i = random.randrange(0,5000)
#             print i
            if i>= 0:
                i = i/100.0
                h = float(-z*i)
             
                x =math.exp(h)
                
                ans = float(1-x)
                f.write(str(ans)+'\n')
                j =j+1
            if i<0:
                ans = float(0)
        f.close()
    def normal(self,mean,var):
        j = 0
        f = open('normal.dat','w')
        while (j<1000):
            
            ans = None
            ans = random.normalvariate(mean,var)
            f.write(str(ans)+'\n')
            j =j+1
        f.close()
    
        
start = lab2()
a = start.input()