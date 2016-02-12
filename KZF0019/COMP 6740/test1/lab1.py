'''
Created on Feb 11, 2016

@author: KevinFAN
'''

import random
list = []
class lab1(object):
    def num(self):
        file = open('lab1.txt','w')    #open a file to collect data
        #for r in range(1,10,1):      #set the value of r
        r = 3
        for p in range(1,9,1):   #set the value of p
        # p=1 
            for i in range(1,100,1):  #simulate enough times
                Failure = 0
                Success = 0
#                 print p
                v = float(p)/10
#                 print v
                while(Success<r):      
                    number = random.randrange(1,10,1)     #get a random number to judge success
                    v2 = float(number)/10
                    if v2 <=v:
                        Success = Success +1            #record success times
                        #print Success
                    else:
                        Failure = Failure + 1           #record failure time
                st = str(Failure) + ' '
                try:
                    file.writelines(st)
                except:
                    pass
        file.close()                #record the data of simulation into the file

start = lab1()
run = start.num()