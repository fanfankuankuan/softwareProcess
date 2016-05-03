'''
Created on Mar 20, 2016

@author: KevinFAN
'''
import GenerateNegativeBinomial as en
class Test(object):
    def __inital__(self):
        pass
    def plotfigure(self):
        a = 0.5
        b = 3 
        input1 = en.GenerateNegativeBinomial
        list1 = input1.input(a,b)
        print list1

a = Test()
b = a.plotfigure()