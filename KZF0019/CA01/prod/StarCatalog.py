'''
Created on Sep 1, 2015

@author: KevinFAN
'''

import string     #import method to help
import os
import math
path = os.path.expanduser(r"~/Documents/COMP 6700/Sao.txt")  #define a path to find the local file

class StarCatalog(object):
    # define global variable
    
    def __init__(self):        
        pass
    def loadCatalog(self,starFile=None):   #define star loading function
        global starFile1 
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        
        if(starFile == None):
            raise ValueError("Invalid file type")   #throw an error
        if(isinstance(starFile,str)):
            starFile1 = starFile
            try: 
                j = 0                        #define a variable helps to count
                
                with open(starFile1) as f:    #open the file
                    content = f.read()       #read the file
                    for i in content.splitlines():    #split the file into several lines
                        fields = i.split('\t')        #split the line
                        j += 1
                        try :
                            float(fields[0])
                            float(fields[1])
                            float(fields[2])
                            float(fields[3])
                        except:
                            raise ValueError("invalid data")
                        #print fields[2]              #Use to fix bug
                        list1.append(fields[0])       #add the value into list
                        list2.append(fields[1])
                        list3.append(fields[2])
                        list4.append(fields[3])
                    print "There are",j,"stars"         #count the star number
                    return j
            except:
                raise ValueError("StarCatalog.loadCatalog:cannot open the file")
        else :
            raise ValueError("StarCatalog.loadCatalog:invalid file name")    
    def getStarCount(self,lowerMagnitude=-999, upperMagnitude=999):   #define a Star counting function
        if lowerMagnitude <= upperMagnitude:
            list1 = []
            list2 = []
            list3 = []
            list4 = []
            try:
                with open(starFile1) as f:

                    MaxM = upperMagnitude    #define the biggest number
                    MinM = lowerMagnitude    #define the smallest number
                    content = f.read()
                    j = 0                    #define a variable helps to count
                    for i in content.splitlines():
                        fields = i.split('\t')
                        if (string.atof(fields[1]) <= MaxM and string.atof(fields[1]) >= MinM):
                            j += 1
                            print "ID",fields[0], "star is in the square, its brightness is ", fields[1] 
                            list1.append(fields[0])      #add the value into list
                            list2.append(fields[1])    
                            list3.append(fields[2])
                            list4.append(fields[3])  
                    print "There are",j,"stars in the square." 
                    return j
                    
            except:
                raise ValueError("StarCatalog.getStarcount:invalid input")
                #print "Invalid files"
        else:
            raise ValueError("StarCatalog.getStarCount:invalid input")
    def emptyCatalog(self):      #define a deleting function
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        try: 
            j = 0                        #define a variable helps to count
                
            with open(starFile1) as f:    #open the file
                
                content = f.read()       #read the file
                   
                for i in content.splitlines():    #split the file into several lines
                    fields = i.split('\t')        #split the line
                    j += 1
                    #print fields[2]              #Use to fix bug
                    list1.append(fields[0])       #add the value into list
                    list2.append(fields[1])
                    list3.append(fields[2])
                    list4.append(fields[3])
        except:
            print "There is no file!"             #throw a exception
        for i in range(0, len(list1)):
            
            list1.pop()          #throw the value of list away
            list2.pop()
            list3.pop()
            list4.pop()           
        print "The system has deleted:",i+1,"stars"   #count the deleted star number
        return i+1
    def getMagnitude(self,rightAscensionCenterPoint=None,declinationCenterPoint=None,fieldOfView=None):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        try:
            xMaxnum = float(rightAscensionCenterPoint+fieldOfView/2)    #calculate the Max number in the x axle  
            xMinnum = float(rightAscensionCenterPoint-fieldOfView/2)    #calculate the Min number in the x axle
            yMaxnum = float(declinationCenterPoint+fieldOfView/2)       #calculate the Max number in the y axle
            yMinnum = float(declinationCenterPoint-fieldOfView/2)       #calculate the Min number in the y axle
            
            with open(starFile1) as f:
                j = 0
                content = f.read()
                for i in content.splitlines():
                    fields = i.split('\t')       
                    #print fields[2]
                    if ((float(fields[2]) <= xMaxnum and float(fields[2]) >= xMinnum) or (float(fields[2]) <= xMaxnum-2*math.pi and float(fields[2]) >= xMinnum - 2*math.pi) or (float(fields[2]) <= xMaxnum+2*math.pi and float(fields[2]) >= xMinnum+2*math.pi)): 
                        if ((float(fields[3]) <= yMaxnum and float(fields[3]) >= yMinnum) or (float(fields[3]) <= yMaxnum - 2*math.pi and float(fields[3]) >= yMinnum -2*math.pi) or (float(fields[3]) <= yMaxnum + 2*math.pi and float(fields[3]) >= yMinnum + 2*math.pi)):
                            j += 1
                            #print "ID",fields[0], "star is in the square, its brightness is ", fields[1] 
                            list1.append(fields[0])     #add the value into list
                            list2.append(fields[1])
                            list3.append(fields[2])
                            list4.append(fields[3])
                        else:
                            pass
                            #raise ValueError("Invalid input")
                    else:
                        pass
                        #raise ValueError("Invalid input")
                #print "There are ",j,"stars in the square." 
                print list2              
                #minbr = min(list2)
                minbr = 9999
                for k in list2:
                    if float(minbr) > float(k):
                        minbr = k
                if minbr == 9999:
                    minbr = None
                print "The bright star ID is ", list1[list2.index(minbr)],",its brightness is: ",minbr 
                return float(minbr)
                
        except :
            #diagnosticString2 = e.args[0]
            #raise ValueError( "Error,please try again" )   #throw an error
            return None
#stars = StarCatalog()       #call function of the class
#readStar = stars.loadCatalog(path)
#brightestStar = stars.getMagnitude(1.71239554, 0.3452005, 2.17453)
#starsBetween2And5 = stars.getStarCount(1,5)
#deleteStar = stars.emptyCatalog() 