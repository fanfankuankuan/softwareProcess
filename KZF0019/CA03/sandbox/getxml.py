'''
Created on Oct 27, 2015

@author: KevinFAN
'''
#import  xml.etree.cElementTree as etr
import  xml.dom.minidom
#3dom = etr.parse('abc.xml')
dom = xml.dom.minidom.parse('abc.xml')
#root = dom.getroot()
#list1 = []
#for i in range(0,len(root)):
#    list1.append(root[i].text)
#print list1
root = dom.documentElement

cc=dom.getElementsByTagName('parm')
c = []
for i in range(0,len(cc)):
    c.append(cc[i].firstChild.data)
    print cc[i].firstChild.data
print c

b = []
itemlist = root.getElementsByTagName('definition')
for i in range(0,len(itemlist)):
    item = itemlist[i]
    un=item.getAttribute("component")
    b.append(un)
print b


