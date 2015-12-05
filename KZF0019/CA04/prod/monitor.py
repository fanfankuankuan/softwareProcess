'''
Created on Nov 30, 2015

@author: KevinFAN
'''
import types
from genericpath import isfile
import os
import CA02.prod.Environment as En


class Monitor(object):
    def __init__(self):
        pass
    def initialize(self,logFile):
        if(logFile == None):
            raise ValueError("monitor.intialize:  invalid file type")
            return False
        if not(isinstance(logFile, types.StringType)):
            raise ValueError("monitor.intialize:  invalid file name")
            return False
        #if not isfile(logFile):
        #    raise ValueError("monitor.intialize:  the file name is not a file")
        if os.path.exists(logFile):
            #raise ValueError("monitor.intialize:  file exists by the specified file name")
            self.fw = open(logFile,'a')
            return False
        else:
            self.fw = open(logFile,'a')
            #self.time = 0
            
            return True
    def configure(self,environment):
        if not(isinstance(environment, En.Environment)):
            raise ValueError("monitor.configure:  file is invalid")
        self.env = environment
        self.time = 0
        self.n = 0
        return True
    def serviceRequest(self,source=None,target=None,event= None):
        if source == None or target == None or event == None:
            return 1
            raise ValueError("Monitor serviceRequest:  the input value is not complete.")
        self.time = self.env.getTime()
        self.fw.write(str(self.time))
        self.fw.write('\t')
        self.fw.write(source)
        self.fw.write('\t')
        self.fw.write(target)
        self.fw.write('\t')
        self.fw.write(event)
        self.fw.write('\n')
        #simulatedTime += 40
        if (self.n % 2==0 ):
            self.env.incrementTime(40) 
        self.n = self.n + 1
        return self.time
        
