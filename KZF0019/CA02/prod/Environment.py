'''
Created on Oct 1, 2015

@author: KevinFAN
'''
class Environment(object):
    simulatedClock = 0
    rotationalPeriod = 0
    def __init__(self):
        self.simulatedClock = 0
    
    def getTime(self):
        return self.simulatedClock       
    
    def StarTime(self,time1):
        self.simulatedClock = time1
        
    def setdegradationnum(self,degradation):
        self.degradation = degradation
        
    def getdegradationnum(self):
        return self.degradation
    
    def incrementTime(self, microseconds=None):
        if microseconds == None:
            raise ValueError("Environment.incrementTime:  param microseconds is needed")
        if not isinstance(microseconds, int):
            raise ValueError("Environment.incrementTime:  param microseconds must be a integer")
        if microseconds < 0:
            raise ValueError("Environment.incrementTime:  param microseconds must be GE 0")
        self.simulatedClock = self.simulatedClock + microseconds 
        return self.simulatedClock
    
    def setRotationalPeriod(self, microseconds=None):
        if microseconds == None:
            raise ValueError("Environment.setRotationalPeriod:  param microseconds is needed")
        if not isinstance(microseconds, int):
            raise ValueError("Environment.setRotationalPeriod:  param microseconds must be an integer")
        if microseconds < 1000000:
            raise ValueError("Environment.setRotationalPeriod:  param microseconds must be GE 1000000")
        self.rotationalPeriod += microseconds 
        return self.rotationalPeriod
    
    def getRotationalPeriod(self):
        if self.rotationalPeriod == 0:
            raise ValueError("Environment.getRotationalPeriod:  The rotational period has not previously been set") 
        return self.rotationalPeriod
