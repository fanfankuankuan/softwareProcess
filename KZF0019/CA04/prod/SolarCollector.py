'''
Created on Nov 30, 2015

@author: KevinFAN
'''
import CA02.prod.Environment as En
import math
class SolarCollector(object):
    def __init__(self):
        pass

    def configure(self,environment):
        if not(isinstance(environment, En.Environment)):
            raise ValueError("device.configure:  file is invalid")
        self.env = environment
        #print En.Environment.getTime(self)
        return True
    def serviceRequest(self):
        num = self.env.getdegradationnum()
        degradation = int(num)
        daytime = long((23*3600+56*60+4.1)*1e6)
        #print degradation
        RadSatellite=2*math.pi*(self.env.getTime()%daytime)/daytime
        #print RadSatellite
        if (RadSatellite <= 8.6 or RadSatellite >= 351.4):
            ret = "0000"
        else:
            degradation = self.getDegradation()
            energy = int("7fff", 16) * (100 - degradation) / 100
            ret = '{0:04x}'.format(int(energy)) 
        
        #self.environment.incrementTime(40)
        return ret