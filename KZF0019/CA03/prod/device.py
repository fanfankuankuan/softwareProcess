'''
Created on Oct 18, 2015

@author: KevinFAN
'''
import CA02.prod.Environment as En
 
class device(object):
    def __init__(self):
        pass
    def configure(self,environment):
        if not(isinstance(environment, En.Environment)):
            raise ValueError("StarSensor.configure:file is invalid")
        self.env = environment
        return True
    def serviceRequest(self):
        pass
    