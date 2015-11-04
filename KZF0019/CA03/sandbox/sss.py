'''
Created on Nov 4, 2015

@author: KevinFAN
'''
'''
Created on 9/29/2015

@author: Ting Cao
'''
import CA02.prod.Environment as En
import math

class StarSensor(object):
    global bright
    global id
    global brightGM
    bright = []
    id = []
    brightGM = []
    def __init__(self,fieldOfView =None):
        if fieldOfView <= 0 or fieldOfView >math.pi/4 or float(fieldOfView) == False:
            raise ValueError("StarSensor.__init__:  ")
        self.fieldOfView = fieldOfView             
        
    def initializeSensor(self,starFile = None):
        if(starFile == None):
            raise ValueError("StarSensor.initializeSensor:  ")
        else:
            try:
                #global lines
                f = file(starFile)      
                self.lines = f.readlines() 
                #print "lines:" , lines  
                length = 0
                for line in self.lines[0:]:
                    length += 1
                    data = line.split() 
                
                    try :
                        float(data[0])
                        float(data[1])
                    except: 
                        raise ValueError("invalid data")                       
                    bright.append(data[1])
                    id.append(data[0]) 
                #self.f.close() 
            except:
                raise ValueError("StarSensor.initializeSensor:  file contains invalid information")      
        #else:
        #   raise ValueError("StarSensor.initializeSensor:  file contains invalid information")
        return length
    def getSensorPosition(self):
        try:
            StarSensorRA = float(math.pi/2 + (self.myEnv.getTime())*(2*math.pi)/((23*60*60+56*60+4.1)*1000000))
            StarSensorDec = float(( self.myEnv.getTime())*(2*math.pi)/self.myEnv.getRotationalPeriod())
            
        except:
            return [None,None]
        while StarSensorRA >= 2*math.pi:
            StarSensorRA = StarSensorRA-2*math.pi
        while StarSensorRA <= -2*math.pi:
            StarSensorRA = StarSensorRA+2*math.pi
        while StarSensorDec >= 2*math.pi:
            StarSensorDec = StarSensorDec-2*math.pi
        while StarSensorDec <= -2*math.pi:
            StarSensorDec = StarSensorDec+2*math.pi
        return [StarSensorRA,StarSensorDec]
                
    def configure(self,environment = None):
        if not(isinstance(environment, En.Environment)):
            raise ValueError("StarSensor.configure:  ")
        self.myEnv = environment
        return True
    
    def serviceRequest(self):
        try:
            raCenter = float(math.pi/2+ self.myEnv.getTime()*(2*math.pi)/(((23 * 60 * 60) + (56 * 60) + 4.1) * 1000000))
            decCenter = float((self.myEnv.getTime())*(2*math.pi)/self.myEnv.getRotationalPeriod())
            #print "RA: " , raCenter
            #print "getTime():" ,self.myEnv.getTime()
            #print "self.myEnv.getRotationalPeriod():" , self.myEnv.getRotationalPeriod()
            #print "DEC: ", decCenter
        except:
            return None
        while raCenter- self.fieldOfView/2  >= 2 * math.pi:
            raCenter = raCenter-2*math.pi
        while decCenter  >=  math.pi:
            decCenter = decCenter-2*math.pi
        try:
            a = float(raCenter - self.fieldOfView/2)
            b = float(raCenter + self.fieldOfView/2)
            c = float(decCenter - self.fieldOfView/2) 
            d = float(decCenter + self.fieldOfView/2)
        except:
            raise ValueError("")

        for line in self.lines[0:]:
            data = line.split()
            if ((float(data[2])>=a and float(data[2])<=b)):
                if((float(data[3])>=c and float(data[3])<=d)):
                    brightGM.append(data[1])
        bright=9999.0
        for i in brightGM:
            if bright>float(i):
                bright=float(i)
        del brightGM[:]
        a = bright*10
        a = int(a)
        b = hex(a)
        tempStr = 'x'
        c = b.find(tempStr)
        d = b[(b.find(tempStr)+1):]
        if bright>=1.6 and bright<25.6:
            d = "00"+d
        elif bright>=0 and bright<1.6:
            d ="000"+d
        elif bright>=25.6 and bright<409.6:
            d = "0"+d
        elif bright<0 and bright>=-383.9:
            b = hex(4095+a)
            c = b.find(tempStr)
            d = b[(b.find(tempStr)+1):]
            d = "f"+d
        else:
            d = None
        minBright = d
        self.myEnv.incrementTime(40)
        try:
            return minBright
        except:
            return None
            raise ValueError("")  
        
