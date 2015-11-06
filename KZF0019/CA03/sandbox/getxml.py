'''
Created on Oct 27, 2015

@author: KevinFAN
'''
#import  xml.etree.cElementTree as etr
import  xml.dom.minidom
from xml.etree import ElementTree as ET
#3dom = etr.parse('abc.xml')
try:
    dom = xml.dom.minidom.parse('ab.xml')
except:
    assert ValueError("XXX")
#root = dom.getroot()
#list1 = []
#for i in range(0,len(root)):
#    list1.append(root[i].text)
#print list1
dom = xml.dom.minidom.parse('abc.xml')
root = dom.documentElement

bb = root.nodeName
print bb

a=[]

cc=dom.getElementsByTagName('parm')
c = []
for i in range(0,len(cc)):
    c.append(cc[i].firstChild.data)
    item = cc[i]
    un=item.getAttribute("name")
    a.append(un)
    #c.append(cc[i].secondChild.data)
    #print cc[i].firstChild.data
    #print i
print "parm"
print c
print "name"
print a

zz = dom.getElementsByTagName("frame")
z = []
for i in range(0,len(zz)):
    ite = zz[i]
    ui = ite.getAttribute("rate")
    z.append(ui)
print "rate"
print z
    

bb = dom.getElementsByTagName('definition')

b= []
for i in range(0,len(bb)):
    item = bb[i]
    un = item.getAttribute("component")
    b.append(un)
    #print un
    
print "component"
print b
print "\n"

dd = dom.getElementsByTagName('device')
d = []
for i in range(0,len(dd)):
    d.append(dd[i].firstChild.data)
    #print dd[i].firstChild.data
print "device"    
print d

for child in dom.childNodes :
        if child.tagName == "frame" :
            rate = child.getAttribute("rate")
            print rate
            if rate == None:
                raise ValueError("Controller.initialize:  rate doesn't exist")
