'''
Created on Oct 3, 2015

@author: KevinFAN
'''
import CA02.prod.StarSensor as StarSensor
import CA02.prod.Environment as Environment
import math 
 
# instantiate the simulation environment 
simEnv = Environment.Environment() 
 
rotationalPeriod = 1000000 * 3 
simEnv.setRotationalPeriod(microseconds=rotationalPeriod) 
 
# 2 degrees = 2*pi*2/360 radians 
fov = (2.0 / 360.0) * (2.0 * math.pi) 
sensor = StarSensor.StarSensor(fov) 
 
# provide the star sensor with candidate stars <-------------------------- new
sensor.initializeSensor("Sao.txt")                    
 
# give the star sensor access to environmental information 
sensor.configure(simEnv) 
starSightings = [] 
increment = 10 * 1000000 
for time in range(0, 5 * 60 * 1000000, increment): 
    timeOfNextIncrement = simEnv.getTime() + increment 
    starSightings.append(sensor.serviceRequest()) 
    simEnv.incrementTime(timeOfNextIncrement - simEnv.getTime())
    print sensor.getSensorPosition()
#print starSightings
      

