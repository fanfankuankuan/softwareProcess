'''
Created on Nov 30, 2015

@author: KevinFAN
'''
import CA02.prod.Environment as En
import random

class device(object):
    
    def __init__(self):
        pass
    def configure(self,environment = None):
        if not(isinstance(environment, En.Environment)):
            raise ValueError("device.configure:  file is invalid")
        if environment == None:
            raise ValueError("device.configure:  input error.")
        self.env = environment
        return True
    def serviceRequest(self):
        
        a = random.randrange(1,4)
        if a == 1:
            return "0000"
        if a == 2 or a == 3:
            b = random.randrange(1,32767)
            c = hex(b)
            d = c[2:]
            if b < 16:
                d = '000' + d
            if b < 256 and b >= 16:
                d = '00' + d
            if b < 4096 and b >= 256:
                d ='0' + d
            return d
        if a == 4 :
            b = random.randrange(32768,65535)
            c = hex(b)
            d = c[2:]
            return d
        #self.env.incrementTime(40)
#d = device()
#a = d.serviceRequest()
#print a
