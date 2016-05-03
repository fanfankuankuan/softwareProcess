'''
Created on Feb 11, 2016

@author: KevinFAN
'''
import random
class lab2(object):

    def test2(self):
        file = open('lab2.txt','w')
        for y in range(1,1000,1):        #set the test times
            conum = 0
            totalnum = 0
            codtime = []
            avgtime = 20
            avgrate = 0.2
            L = 0
            for i in range(1,1001,1):           #set the operating times to make data accurate
                pro = random.randrange(0,10,1)     #get a random number to judge success
                v2 = float(pro) / 10
                if v2 < avgrate:
                    conum = conum + 1         #record success times 
                    radtime = 20 + random.randrange(-19,19,1)
                    codtime.append(radtime+i)
                for z in range(0,len(codtime),1):
                    if codtime[z] == i:
                        conum = conum - 1
                totalnum = totalnum + conum
                
            
            L = float(totalnum) / 1000
            line = str(L) + ' '
            #print L
            try:
                file.writelines(line)
            except:
                    pass
        file.close()

start = lab2()
run = start.test2()