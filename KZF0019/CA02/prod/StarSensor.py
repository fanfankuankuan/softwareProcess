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
        #finally:
        #    fw.close()
        #    fr.close()
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
     
        list2 = []
     
        if (self.env == None ):
            #print 'a'
            return None
        else:
            rightAscension =  math.pi / 2 + self.env.getTime() * 2 * math.pi / (86164.1*1000000)
            declination = self.env.getTime() * 2 * math.pi / self.env.getRotationalPeriod()
            
            while (rightAscension-self.fieldView/2) >= 2 * math.pi:
                rightAscension = rightAscension - 2 * math.pi
                
            while (declination-self.fieldView/2) >= math.pi:
                declination = declination - 2 * math.pi
                
            xMaxnum = float(rightAscension+self.fieldView/2)    #calculate the Max number in the x axle  
            xMinnum = float(rightAscension-self.fieldView/2)    #calculate the Min number in the x axle
            yMaxnum = float(declination+self.fieldView/2)       #calculate the Max number in the y axle
            yMinnum = float(declination-self.fieldView/2)       #calculate the Min number in the y axle
            #print xMaxnum,xMinnum,yMaxnum,yMinnum
            
            try:    
                with open(self.starFile) as f:
                
                    content = f.readlines()
                    for i in content[0:]:
                        
                        fields = i.split()   
                        print fields
                        if ((float(fields[2]) <= xMaxnum and float(fields[2]) >= xMinnum) ): 
                            if ((float(fields[3]) <= yMaxnum and float(fields[3]) >= yMinnum)):                           
                                list2.append(fields[1])
                            #print "ID",fields[0], "star is in the square, its brightness is ", fields[1] 
                            else:
                                pass
                            #raise ValueError("Invalid input")
                        else:
                            pass
                #print list2
                minbr = 9999
                for k in list2:
                    if float(minbr) > float(k):
                            minbr = k
                    #if minbr == 9999:
                    #    minbr = None
                
                x= float(minbr)
                a = x*10
                a = int(a)
                b = hex(a)
                tempStr = 'x'
                c = b.find(tempStr)
                d = b[(b.find(tempStr)+1):]
                if x>=1.6 and x<25.6:
                    d = "00"+d
                    print d
                elif x>=0 and x<1.6:
                    d ="000"+d
                    print d
                elif x>=25.6 and x<409.6:
                    d = "0"+d
                    print d
                elif x>=409.6:
                    print d
                elif x<0 and x>=-383.9:
                    b = hex(4095+a)
                    c = b.find(tempStr)
                    d = b[(b.find(tempStr)+1):]
                    d = "f"+d
                    print d
                else:
                    raise ValueError("")
                minBright = d
                #self.env.incrementTime(40)
                try:
                    if minBright=="18696":
                        return None
                    return minBright 
                except:
            
                    return None
                    raise ValueError("Sensor.serviceRequest: invalid return")  
                
                #return hex(float(minbr))         
            except:
                pass
            self.env.incrementTime(40)

    
    def getSensorPosition(self):
        rightAscension =  math.pi / 2 + self.env.getTime() * 2 * math.pi / (86164.1*1000000)
        declination =  self.env.getTime() * 2 * math.pi / self.env.getRotationalPeriod()
        for i in range(0,99999,1):
            #print i
            if rightAscension >= 2*math.pi:
                rightAscension = rightAscension-2*math.pi
        return [rightAscension,declination]