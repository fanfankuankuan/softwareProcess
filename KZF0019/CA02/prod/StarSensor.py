'''
Created on Oct 1, 2015

@author: KevinFAN
'''
import math
import types
from CA02.prod import Environment as En
from genericpath import isfile


class StarSensor(object):
    env = None
    def __init__(self, fieldOfView=None):
        if fieldOfView == None:
            raise ValueError("StarSensor.__init__:  fieldOfView cannot be none")
        if not(fieldOfView > 0 and fieldOfView <= (math.pi / 4)):
            raise ValueError("StarSensor.__init__:  fieldOfView invalid")
        self.fieldView = fieldOfView
        
    def initializeSensor(self, starFile = None):
        starCount = 0
        if(starFile == None):
            raise ValueError("StarSensor.initializeSensor:  invalid file type")
        if not(isinstance(starFile, types.StringType)):
            raise ValueError("StarSensor.initializeSensor:  invalid file name")
        if not isfile(starFile):
            raise ValueError("StarSensor.initializeSensor:  no file exists by the specified file name")
        try:
            self.starFile = starFile
            fr = open(starFile, 'r')
            fw = open("Data.txt",'w')
            self.lines = fr.readlines()
            for line in self.lines[0:]:
                #infors = line.split()
                #for i in range(0,len(infors)):
                #    infors[i] = (float)(infors[i])
                #    print infors
                #fw.write(line)
                starCount += 1
            #print starCount
            return starCount
        except Exception, ex:
            print ex
            raise ValueError("StarSensor.initializeSensor:  file contains invalid information")
        finally:
            fw.close()
            fr.close()
    def StarSensor(self,fieldview=None):
        self.fieldView = fieldview
        self.env.__init__()
    def configure(self, environment = None):
        if not(isinstance(environment, En.Environment)):
            raise ValueError("StarSensor.configure:  the file is invalid.")
        if (environment == None):
            raise ValueError("StarSensor.configure:  the file is empty.")
        self.env = environment
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
        

    
    def getSensorPosition(self):
        rightAscension =  math.pi / 2 + self.env.getTime() * 2 * math.pi / (86164.1*1000000)
        declination =  self.env.getTime() * 2 * math.pi / self.env.getRotationalPeriod()
        for i in range(0,99999,1):
            #print i
            if rightAscension >= 2*math.pi:
                rightAscension = rightAscension-2*math.pi
        return [rightAscension,declination]