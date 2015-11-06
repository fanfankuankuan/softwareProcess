'''
Created on Nov 5, 2015

@author: KevinFAN
'''
import types
import xml.dom.minidom
import CA02.prod.Environment as En
import CA03.prod.monitor as Mo
import CA03.prod.device as De
import CA02.prod.StarSensor as ss
from genericpath import isfile

class Controller(object):
    def __init__ (self):
        pass
    def initialize(self,architectureFile=None):
        if (architectureFile == None) or not isinstance(architectureFile, types.StringType) or not isfile(architectureFile):
            raise ValueError("Controller.initialize: invalid file")
        self.res = []
        self.defi = [] 
        self.pElement = []
        self.pName = []
        try:
            DOMTree = xml.dom.minidom.parse(architectureFile)
            collection = DOMTree.documentElement
            definition = collection.getElementsByTagName("definition")
            frame = collection.getElementsByTagName("frame")
            device = collection.getElementsByTagName("device")
            parm = collection.getElementsByTagName("parm")
            root=DOMTree.documentElement
            #self.component['parm'] = collection.getElementsByTagName("parm")
        except:
            raise ValueError("Controller.initialize: invalid file")
        for tag in definition:
            if tag.hasAttribute("component"):
                #self.component['component'] = tag.getAttribute('component')
                a = str(tag.getAttribute("component"))
                self.defi.append(a)
            else :
                raise ValueError("Controller.initialize:  invalid file")   
        if not len(frame)>0 or not len(device)>0:
            raise ValueError("Controller.initialize:  invalid file") 
        for tag in parm:
            if tag.hasAttribute("name"):
                a = str(tag.getAttribute("name"))
                self.pName.append(a)
            else :
                raise ValueError("Controller.initialize:  invalid file")
        for i in range(0,4):
            try:
                node= root.getElementsByTagName('parm')[i]
            except:
                raise ValueError("Controller.initialize:  invalid file")
            for node in node.childNodes:
                if node.nodeType in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
                    a = str(node.data)
                    self.pElement.append(a)
        for tag in frame:
            if tag.hasAttribute("rate"):
                try:
                    rate = tag.getAttribute("rate")
                    self.timeLimit = int(rate)
                except:
                    raise ValueError("Controller.initialize:  invalid rate")
            else:
                raise ValueError("Controller.initialize:  cannot get rate")
        for i in range(0,len(device),1):
            devices = tag.getElementsByTagName('device')[i]
            a = str(devices.childNodes[0].data) 
            self.res.append(a)
        #print self.defi
        #print self.pName
        #print self.pElement
        #print self.res 
        return self.res
    def run(self,microseconds=None):
        try :
            microseconds = int(microseconds)
        except:
            raise ValueError("Controller.run: invalid microseconds")
        de1 = 0
        de2 = 0 
        de3 = 0
        de4 = 0
        pn1 = 0
        pn2 = 0
        pn3 = 0
        pn4 = 0
        flagD = 0
        flagP = 0
        flag = 0
        result = []
        simulatedTime = 0
        for i in range(0,len(self.defi)):
            if self.defi[i] == "Environment" : 
                de1 = 1
            if self.defi[i] == "Monitor":
                de2 = 1
            if self.defi[i] == "StarSensor":
                de3 = 1
            if self.defi[i] == "Device":
                de4 = 1
            if de1 == 1 and de2 == 1 and de3 == 1 and de4 == 1:
                myEnv = En.Environment()
                myEnv.getTime()
                #Mon = Mo.Monitor
                Devices = De.device()
                Devices.configure(myEnv)
                flagD = 1
        if flagD == 0:
            raise ValueError("Controller.run:  invalid file")
        for i in range (0,len(self.pName)):
            if self.pName[i] == "rotationalPeriod" :
                pn1 = 1
            if self.pName[i] == "logFile":
                pn2 = 1
            if self.pName[i] == "fieldOfView":
                pn3 = 1
            if self.pName[i] == "starFile":
                pn4 = 1
            if pn1 == 1 and pn2 == 1 and pn3== 1 and pn4==1:
                fov = float(self.pElement[2])
                myStarSensor = ss.StarSensor(fov)
                myStarSensor.initializeSensor(self.pElement[3]) 
                #Mon.initialize(self.pElement[1])  
                myEnv.setRotationalPeriod(int(self.pElement[0]))
                myStarSensor.configure(myEnv)
                #Mon.configure(myEnv)
                myEnv.incrementTime(microseconds)   
              
                flagP = 1
        if flagP == 0:
            raise ValueError("Controller.run:  invalid parameter")
        #if microseconds > self.timeLimit:
        #    flag = 1
        if len(self.res) > 0:
            while flag==0:
                for i in range(0,len(self.res)):
                    if self.res[i] == "Device":
                        r = Devices.serviceRequest()
                        result.append(r)
                        simulatedTime += 40
                    if self.res[i] == "StarSensor":
                        r = myStarSensor.serviceRequest()
                        result.append(r)
                        simulatedTime += 40
                    if (microseconds+simulatedTime) > self.timeLimit:
                        flag = 1 
                        break
        else:
            raise ValueError("Controller.run: invalid Frame")
        #print result
        #print len(result)            
        return simulatedTime
        
c = Controller()
f = c.initialize('abc.xml')
a = c.run(990000) 
print a 
print f
