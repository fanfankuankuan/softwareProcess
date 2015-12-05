'''
Created on Nov 30, 2015

@author: KevinFAN
'''
import types
from genericpath import isfile
import CA02.prod.Environment as En
import CA02.prod.StarSensor as St
import CA04.prod.device as De
import CA04.prod.monitor as Mo
import CA04.prod.SolarCollector as So
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
        
        #parm and name
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
       
    
        if len(self.b) == 5 and len(self.c) == 6 and len(self.a) == 6:
            for i in range(6):
                if self.a[i] == "starTime" or "rotationalPeriod" or "logFile" or "degradation" or "fieldOfView" or "starFile":
                    a2 = a2 + 1
                if self.c[i] == "10000000" or "logfile.txt" or "starFile":
                    a3 = a3 + 1
            for i in range(5):
                if self.b[i] == "SolarCollector" or "Environment" or "Monitor" or "StarSensor" or "Device":
                    a1 = a1 + 1
            if not a1 == 5:
                raise ValueError("Controller.intialize:  the information of component is missing")
            if not a2 == 6:
                raise ValueError("Controller.intialize:  the information of name is missing")
            if not a3 == 6:
                raise ValueError("Controller.intialize:  the information of parm is missing") 
        else :
            raise ValueError("Controller.initialize:  the file missed component.")
        
                
        return self.d
                
       

    def run(self):
        microseconds = self.c[0]
        
        try :
            microseconds = int(microseconds)
        except:
            raise ValueError("Controller.run: invalid microseconds")
        result = []
        
        simulatedTime = 0
        
        
        Solar = So.SolarCollector()
        
        
        myEnv = En.Environment()
        myEnv.StarTime(int(microseconds))
        myEnv.getTime()
        
        Solar.configure(myEnv)
        myEnv.setdegradationnum(self.c[2])
        #Mon = Mo.Monitor
        Devices = De.device()
        Devices.configure(myEnv)
        myStarSensor = St.StarSensor(float(self.c[4]))
        
        #Mon.initialize(self.pElement[1])  
        myEnv.setRotationalPeriod(int(self.c[1]))
        myStarSensor.configure(myEnv)
        #Mon.configure(myEnv)  
        
        mm = Mo.Monitor()
        mm.configure(myEnv)
        mm.initialize(str(self.c[3]))
        #if microseconds > self.timeLimit:
        #    flag = 1
        
        time1 = self.z[0]
        if len(self.d) > 0:
            while (int(time1) > int(simulatedTime + microseconds)):
                for i in range(0,len(self.d)):
                    #while(int(simulatedTime + microseconds) > self.c[0] ):
                    if self.d[i] == "SolarCollector":
                        r = Solar.serviceRequest()
                        result.append(r)
                        simulatedTime += 40
                        mm.serviceRequest("Controller","SolarCollector","service")
                        #simulatedTime += 40
                        mm.serviceRequest("SolarCollector","Controller",str(r))
                    if self.d[i] == "Device":
                        r = Devices.serviceRequest()
                        result.append(r)
                        simulatedTime += 40
                        mm.serviceRequest("Controller","Device","serviceRequest")
                        #simulatedTime += 40
                        mm.serviceRequest("Device","Controller",str(r))
                    if self.d[i] == "StarSensor":
                        r = myStarSensor.serviceRequest()
                        result.append(r)
                        simulatedTime += 40
                        mm.serviceRequest("Controller","StarSensor","serviceRequest" )
                        #simulatedTime += 40
                        mm.serviceRequest("StarSensor","Controller",str(r))
                    #myEnv.incrementTime(40)
                    #simulatedTime += 40
        else:
            raise ValueError("Controller.run: invalid Frame")
        
        return simulatedTime + microseconds
    
#d = controller()
#f = d.initialize("abc.xml")
#z = d.run() 
#print z
#print f
