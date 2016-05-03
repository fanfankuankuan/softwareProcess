'''
Created on Mar 30, 2016

@author: KevinFAN
'''
speed = 15000
delay = 0.005
import random
class traffic1(object):
    def __init__(self):
        pass
    def project(self):
        i = 0
        sumpacket = 0
        droppacket = 0
        while(i<10):
            time = 0.0
            selectnode1 = random.randrange(1,6)
            selectnode2 = random.randrange(1,6) 
            packet = random.randrange(0,1024)
            if selectnode1 == selectnode2 :
                droppacket = droppacket + 1
            if selectnode2 == 3:
                time = time + delay + float(packet/speed)
                print "The first delay is " + str(time)
                i = i + 1
                sumpacket = packet + sumpacket
            else:
                time = time + 2* delay + 2* float(packet/speed)
                print "The second delay is " + str(time)
                i = i + 1
                sumpacket = packet + sumpacket
        print sumpacket
        print droppacket
start = traffic1()
run = start.project()