'''
Created on Oct 18, 2015

@author: KevinFAN
'''
import types
from genericpath import isfile
import CA02.prod.Environment as En
import CA02.prod.StarSensor as St
import CA03.prod.device as De
import CA03.prod.monitor as Mo
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
        
        #parm and definition
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
        
        #component
        bb = self.dom.getElementsByTagName('definition')
        self.b= []
        for i in range(0,len(bb)):
            item = bb[i]
            un = item.getAttribute("component")
            self.b.append(un)
            
        #device
        dd = self.dom.getElementsByTagName('device')
        self.d = []
        for i in range(0,len(dd)):
            self.d.append(dd[i].firstChild.data)
        
        #rate
        
        zz = self.dom.getElementsByTagName("frame")
        self.z = []
        for i in range(0,len(zz)):
            ite = zz[i]
            ui = ite.getAttribute("rate")
            self.z.append(ui)
        #print self.z
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
        
                
        return self.d
                
       

    def run(self,microseconds = None):
        try :
            microseconds = int(microseconds)
        except:
            raise ValueError("Controller.run: invalid microseconds")
        result = []
        simulatedTime = 0
        myEnv = En.Environment()
        myEnv.getTime()
        
        #Mon = Mo.Monitor
        Devices = De.device()
        Devices.configure(myEnv)
        myStarSensor = St.StarSensor(float(self.c[2]))
        
        #Mon.initialize(self.pElement[1])  
        myEnv.setRotationalPeriod(int(self.c[0]))
        myStarSensor.configure(myEnv)
        #Mon.configure(myEnv)  
        mm = Mo.Monitor()
        mm.configure(myEnv)
        mm.initialize(str(self.c[1]))
        #if microseconds > self.timeLimit:
        #    flag = 1
        time1 = self.z[0]
        if len(self.d) > 0:
            while (int(time1) > int(simulatedTime + microseconds)):
                for i in range(0,len(self.d)):
                    if self.d[i] == "Device":
                        r = Devices.serviceRequest()
                        result.append(r)
                        simulatedTime += 40
                        mm.serviceRequest("Controller","Device","serviceRequest")
                        mm.serviceRequest("Device","Controller",str(r))
                    if self.d[i] == "StarSensor":
                        r = myStarSensor.serviceRequest()
                        result.append(r)
                        simulatedTime += 40
                        mm.serviceRequest("Controller","StarSensor","serviceRequest" )
                        mm.serviceRequest("StarSensor","Controller",str(r))
                    myEnv.incrementTime(40)
                    
        else:
            raise ValueError("Controller.run: invalid Frame")
        #print result
        #print len(result)            
        
        
        #print myEnv.getTime()
        
        
        
        return simulatedTime + microseconds
    
d = controller()
f = d.initialize("abc.xml")
z = d.run(990000) 
#print z
#print f
