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


cc=dom.getElementsByTagName('parm')
c = []
for i in range(0,len(cc)):
    c.append(cc[i].firstChild.data)
    #c.append(cc[i].secondChild.data)
    print cc[i].firstChild.data
    print i
print c

bb = dom.getElementsByTagName('definition')

b= []
for i in range(0,len(bb)):
    item = bb[i]
    un = item.getAttribute("component")
    b.append(un)
    print un


per=ET.parse('abc.xml')
p=per.findall('./configuration/definition')

for oneper in p:
    for child in oneper.getchildren():
        print child.tag,'',child.text
print b