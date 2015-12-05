'''
Created on Dec 4, 2015

@author: KevinFAN
'''
import CA04.prod.Environment as Environment
import math

class SolarCollector(object):
     def __init__(self):
  
        self.environment = None
        
     def configure(self, environment = None):
        """
        Passes information about the simulation environment to the collector.
        Returns: True
        """
        diagMethod = "configure:  "
        if (environment == None):
            raise ValueError('SolarCollector.configure:  No environment been configured')
        if not (isinstance(environment, Environment.Environment)):
            raise ValueError('SolarCollector.configure:  No environment been configured')
        self.environment = environment
        return True
    
     def getDegradation(self):
        if (self.environment != None):
            return self.environment.degradation
        return None
    
    
     def serviceRequest(self):
    
        if (self.environment == None):
            raise ValueError("SolarCollector.serviceRequest:  environment has not yet been called")
        
        daytime = long((23*3600+56*60+4.1)*1e6)
        RadSatellite=2*math.pi*(self.environment.SimulatedClock%daytime)/daytime
        
        if (RadSatellite <= 8.6 or RadSatellite >= 351.4):
            ret = "0000"
        else:
            degradation = self.getDegradation()
            energy = int("7fff", 16) * (100 - degradation) / 100
            ret = '{0:04x}'.format(int(energy)) 
            
        self.environment.incrementTime(40)
        return ret