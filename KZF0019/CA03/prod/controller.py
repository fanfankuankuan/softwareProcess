'''
Created on Oct 18, 2015

@author: KevinFAN
'''
import types
from genericpath import isfile
import CA02.prod.Environment as En
import CA03.prod.device as De
import  xml.dom.minidom

class controller(object):
    def __init__(self):
        pass 
    def initialize(self,architectureFile):
        if(architectureFile == None):
            raise ValueError("Controller.architectureFile:  invalid file type")
            return []
        if not(isinstance(architectureFile, types.StringType)):
            raise ValueError("Controller.architectureFile:  invalid file name")
        if not isfile(architectureFile):
            raise ValueError("Controller.architectureFile:  no file exists by the specified file name")
        dom = xml.dom.minidom.parse('abc.xml')
        
        pass

    def run(self,microseconds):
        if microseconds == None:
            raise ValueError("Controller.run:  input is invalid.")
        De.device.serviceRequest()
        return microseconds
    