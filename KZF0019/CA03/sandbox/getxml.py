'''
Created on Oct 27, 2015

@author: KevinFAN
'''
import  xml.dom.minidom

dom = xml.dom.minidom.parse('abc.xml')
root = dom.documentElement

print dom
print root.nodeName
print root.nodeValue
print root.nodeType