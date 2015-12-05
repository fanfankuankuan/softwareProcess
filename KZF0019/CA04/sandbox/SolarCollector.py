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
    def serviceRequest(self,num):
        degradation = int(num)
        daytime = long((23*3600+56*60+4.1)*1e6)
        print self.env.getTime()
        RadSatellite=2*math.pi*(self.env.getTime()%daytime)/daytime
        
        if (RadSatellite <= 8.6 or RadSatellite >= 351.4):
            ret = "0000"
        else:
            degradation = self.getDegradation()
            energy = int("7fff", 16) * (100 - degradation) / 100
            ret = '{0:04x}'.format(int(energy)) 
            
        #self.environment.incrementTime(40)
        return ret
        
        
#         x= (100 - float(minbr)) / 100 * 32767
#        
#         a = int(x)
#         b = hex(a)
#         tempStr = 'x'
#         c = b.find(tempStr)
#         d = b[(b.find(tempStr)+1):]
#         if x>=1.6 and x<25.6:
#             d = "00"+d
#             
#         elif x>=0 and x<1.6:
#             d ="000"+d
#             
#         elif x>=25.6 and x<409.6:
#             d = "0"+d
#            
#         elif x>=409.6:
#             pass
#         elif x<0 and x>=-383.9:
#             b = hex(4095+a)
#             c = b.find(tempStr)
#             d = b[(b.find(tempStr)+1):]
#             d = "f"+d
#             
#         else:
#             raise ValueError("")
#         return d