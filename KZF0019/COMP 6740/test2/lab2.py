'''
Created on Feb 11, 2016

@author: KevinFAN
'''
import random
class lab2(object):
    def test2(self):

        conum = 0
        totalnum = 0
        codtime = []
        avgtime = 15
        avgrate = 0.3
        
        for i in range(1,1001,1):
            pro = random.randrange(1,10,1)     #get a random number to judge success
            v2 = float(pro)/10
            if v2 <= avgrate:
                conum = conum +1            #record success times 
                radtime =random.randrange(1,29,1)
                codtime.append(radtime+i)
            for z in range(1,len(codtime),1):
                if codtime[z] == i:
                    conum = conum - 1
            totalnum = totalnum + conum
        
        L = float(totalnum) / 1000
        print L
        if L == avgtime*avgrate:
            print "The little's law is right"
        else:
            print "The little's law is wrong"
            
            
start = lab2()
run = start.test2()