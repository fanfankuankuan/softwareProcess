'''
Created on Oct 27, 2015

@author: KevinFAN
'''
import  xml.etree.cElementTree as etr

dom = etr.parse('abc.xml')
root = dom.getroot()
list1 = []
for i in range(0,len(root)):
    list1.append(root[i].text)
print list1

