'''
Created on Oct 18, 2015

@author: KevinFAN
'''
import types
from genericpath import isfile
import CA02.prod.Environment as En
import CA02.prod.StarSensor as St
import CA03.prod.device as De
import  xml.dom.minidom
import os
class controller(object):
    def __init__(self):
        pass 
    def initialize(self,architectureFile):
        #list = []
        if(architectureFile == None):
            raise ValueError("Controller.initialize:  invalid file type")
            return []
        if not(isinstance(architectureFile, types.StringType)):
            raise ValueError("Controller.initialize:  invalid file name")
        if os.path.splitext(architectureFile)[1] != '.xml':
            raise ValueError("Controller.initialize:  invalid file type")
        if not(len(os.path.splitext(architectureFile)[0]) >= 1):
            raise ValueError("Controller.initialize:  the file name violates")
        if not isfile(architectureFile):
            raise ValueError("Controller.initialize:  no file exists by the specified file name")
        try:
            self.dom = xml.dom.minidom.parse(architectureFile)
        except:
            raise ValueError("Controller.architectureFile:  Cannot open the file")
        root = self.dom.documentElement
        if root.nodeName == None:
            return []
        else:
            pass
        cc=self.dom.getElementsByTagName('parm')
        self.a = []
        self.c = []
        
        try:
            for i in range(0,len(cc)):
                self.c.append(cc[i].firstChild.data)
                item = cc[i]
                un=item.getAttribute("name")
                self.a.append(un)
        except:
            raise ValueError("Controller.initialized:  there is not enough information.")
        bb = self.dom.getElementsByTagName('definition')
        self.b= []
        
        #
        for i in range(0,len(bb)):
            item = bb[i]
            un = item.getAttribute("component")
            self.b.append(un)
        
        a1 = 0
        a2 = 0
        a3 = 0
       
        if len(self.b) == 4 and len(self.c) == 4 and len(self.a) == 4:
            for i in range(4):
                if self.b[i] == "Environment" or "Monitor" or "StarSensor" or "Device":
                    a1 = a1 + 1
                if self.a[i] == "rotationalPeriod" or "logFile" or "fieldOfView" or "starFile":
                    a2 = a2 + 1
                if self.c[i] == "10000000" or "logfile.txt" or "starFile":
                    a3 = a3 + 1
            if not a1 == 4:
                raise ValueError("Controller.intialize:  the information of component is missing")
            if not a2 == 4:
                raise ValueError("Controller.intialize:  the information of name is missing")
            if not a3 == 4:
                raise ValueError("Controller.intialize:  the information of parm is missing") 
        else :
            raise ValueError("Controller.initialize:  the file missed component.")
        
        for child in self.dom.childNodes :
            if child.tagName == "frame" :
                rate = child.getAttribute("rate")
                if rate == None:
                    raise ValueError("Controller.initialize:  rate doesn't exist")
                
                
       

    def run(self,microseconds):
        if microseconds == None:
            raise ValueError("Controller.run:  input is invalid.")
        #self.a       
        #self.b
        #self.c
        for i in len(self.c):
            operate = self.c[i]
            if (operate == "Device"):
                ans = De.device.serviceRequest()
            if (operate == "StarSensor"):
                ans = St.StarSensor.serviceRequest()
            print ans
            microseconds = En.Environment.incrementTime(40)
        dd = self.dom.getElementsByTagName('device')
        
        
        
        return microseconds
d = controller()
f = d.initialize("abc.xml")
#a = d.run(990000) 
#print a 
print f
