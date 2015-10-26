'''
Created on Oct 18, 2015

@author: KevinFAN
'''
import types
from genericpath import isfile
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
        if not isfile(logFile):
            raise ValueError("monitor.intialize:  no file exists by the specified file name")
            return False
        else:
            return True
    def configure(self,environment):
        if not(isinstance(environment, En.Environment)):
            raise ValueError("StarSensor.configure:file is invalid")
        self.env = environment
        return True
    def serviceRequest(self,source,target,event):
        pass
    